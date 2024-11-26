<template>
  <div class="quiz-content">
    <!-- 돌아가기 버튼 추가 -->
    <button @click="$emit('game-end')" class="back-btn">
      ← 퀴즈 선택으로
    </button>

    <!-- 퀴즈 진행 화면 -->
    <div v-if="!showResult">
      <div class="quiz-header">
        <div class="quiz-info">
          <h2>문제 {{ currentQuizIndex + 1 }} / {{ quizzes.length }}</h2>
          <div class="current-level">고급</div>
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
        <div class="section-header">
          <h3>틀린 문제 리뷰</h3>
        </div>
        <div class="wrong-answers-list">
          <div v-for="(quiz, index) in wrongAnswers" 
               :key="index" 
               class="wrong-quiz">
            <p class="question">Q. {{ quiz.body }}</p>
            <div class="answer-box">
              <div class="answer-item correct-answer">
                <span class="answer-label">정답</span>
                <span class="answer-text">{{ quiz.correct_choice }}</span>
              </div>
              <div class="answer-item wrong-answer">
                <span class="answer-label">선택한 답</span>
                <span class="answer-text">{{ quiz.user_choice }}</span>
              </div>
            </div>
          </div>
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

const quizzes = ref([])             // 퀴즈 목록
const currentQuizIndex = ref(0)     // 현재 문제의 인덱스
const score = ref(0)                // 점수
const userAnswer = ref('')           // 사용자가 선택한 답
const showResult = ref(false)        // 결과 화면 표시 여부
const correctAnswers = ref(0)        // 맞힌 문제 개수
const showAnswer = ref(false)      // 정답 공개 여부
const wrongAnswers = ref([])       // 틀린 문제 목록


const loadQuizzes = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/v1/quiz_game/quiz/random/5/', {
      params: { level: 'advanced' },
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
  max-width: 900px;
  margin: 2rem auto;
  padding: 2.5rem;
  background: #ffffff;
  border-radius: 20px;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.05);
  position: relative;
}

/* 돌아가기 버튼 스타일 */
.back-btn {
  position: absolute;
  top: 1.5rem;
  left: 1.5rem;
  padding: 0.8rem 1.2rem;
  background: white;
  border: 3px solid #88C9F2;
  border-radius: 12px;
  color: #34343f;
  font-family: 'DNFBitBitv2';
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 0 #F25E86;
}

.back-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 0 #F25E86;
  border-color: #F2B705;
}

.quiz-header {
  background: linear-gradient(145deg, #88C9F2, #9CD95F);
  padding: 1.5rem;
  border-radius: 15px;
  border: 3px solid #F2B705;
  margin: 2rem 0;
  color: white;
  box-shadow: 0 4px 0 #88C9F2;
}

.quiz-info h2 {
  font-family: 'DNFBitBitv2';
  color: white;
  text-shadow: 2px 2px 0 rgba(0, 0, 0, 0.2);
}

.current-level {
  display: inline-block;
  padding: 0.4rem 1rem;
  background: white;
  border-radius: 20px;
  color: #F25E86;
  font-weight: bold;
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

.score {
  font-family: 'DNFBitBitv2';
  font-size: 1.4rem;
  color: #F2B705;
  text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.2);
}

.quiz-question {
  font-family: 'DNFBitBitv2';
  font-size: 1.5rem;
  color: #34343f;
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
  background: white;
  border: 3px solid #88C9F2;
  border-radius: 12px;
  font-family: 'DNFBitBitv2';
  font-size: 1.1rem;
  color: #34343f;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 0 #F25E86;
  text-align: left;
}

.choice-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 0 #F25E86;
  border-color: #F2B705;
}

.choice-btn.correct {
  background: #9CD95F;
  color: white;
  border-color: #F2B705;
}

.choice-btn.wrong {
  background: #F25E86;
  color: white;
  border-color: #F2B705;
}

/* 결과 화면 스타일 수정 */
.result-screen {
  text-align: center;
  padding: 2rem;
}

.result-screen h2 {
  font-family: 'DNFBitBitv2';
  color: #34343f;
  font-size: 2.2rem;
  margin-bottom: 2rem;
}

.restart-btn {
  background: linear-gradient(145deg, #F25E86, #F29F05);
  padding: 1.2rem 2.5rem;
  border: none;
  border-radius: 15px;
  color: white;
  font-family: 'DNFBitBitv2';
  font-size: 1.3rem;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 4px solid #F2B705;
  box-shadow: 0 6px 0 #F25E86;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.2);
}

.restart-btn:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 0 #F25E86;
}

@font-face {
  font-family: 'DNFBitBitv2';
  font-style: normal;
  font-weight: 400;
  src: url('//cdn.df.nexon.com/img/common/font/DNFBitBitv2.otf') format('opentype');
}

/* 반응형 스타일은 그대로 유지 */

.wrong-answers {
  margin-top: 3rem;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  border: 4px solid #88C9F2;
  box-shadow: 0 8px 0 #F25E86;
  overflow: hidden;
  margin-bottom: 2rem;
}

.wrong-answers .section-header {
  background: linear-gradient(145deg, #88C9F2, #9CD95F);
  padding: 1.2rem 1.5rem;
  border-bottom: 4px solid #F2B705;
}

.wrong-answers .section-header h3 {
  font-family: 'DNFBitBitv2';
  font-size: 1.8rem;
  color: white;
  margin: 0;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.2);
}

.wrong-answers-list {
  padding: 1.5rem;
}

.wrong-quiz {
  background: linear-gradient(145deg, #fff, #f8f9fa);
  padding: 1.5rem;
  border-radius: 12px;
  border: 3px solid #88C9F2;
  box-shadow: 0 4px 0 #F25E86;
  transition: all 0.3s ease;
  margin-bottom: 1.5rem;
  animation: slideIn 0.3s ease-out;
}

.wrong-quiz:hover {
  transform: translateY(-4px);
  border-color: #F2B705;
  box-shadow: 0 8px 0 #F25E86;
}

.wrong-quiz:last-child {
  margin-bottom: 0;
}
</style>