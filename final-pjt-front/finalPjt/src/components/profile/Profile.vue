<template>
  <div class="profile-container">
    <div class="profile-card">
      <h2>프로필</h2>
      <div class="profile-info">
        <div class="info-group">
          <label>사용자 이름</label>
          <p>{{ userInfo.username }}</p>
        </div>
        <div class="info-group">
          <label>나이</label>
          <p>{{ userInfo.age || '정보 없음' }}</p>
        </div>
        <div class="info-group">
          <label>성별</label>
          <p>{{ genderLabel }}</p>
        </div>
        <div class="info-group">
          <label>목표 금액</label>
          <p>{{ userInfo.goal_amount ? `${userInfo.goal_amount.toLocaleString()} 원` : '설정되지 않음' }}</p>
        </div>
        <div class="info-group">
          <label>포인트</label>
          <p>{{ userInfo.point }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { ref } from 'vue'

const props = defineProps({
  userInfo: Object,
})

const genderLabel = computed(() => {
  const genderMap = { 0: '미지정', 1: '남성', 2: '여성' }
  return genderMap[props.userInfo.gender] || '미지정'
})
</script>

<style scoped>
.profile-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to right, #d3cce3, #e9e4f0);
  padding: 2rem;
}

.profile-card {
  background: white;
  border: 1px solid #ddd;
  border-radius: 15px;
  padding: 2rem 2.5rem;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  width: 100%;
  text-align: center;
}

h2 {
  font-family: 'Pretendard-Bold';
  font-size: 1.8rem;
  color: #34495e;
  margin-bottom: 1.5rem;
}

.profile-info {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.info-group {
  text-align: left;
}

label {
  display: block;
  font-size: 0.9rem;
  color: #7f8c8d;
  margin-bottom: 0.4rem;
  font-family: 'Pretendard-Medium';
}

p {
  font-size: 1rem;
  font-family: 'Pretendard-Regular';
  color: #2c3e50;
  background: #f8f9fa;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 0.8rem;
  margin: 0;
}
</style>
