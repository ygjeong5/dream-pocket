<template>
  <div class="quiz-game-container">
    <div v-if="!gameStarted" class="start-screen">
      <section class="intro-header">
        <h1>금융 퀴즈</h1>
        <p class="intro-description">
          당신의 금융 지식을 테스트해보세요!<br>
          <span class="highlight">레벨을 선택</span>하고<br>
          도전을 시작해보세요!
        </p>
      </section>

      <div class="level-selection">
        <button 
          v-for="level in levels" 
          :key="level.value"
          @click="selectLevel(level.value)"
          :class="['level-btn', { active: selectedLevel === level.value }]"
        >
          <div class="level-icon-wrapper">
            <span class="level-icon">{{ level.icon }}</span>
          </div>
          <div class="level-info">
            <h3>{{ level.label }}</h3>
            <p>{{ level.description }}</p>
          </div>
        </button>
      </div>

      <button @click="startGame" class="start-btn">
        게임 시작하기
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

<!-- <style scoped>
.quiz-game-container {
  max-width: 900px;
  margin: 2rem auto;
  padding: 2.5rem;
  background: #ffffff;
  border-radius: 20px;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.05);
  position: relative;
}

.intro-header {
  background: linear-gradient(145deg, #88C9F2, #9CD95F);
  padding: 2.5rem;
  border-radius: 20px;
  text-align: center;
  margin-bottom: 2.5rem;
  border: 4px solid #F2B705;
  box-shadow: 0 6px 0 #88C9F2;
  position: relative;
  overflow: hidden;
}

.intro-header h1 {
  font-family: 'DNFBitBitv2';
  font-size: 2.8rem;
  color: white;
  margin: 0 0 1rem 0;
  text-shadow: 3px 3px 0 rgba(0, 0, 0, 0.2);
}

.intro-description {
  font-family: 'DNFBitBitv2';
  font-size: 1.3rem;
  color: white;
  line-height: 1.8;
  margin: 0;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
}

.highlight {
  color: #F2B705;
  font-weight: bold;
  font-size: 1.4rem;
}

.level-selection {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  margin-bottom: 2rem;
  padding: 0 1rem;
}

.level-btn {
  display: flex;
  align-items: center;
  padding: 1.2rem;
  background: white;
  border: 3px solid #88C9F2;
  border-radius: 15px;
  box-shadow: 0 4px 0 #F25E86;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
}

.level-btn:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 0 #F25E86;
  border-color: #F2B705;
}

.level-btn.active {
  background: linear-gradient(145deg, #88C9F2, #9CD95F);
  border-color: #F2B705;
  color: white;
}

.level-icon-wrapper {
  background: white;
  width: 60px;
  height: 60px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #F2B705;
  margin-right: 1.5rem;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.level-icon {
  font-size: 2rem;
  animation: float 3s ease-in-out infinite;
}

.level-info h3 {
  font-family: 'DNFBitBitv2';
  font-size: 1.4rem;
  margin: 0 0 0.3rem 0;
  color: #34343f;
}

.level-info p {
  font-family: 'DNFBitBitv2';
  color: #666;
  margin: 0;
  font-size: 1.1rem;
}

.level-btn.active .level-info h3,
.level-btn.active .level-info p {
  color: white;
  text-shadow: 1px 1px 0 rgba(0,0,0,0.2);
}

.start-btn {
  background: linear-gradient(145deg, #F25E86, #F29F05);
  width: 100%;
  padding: 1.2rem;
  border: none;
  border-radius: 15px;
  color: white;
  font-family: 'DNFBitBitv2';
  font-size: 1.4rem;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 4px solid #F2B705;
  box-shadow: 0 6px 0 #F25E86;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.2);
}

.start-btn:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 0 #F25E86;
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
  100% { transform: translateY(0px); }
}

@font-face {
  font-family: 'DNFBitBitv2';
  font-style: normal;
  font-weight: 400;
  src: url('//cdn.df.nexon.com/img/common/font/DNFBitBitv2.otf') format('opentype');
}

@media (max-width: 768px) {
  .quiz-game-container {
    margin: 1rem;
    padding: 1.5rem;
  }

  .intro-header {
    padding: 2rem;
  }

  .intro-header h1 {
    font-size: 2.2rem;
  }

  .level-btn {
    padding: 1rem;
  }

  .level-icon {
    width: 40px;
    height: 40px;
    font-size: 1.5rem;
  }
}
</style> -->

# 차분한 버전
<style scoped>
.quiz-game-container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2.5rem;
  background: #ffffff;
  border-radius: 24px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
}

.intro-header {
  background: linear-gradient(135deg, #6B8CFF, #7D5FFF);
  padding: 2.5rem;
  border-radius: 20px;
  text-align: center;
  margin-bottom: 2.5rem;
  position: relative;
  overflow: hidden;
}

.intro-header::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1));
}

.intro-header h1 {
  font-family: 'DNFBitBitv2';
  font-size: 2.8rem;
  color: white;
  margin: 0 0 1rem 0;
  letter-spacing: 1px;
}

.intro-description {
  font-family: 'DNFBitBitv2';
  font-size: 1.2rem;
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.8;
  margin: 0;
}

.highlight {
  color: #FFC107;
  font-weight: bold;
}

.level-selection {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  margin-bottom: 2.5rem;
}

.level-btn {
  background: #ffffff;
  border: none;
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.level-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(107, 140, 255, 0.15);
}

.level-btn.active {
  background: linear-gradient(135deg, #6B8CFF, #7D5FFF);
  color: white;
}

.level-icon {
  font-size: 2rem;
  margin-right: 1.5rem;
  background: #f8f9ff;
  width: 56px;
  height: 56px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.level-btn.active .level-icon {
  background: rgba(255, 255, 255, 0.2);
  color: white;
}

.level-info {
  flex-grow: 1;
}

.level-info h3 {
  font-family: 'DNFBitBitv2';
  font-size: 1.3rem;
  margin: 0 0 0.4rem 0;
  color: #2D3436;
}

.level-btn.active .level-info h3,
.level-btn.active .level-info p {
  color: white;
}

.level-info p {
  font-family: 'DNFBitBitv2';
  color: #636E72;
  margin: 0;
  font-size: 1rem;
  line-height: 1.4;
}

.start-btn {
  background: linear-gradient(135deg, #FF6B6B, #FF8E8E);
  width: 100%;
  padding: 1.2rem;
  border: none;
  border-radius: 16px;
  color: white;
  font-family: 'DNFBitBitv2';
  font-size: 1.3rem;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.start-btn::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1));
  transition: all 0.3s ease;
}

.start-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(255, 107, 107, 0.25);
}

.start-btn:active {
  transform: translateY(-1px);
}

@font-face {
  font-family: 'DNFBitBitv2';
  font-style: normal;
  font-weight: 400;
  src: url('//cdn.df.nexon.com/img/common/font/DNFBitBitv2.otf') format('opentype');
}

@media (max-width: 768px) {
  .quiz-game-container {
    margin: 1rem;
    padding: 1.5rem;
  }

  .intro-header {
    padding: 2rem;
  }

  .intro-header h1 {
    font-size: 2.2rem;
  }

  .level-btn {
    padding: 1.2rem;
  }

  .level-icon {
    width: 48px;
    height: 48px;
    font-size: 1.8rem;
  }
}
</style>