<template>
  <div class="quiz-content">
    <!-- 돌아가기 버튼 추가 -->
    <button @click="$emit('game-end')" class="back-btn">
      레벨 선택으로
    </button>

    <!-- 퀴즈 진행 화면 -->
    <div v-if="!showResult">
      <div class="quiz-header">
        <div class="quiz-info">
          <h2>문제 {{ currentQuizIndex + 1 }} / {{ quizzes.length }}</h2>
          <div class="current-level">중급</div>
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

const userInfo = ref({})
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
      params: { level: 'intermediate' },
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
    updateUserPoint()
  }
}
const updateUserPoint = () => {
  axios({
    method: 'put',
    url: 'http://127.0.0.1:8000/accounts/user-info/',
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: {
      point: userInfo.value.point + Math.floor(score.value / 5),
    },
  })
} 

onMounted(() => {
  loadQuizzes()
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/accounts/user-info/',
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(res => {
      userInfo.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
})
</script>

<style scoped>
.quiz-content {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2.5rem;
  background: #ffffff;
  border-radius: 24px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
  position: relative;
  font-family: 'DNFBitBitv2';
}

.quiz-header {
  background: linear-gradient(135deg, #6B8CFF, #7D5FFF);
  padding: 2rem;
  border-radius: 20px;
  margin-bottom: 2.5rem;
  position: relative;
  overflow: hidden;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.quiz-header::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1));
}

.quiz-info h2 {
  color: white;
  margin: 0;
  letter-spacing: 1px;
}

.current-level {
  display: inline-block;
  padding: 0.4rem 1rem;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 20px;
  color: #6B8CFF;
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

.score {
  font-size: 1.4rem;
  color: white;
  opacity: 0.9;
}

.quiz-question {
  font-size: 1.4rem;
  color: #2D3436;
  margin: 2rem 0;
  line-height: 1.6;
}

.choices {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.2rem;
  padding: 1rem;
}

.choice-btn {
  padding: 1.2rem;
  background: #ffffff;
  border: none;
  border-radius: 16px;
  font-size: 1.1rem;
  color: #2D3436;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  text-align: left;
}

.choice-btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(107, 140, 255, 0.15);
}

.choice-btn.correct {
  background: linear-gradient(135deg, #6B8CFF, #7D5FFF);
  color: white;
}

.choice-btn.wrong {
  background: #FF6B6B;
  color: white;
}

.result-screen {
  text-align: center;
  padding: 2rem;
}

.result-screen h2 {
  color: #2D3436;
  font-size: 2.2rem;
  margin-bottom: 2rem;
}

.result-info p {
  font-size: 1.3rem;
  color: #2D3436;
  margin: 1rem 0;
}

.wrong-answers {
  margin: 2rem 0;
  background: #ffffff;
  border-radius: 20px;
  box-shadow: 0 8px 25px rgba(107, 140, 255, 0.1);
  overflow: hidden;
}

.wrong-answers h3 {
  background: linear-gradient(135deg, #6B8CFF, #7D5FFF);
  padding: 1.2rem 1.5rem;
  color: white;
  margin: 0;
}

.wrong-quiz {
  padding: 1.5rem;
  margin: 1rem;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.restart-btn {
  background: linear-gradient(135deg, #6B8CFF, #7D5FFF);
  padding: 1.2rem 2.5rem;
  border: none;
  border-radius: 16px;
  color: white;
  font-size: 1.3rem;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 2rem;
}

.restart-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(107, 140, 255, 0.25);
}

@media (max-width: 768px) {
  .choices {
    grid-template-columns: 1fr;
  }
  
  .quiz-content {
    margin: 1rem;
    padding: 1.5rem;
  }
}

@font-face {
  font-family: 'DNFBitBitv2';
  font-style: normal;
  font-weight: 400;
  src: url('//cdn.df.nexon.com/img/common/font/DNFBitBitv2.otf') format('opentype');
}

.back-btn {
  position: absolute;
  top: -3rem;
  left: 0;
  padding: 0.8rem 1.2rem;
  background: white;
  border: none;
  border-radius: 16px;
  color: #2D3436;
  font-family: 'DNFBitBitv2';
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.back-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(107, 140, 255, 0.15);
}
</style>