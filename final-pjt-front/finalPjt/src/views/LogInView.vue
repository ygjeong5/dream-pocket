<template>
  <div class="login-container">
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <div class="form-group">
        <label for="username">아이디:</label>
        <input 
          type="text" 
          id="username" 
          v-model="username" 
          required
          placeholder="아이디를 입력하세요"
        >
      </div>
      <div class="form-group">
        <label for="password">비밀번호:</label>
        <input 
          type="password" 
          id="password" 
          v-model="password" 
          required
          placeholder="비밀번호를 입력하세요"
        >
      </div>
      <button type="submit">로그인</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useEggStore } from '@/stores/egg'

const store = useEggStore()
const username = ref('')
const password = ref('')

const logIn = function () {
  if (!username.value || !password.value) {
    window.alert('아이디와 비밀번호를 모두 입력해주세요.')
    return
  }

  store.logIn({ 
    username: username.value, 
    password: password.value 
  })
  .catch((error) => {
    console.error('로그인 처리 중 오류:', error)
  })
}
</script>

<style scoped>
.login-container {
  max-width: 500px;
  margin: 2rem auto;
  padding: 2rem;
  background: #e8f1f8;
  border-radius: 15px;
  border: 3px solid #2980b9;
  box-shadow: 0 8px 0 #7fb3d5;
}

h1 {
  font-family: 'DNFBitBitv2';
  text-align: center;
  margin-bottom: 2rem;
  color: transparent;
  background: linear-gradient(to left top, #2980b9, #3498db);
  -webkit-background-clip: text;
  -webkit-text-stroke: 2px #1a5f7a;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-family: 'DNFBitBitv2';
  color: #34343f;
}

input {
  width: 100%;
  padding: 0.8rem;
  border: 3px solid #7fb3d5;
  border-radius: 10px;
  background: white;
  font-family: 'Pretendard-Regular';
  box-shadow: 0 4px 0 #85929e;
  transition: all 0.2s ease;
}

input:focus {
  outline: none;
  border-color: #1E90FF;
  box-shadow: 0 4px 0 #145999;
}

button {
  width: 100%;
  padding: 1rem;
  background: linear-gradient(145deg, #2980b9, #3498db);
  border: 3px solid #7fb3d5;
  border-radius: 19px;
  color: white;
  font-family: 'DNFBitBitv2';
  font-size: 1.1rem;
  cursor: pointer;
  box-shadow: 0 4px 0 #1a5f7a;
  transition: all 0.2s ease;
}

button:hover {
  transform: translateY(2px);
  box-shadow: 0 2px 0 #145999;
  background: linear-gradient(145deg, #2980b9, #3498db);
}
</style>