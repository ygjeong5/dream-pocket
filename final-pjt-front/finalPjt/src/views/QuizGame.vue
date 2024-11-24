<template>
  <div class="quiz-container">
    <div v-if="!gameStarted" class="start-screen">
      <h1>금융 퀴즈</h1>
      <div class="level-selection">
        <button 
          v-for="level in levels" 
          :key="level.value"
          @click="selectLevel(level.value)"
          :class="['level-btn', { active: selectedLevel === level.value }]"
        >
          {{ level.label }}
        </button>
      </div>
      <button @click="startGame" class="start-btn">게임 시작</button>
    </div>

    <div v-else>
      <div class="quiz-header">
        <div class="quiz-info">
          <h2>문제 {{ currentQuizIndex + 1 }} / {{ quizzes.length }}</h2>
          <div class="current-level">{{ getCurrentLevelLabel() }}</div>
        </div>
        <div class="score">점수: {{ score }}</div>
      </div>

      <!-- ... 기존 게임 화면 코드 ... -->
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { useEggStore } from '@/stores/egg'

const store = useEggStore()
const selectedLevel = ref('beginner')
const levels = [
  { value: 'beginner', label: '초급' },
  { value: 'intermediate', label: '중급' },
  { value: 'advanced', label: '고급' }
]

const quizzes = ref([])
const currentQuizIndex = ref(0)
const score = ref(0)
const gameStarted = ref(false)
const userAnswer = ref('')
const showResult = ref(false)
const correctAnswers = ref(0)

const selectLevel = (level) => {
  selectedLevel.value = level
}

const getCurrentLevelLabel = () => {
  const level = levels.find(l => l.value === selectedLevel.value)
  return level ? level.label : '초급'
}

const startGame = async () => {
  try {
    const response = await axios.get(`http://localhost:8000/api/v1/quiz/random/5/?level=${selectedLevel.value}`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    quizzes.value = response.data;
    gameStarted.value = true;
    resetGame();
  } catch (error) {
    console.error('퀴즈 데이터를 불러오는데 실패했습니다:', error);
    if (error.response?.status === 401) {
      alert('로그인이 필요한 서비스입니다.');
    } else if (error.response?.status === 404) {
      alert('해당 난이도의 퀴즈가 없습니다.');
    }
  }
}

// ... 기존 methods ...
</script>

<style scoped>
/* ... 기존 스타일 ... */

.level-selection {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin: 30px 0;
}

.level-btn {
  padding: 12px 25px;
  border: 2px solid #4CAF50;
  border-radius: 5px;
  cursor: pointer;
  background-color: white;
  color: #4CAF50;
  font-size: 1.1em;
  transition: all 0.3s ease;
}

.level-btn.active {
  background-color: #4CAF50;
  color: white;
}

.level-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.quiz-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.current-level {
  font-size: 0.9em;
  color: #666;
  margin-top: 5px;
}

/* ... 기존 스타일 ... */

.result-content {
  background-color: white;
  padding: 40px;
  border-radius: 15px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}

.result-content h2 {
  color: #2c3e50;
  margin-bottom: 20px;
}

.result-content p {
  font-size: 1.2em;
  margin: 10px 0;
  color: #34495e;
}

.result-content button {
  margin-top: 25px;
  padding: 12px 30px;
  font-size: 1.1em;
  transition: all 0.3s ease;
}

.result-content button:hover {
  background-color: #45a049;
  transform: translateY(-2px);
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
</style> 