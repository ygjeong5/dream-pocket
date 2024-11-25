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

</style>