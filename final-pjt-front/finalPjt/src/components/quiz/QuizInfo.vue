<template>
  <div class="quiz-info-container">
    <h1>퀴즈 정보 게시판</h1>
    <div class="post-container">
      <div class="post-header">
        <div class="post-title no-column">No</div>
        <div class="post-title answer-column">정답</div>
        <div class="post-title content-column">내용</div>
      </div>
      <slot>

        <div class="post-list">
          <div class="post" v-for="(quiz, index) in quizInfo" :key="quiz.id">
            <div class="post-item no-column">{{ index + 1 }}</div>
            <div class="post-item answer-column">{{ quiz.title }}</div>
            <div class="post-item content-column">{{ quiz.body }}</div>
          </div>
        </div>
      </slot>
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
  max-width: 1200px; /* 너비를 조정 */
  margin: 2rem auto;
  padding: 2rem;
  background: #f9f9f9; /* 배경색을 게시판 스타일에 맞게 설정 */
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  color: #2980b9;
  margin-bottom: 1.5rem;
}

.post-container {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}

.post-header {
  display: flex;
  background-color: #2980b9;
  color: white;
  padding: 10px;
  font-weight: bold;
}

.post-title {
  text-align: center;
}

.post-list {
  display: flex;
  flex-direction: column;
}

.post {
  display: flex;
  padding: 10px;
  border-bottom: 1px solid #ddd;
  transition: background-color 0.2s;
}

.post:hover {
  background-color: #f1f1f1; /* hover 시 배경색 변경 */
}

.post-item {
  text-align: center;
}

/* 열 너비 조정 */
.no-column {
  flex: 1; /* No 열의 너비 */
}

.answer-column {
  flex: 1; /* 정답 열의 너비 */
}

.content-column {
  flex: 2; /* 내용 열의 너비 */
}
</style>
