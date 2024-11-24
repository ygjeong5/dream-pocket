<template>
  <div class="quiz-content">
    <!-- 퀴즈 진행 화면 -->
    <div v-if="!showResult">
      <div class="quiz-header">
        <div class="quiz-info">
          <h2>문제 {{ currentQuizIndex + 1 }} / {{ quizzes.length }}</h2>
          <div class="current-level">초급</div>
        </div>
        <div class="score">점수: {{ score }}</div>
      </div>

      <div v-if="currentQuiz" class="quiz-question-container">
        <h3 class="quiz-question">{{ currentQuiz.body }}</h3>
        <div class="choices">
          <button 
            v-for="(choice, key) in quizChoices" 
            :key="key"
            @click="submitAnswer(key)"
            :class="['choice-btn', { 
              selected: userAnswer === key,
              correct: showAnswer && key === currentQuiz.correct_answer,
              wrong: showAnswer && userAnswer === key && key !== currentQuiz.correct_answer
            }]"
            :disabled="showAnswer"
          >
            {{ choice }}
          </button>
        </div>
      </div>
    </div>

    <!-- 결과 화면 -->
    <div v-else class="result-screen">
      <h2>퀴즈 결과</h2>
      <div class="result-info">
        <p>총점: {{ score }}점</p>
        <p>맞은 개수: {{ correctAnswers }}개 / {{ quizzes.length }}개</p>
      </div>

      <!-- 틀린 문제 리뷰 -->
      <div v-if="wrongAnswers.length > 0" class="wrong-answers">
        <h3>틀린 문제 리뷰</h3>
        <div v-for="(quiz, index) in wrongAnswers" :key="index" class="wrong-quiz">
          <p class="question">Q. {{ quiz.body }}</p>
          <p class="answer">
            <span class="correct-answer">정답: {{ quiz.correct_choice }}</span>
            <span class="wrong-answer">선택한 답: {{ quiz.user_choice }}</span>
          </p>
        </div>
      </div>

      <button @click="$emit('game-end')" class="restart-btn">다시 시작하기</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import { useEggStore } from '@/stores/egg'

const emit = defineEmits(['game-end'])
const store = useEggStore()

const quizzes = ref([])
const currentQuizIndex = ref(0)
const score = ref(0)
const userAnswer = ref('')
const showResult = ref(false)
const correctAnswers = ref(0)
const showAnswer = ref(false)
const wrongAnswers = ref([])

const loadQuizzes = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/v1/quiz_game/quiz/random/5/', {
      params: { level: 'beginner' },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    quizzes.value = response.data
  } catch (error) {
    console.error('Error:', error)
    alert('퀴즈를 불러오는데 실패했습니다.')
  }
}

const currentQuiz = computed(() => quizzes.value[currentQuizIndex.value] || null)

const quizChoices = computed(() => {
  if (!currentQuiz.value) return {}
  return {
    'A': currentQuiz.value.choice_a,
    'B': currentQuiz.value.choice_b,
    'C': currentQuiz.value.choice_c,
    'D': currentQuiz.value.choice_d
  }
})

const submitAnswer = async (answer) => {
  if (showAnswer.value) return
  
  userAnswer.value = answer
  showAnswer.value = true
  
  const isCorrect = currentQuiz.value.correct_answer === answer
  if (isCorrect) {
    score.value += 20
    correctAnswers.value++
  } else {
    // 틀린 문제 저장
    wrongAnswers.value.push({
      body: currentQuiz.value.body,
      correct_choice: quizChoices.value[currentQuiz.value.correct_answer],
      user_choice: quizChoices.value[answer],
      explanation: currentQuiz.value.explanation // 문제 해설이 있다면
    })
  }

  await new Promise(resolve => setTimeout(resolve, 1000))
  showAnswer.value = false
  
  if (currentQuizIndex.value < quizzes.value.length - 1) {
    currentQuizIndex.value++
    userAnswer.value = ''
  } else {
    showResult.value = true
  }
}

onMounted(() => {
  loadQuizzes()
})
</script>

<style scoped>
.quiz-content {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background: white;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.quiz-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid #eee;
}

.quiz-info h2 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.current-level {
  color: #666;
  font-size: 0.9em;
}

.score {
  font-size: 1.2em;
  font-weight: bold;
  color: #4CAF50;
}

.quiz-question {
  font-size: 1.4em;
  color: #2c3e50;
  margin-bottom: 2rem;
  line-height: 1.5;
}

.choices {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.choice-btn {
  padding: 1.2rem;
  border: 2px solid #4CAF50;
  border-radius: 10px;
  background: white;
  color: #4CAF50;
  font-size: 1.1em;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: left;
}

.choice-btn:hover {
  background: #4CAF50;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(76,175,80,0.2);
}

.choice-btn.selected {
  background: #4CAF50;
  color: white;
  transform: translateY(-2px);
}

/* 결과 화면 스타일 */
.result-screen {
  text-align: center;
  padding: 2rem;
}

.result-screen h2 {
  color: #2c3e50;
  font-size: 2em;
  margin-bottom: 2rem;
}

.result-info {
  margin: 2rem 0;
}

.result-info p {
  font-size: 1.3em;
  color: #34495e;
  margin: 1rem 0;
}

.restart-btn {
  padding: 1rem 2rem;
  font-size: 1.2em;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.restart-btn:hover {
  background-color: #45a049;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(76,175,80,0.2);
}

@media (max-width: 768px) {
  .choices {
    grid-template-columns: 1fr;
  }
  
  .quiz-content {
    margin: 1rem;
    padding: 1rem;
  }
  
  .quiz-question {
    font-size: 1.2em;
  }
  
  .choice-btn {
    padding: 1rem;
    font-size: 1em;
  }
}

.wrong-answers {
  margin: 2rem 0;
  text-align: left;
}

.wrong-quiz {
  background: #f8f9fa;
  padding: 1.5rem;
  margin: 1rem 0;
  border-radius: 12px;
  border-left: 4px solid #f44336;
}

.question {
  font-weight: bold;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.answer {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.correct-answer {
  color: #4CAF50;
  font-weight: 500;
}

.wrong-answer {
  color: #f44336;
  font-weight: 500;
}

.choice-btn.correct {
  background-color: #4CAF50;
  color: white;
  border-color: #4CAF50;
}

.choice-btn.wrong {
  background-color: #f44336;
  color: white;
  border-color: #f44336;
}

/* 애니메이션 효과 */
.wrong-quiz {
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>