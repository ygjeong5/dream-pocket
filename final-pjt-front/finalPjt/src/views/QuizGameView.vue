<template>
  <div class="quiz-game-container">
    <div v-if="!gameStarted" class="start-screen">
      <div class="game-intro">
        <h1>금융 퀴즈</h1>
        <p class="intro-text">당신의 금융 지식을 테스트해보세요!</p>
      </div>

      <div class="level-selection">
        <button 
          v-for="level in levels" 
          :key="level.value"
          @click="selectLevel(level.value)"
          :class="['level-btn', { active: selectedLevel === level.value }]"
        >
          <div class="level-icon">{{ level.icon }}</div>
          <div class="level-info">
            <h3>{{ level.label }}</h3>
            <p>{{ level.description }}</p>
          </div>
        </button>
      </div>

      <button @click="startGame" class="start-btn">
        게임 시작
      </button>
    </div>

    <div v-else>
      <BeginnerQuiz v-if="selectedLevel === 'beginner'" @game-end="handleGameEnd" />
      <IntermediateQuiz v-if="selectedLevel === 'intermediate'" @game-end="handleGameEnd" />
      <AdvancedQuiz v-if="selectedLevel === 'advanced'" @game-end="handleGameEnd" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import BeginnerQuiz from '../components/quiz/BeginnerQuiz.vue'
import IntermediateQuiz from '../components/quiz/IntermediateQuiz.vue'
import AdvancedQuiz from '../components/quiz/AdvancedQuiz.vue'

const selectedLevel = ref('beginner')
const gameStarted = ref(false)

const levels = [
  { 
    value: 'beginner', 
    label: '초급', 
    icon: '🌱',
    description: '금융의 기초 개념을 배워봅시다!'
  },
  { 
    value: 'intermediate', 
    label: '중급', 
    icon: '🌿',
    description: '심화된 금융 지식을 테스트하세요!'
  },
  { 
    value: 'advanced', 
    label: '고급', 
    icon: '🌳',
    description: '전문가 수준의 도전!'
  }
]

const selectLevel = (level) => {
  selectedLevel.value = level
}

const startGame = () => {
  gameStarted.value = true
}

const handleGameEnd = () => {
  gameStarted.value = false
}
</script>

<style scoped>
.quiz-game-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f5f7fa;
}

.start-screen {
  background: white;
  padding: 3rem;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 100%;
  max-width: 600px;
  animation: fadeIn 0.5s ease-out;
}

.game-intro {
  margin-bottom: 2.5rem;
}

.game-intro h1 {
  color: #2c3e50;
  font-size: 2.5em;
  margin-bottom: 1rem;
  font-weight: 700;
}

.intro-text {
  color: #666;
  font-size: 1.2em;
  margin-bottom: 2rem;
}

.level-selection {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 2.5rem;
}

.level-btn {
  display: flex;
  align-items: center;
  padding: 1.5rem;
  border: 2px solid #4CAF50;
  border-radius: 12px;
  background-color: white;
  color: #4CAF50;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: left;
}

.level-icon {
  font-size: 2em;
  margin-right: 1.5rem;
  min-width: 50px;
  text-align: center;
}

.level-info {
  flex-grow: 1;
}

.level-info h3 {
  font-size: 1.2em;
  margin-bottom: 0.3rem;
  color: #2c3e50;
}

.level-info p {
  font-size: 0.9em;
  color: #666;
  margin: 0;
}

.level-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 15px rgba(76, 175, 80, 0.2);
}

.level-btn.active {
  background-color: #4CAF50;
  color: white;
}

.level-btn.active .level-info h3,
.level-btn.active .level-info p {
  color: white;
}

.start-btn {
  padding: 1.2rem 3rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1.3em;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  letter-spacing: 1px;
  width: 100%;
}

.start-btn:hover {
  background-color: #45a049;
  transform: translateY(-3px);
  box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .quiz-game-container {
    padding: 1rem;
  }

  .start-screen {
    padding: 2rem;
  }

  .game-intro h1 {
    font-size: 2em;
  }

  .level-btn {
    padding: 1rem;
  }

  .level-icon {
    font-size: 1.5em;
    margin-right: 1rem;
    min-width: 40px;
  }

  .start-btn {
    padding: 1rem;
  }
}

/* 호버 효과 비활성화 (모바일) */
@media (hover: none) {
  .level-btn:hover,
  .start-btn:hover {
    transform: none;
    box-shadow: none;
  }
}
</style>