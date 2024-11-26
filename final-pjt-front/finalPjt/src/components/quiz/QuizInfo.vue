<template>
  <div class="quiz-info-container">
    <h1>퀴즈 정보 게시판</h1>
    <div class="quiz-info-content">금융 용어를 공부한 후 퀴즈를 풀어보세요!</div>
    <div class="post-container">
      <div class="post-header">
        <div class="post-title no-column">No</div>
        <div class="post-title answer-column">정답</div>
        <div class="post-title content-column">내용</div>
      </div>
      <div class="post-list">
        <div class="post" v-for="(quiz, index) in quizInfo" :key="quiz.id">
          <div class="post-item no-column">{{ index + 1 }}</div>
          <div class="post-item answer-column">{{ quiz.title }}</div>
          <div class="post-item content-column">{{ quiz.body }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useEggStore } from '@/stores/egg';

const store = useEggStore();
const quizInfo = ref([]);

const fetchQuizInfo = () => {
  axios({
    method: 'GET',
    url: 'http://localhost:8000/api/v1/quiz_game/quiz-info/',
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      quizInfo.value = res.data;
    })
    .catch((err) => {
      console.error(err);
    });
};

onMounted(() => {
  fetchQuizInfo();
});
</script>

<style scoped>
.quiz-info-container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 2.5rem;
  background: #ffffff;
  border-radius: 24px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
  position: relative;
  font-family: 'DNFBitBitv2';
}

h1 {
  text-align: center;
  color: #2D3436;
  margin-bottom: 2rem;
  font-size: 2.2rem;
  letter-spacing: 1px;
}

.post-container {
  background: #ffffff;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(107, 140, 255, 0.1);
}

.post-header {
  display: flex;
  background: linear-gradient(135deg, #6B8CFF, #7D5FFF);
  color: white;
  padding: 1.2rem 1.5rem;
  font-weight: bold;
  position: relative;
  overflow: hidden;
}

.post-header::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1));
}

.post-title {
  text-align: center;
  font-size: 1.1rem;
  letter-spacing: 1px;
}

.post-list {
  display: flex;
  flex-direction: column;
}

.post {
  display: flex;
  padding: 1.2rem 1.5rem;
  border-bottom: 1px solid rgba(107, 140, 255, 0.1);
  transition: all 0.3s ease;
}

.post:hover {
  background-color: rgba(107, 140, 255, 0.05);
  transform: translateY(-2px);
}

.post-item {
  text-align: center;
  color: #2D3436;
  font-size: 1rem;
  line-height: 1.6;
}

/* 열 너비 조정 */
.no-column {
  flex: 1;
}

.answer-column {
  flex: 1;
}

.content-column {
  flex: 3;
}

@font-face {
  font-family: 'DNFBitBitv2';
  font-style: normal;
  font-weight: 400;
  src: url('//cdn.df.nexon.com/img/common/font/DNFBitBitv2.otf') format('opentype');
}

@media (max-width: 768px) {
  .quiz-info-container {
    margin: 1rem;
    padding: 1.5rem;
  }

  .post {
    padding: 1rem;
  }

  .post-item {
    font-size: 0.9rem;
  }

  h1 {
    font-size: 1.8rem;
  }
}

/* 애니메이션 효과 */
.post {
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

.quiz-info-content {
  text-align: center;
  margin: 2rem auto;
  padding: 1.5rem;
  background: linear-gradient(135deg, rgba(107, 140, 255, 0.1), rgba(125, 95, 255, 0.1));
  border-radius: 16px;
  color: #2D3436;
  font-size: 1.2rem;
  letter-spacing: 1px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(107, 140, 255, 0.1);
  border: 1px solid rgba(107, 140, 255, 0.2);
  animation: softPulse 3s infinite;
}

.quiz-info-content::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1));
}

/* 부드러운 펄스 애니메이션 추가 */
@keyframes softPulse {
  0% {
    transform: scale(1);
    box-shadow: 0 4px 15px rgba(107, 140, 255, 0.1);
  }
  50% {
    transform: scale(1.01);
    box-shadow: 0 6px 20px rgba(107, 140, 255, 0.15);
  }
  100% {
    transform: scale(1);
    box-shadow: 0 4px 15px rgba(107, 140, 255, 0.1);
  }
}

/* 호버 효과 추가 */
.quiz-info-content:hover {
  background: linear-gradient(135deg, rgba(107, 140, 255, 0.15), rgba(125, 95, 255, 0.15));
  transform: translateY(-2px);
  transition: all 0.3s ease;
}

/* 모바일 반응형 추가 */
@media (max-width: 768px) {
  .quiz-info-content {
    font-size: 1rem;
    padding: 1.2rem;
    margin: 1.5rem auto;
  }
}
</style>
