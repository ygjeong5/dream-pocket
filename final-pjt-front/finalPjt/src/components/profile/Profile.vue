<template>
  <div class="profile-container">
    <div class="profile-card">
      <h2>프로필</h2>
      <div class="profile-info">
        <div class="info-group">
          <label>🏷️ 사용자 이름</label>
          <p>{{ userInfo.username }}</p>
        </div>
        <div class="info-group">
          <label>🎂 나이</label>
          <p>{{ userInfo.age || '정보 없음' }}</p>
        </div>
        <div class="info-group">
          <label>👥 성별</label>
          <p>{{ genderLabel }}</p>
        </div>
        <div class="info-group">
          <label>🎯 목표 금액</label>
          <p>{{ userInfo.goal_amount ? `${userInfo.goal_amount.toLocaleString()} 원` : '설정되지 않음' }}</p>
        </div>
        <div class="info-group">
          <label>💰 포인트</label>
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
    max-width: 1400px;
    margin: 2rem auto;
    padding: 2rem;
    font-family: 'DNFBitBitv2';
    display: flex;
    justify-content: center;
    align-items: flex-start;
    min-height: calc(100vh - 4rem);
    background: #f5f7fa;
}

.profile-card {
    background: white;
    padding: 2.5rem;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 600px;
}

h2 {
    font-size: 2rem;
    color: #2c3e50;
    margin-bottom: 2rem;
    text-align: center;
}

.profile-info {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.info-group {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 15px;
    border-left: 4px solid #88C9F2;
    transition: all 0.3s ease;
}

.info-group:hover {
    transform: translateX(5px);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    color: #666;
    font-size: 0.9rem;
    margin-bottom: 0.8rem;
}

p {
    font-size: 1.1rem;
    color: #2c3e50;
    margin: 0;
    font-weight: 500;
    padding: 0.5rem;
    background: white;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
}

/* 반응형 디자인 */
@media (max-width: 768px) {
    .profile-container {
        padding: 1rem;
    }

    .profile-card {
        padding: 1.5rem;
    }

    h2 {
        font-size: 1.8rem;
    }
}
</style>
