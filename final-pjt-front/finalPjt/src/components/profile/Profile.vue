<template>
  <div class="profile-container">
    <div class="profile-card">
      <h2>프로필 정보</h2>
      <div class="profile-info">
        <div class="info-group">
          <label>사용자 이름</label>
          <p>{{ userInfo.username }}</p>
        </div>
        <!-- 필요한 다른 사용자 정보 필드들 추가 -->
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  userInfo: Object
})
</script>

<style scoped>
.profile-container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
}

.profile-card {
  background: #e8f1f8;
  border: 3px solid #2980b9;
  border-radius: 15px;
  padding: 2rem;
  box-shadow: 0 8px 0 #7fb3d5;
}

h2 {
  font-family: 'DNFBitBitv2';
  text-align: center;
  margin-bottom: 2rem;
  color: transparent;
  background: linear-gradient(to left top, #2980b9, #3498db);
  -webkit-background-clip: text;
  -webkit-text-stroke: 2px #1a5f7a;
  border-bottom: 3px solid #7fb3d5;
  padding-bottom: 1rem;
}

.profile-info {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.info-group {
  background: white;
  border: 3px solid #7fb3d5;
  border-radius: 10px;
  padding: 1rem;
  box-shadow: 0 4px 0 #85929e;
}

label {
  display: block;
  font-family: 'DNFBitBitv2';
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}

p {
  font-family: 'Pretendard-Regular';
  color: #2c3e50;
  margin: 0;
  font-size: 1.1rem;
  padding: 0.5rem;
  background: #f8f9fa;
  border-radius: 5px;
}
</style>