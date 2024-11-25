<template>
  <div class="license-content">
  <h3>회원가입</h3>
  <form @submit.prevent="singUp">
    <label for="username">username :</label>
    <input type="text" id="username" v-model.trim="username"><br>

    <label for="password1">password1 : </label>
    <input type="password" id="password1" v-model.trim="password1"><br>

    <label for="password2">password2 : </label>
    <input type="password" id="password2" v-model.trim="password2"><br>

    <input type="submit" value="SignUp">
  </form>
  
  
  </div>
</template>
  
<script setup> 
  import { ref } from 'vue';
  import axios from 'axios';
  import { useEggStore } from '@/stores/egg';
import router from '@/router';

  const store = useEggStore()

  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  const API_URL = store.API_URL
  

  // 회원가입 (유저 정보 생성)
  const singUp = function() {

  axios({
    method: 'post',
    url: `${API_URL}accounts/signup/`,
    data: {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
    }
  }) 
  .then((res)=> {
    console.log('회원가입 완료')
    const password = password1.value
    // 자동 로그인 기능 
    store.logIn({ username: username.value, password})
    
  })
  }
 
  

</script>

<style scoped>
.license-content {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background: #e8f1f8;
  border-radius: 15px;
  box-shadow: 0 8px 0 #7fb3d5;
  border: 3px solid #2980b9;
}

h3 {
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

form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  max-width: 400px;
  margin: 0 auto;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-family: 'DNFBitBitv2';
  color: #2c3e50;
  text-align: left;
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

input[type="submit"] {
  background: linear-gradient(145deg, #2980b9, #3498db);
  border: 3px solid #7fb3d5;
  border-radius: 19px;
  color: white;
  font-family: 'DNFBitBitv2';
  font-size: 1.1rem;
  cursor: pointer;
  box-shadow: 0 4px 0 #1a5f7a;
  margin-top: 1rem;
}

input[type="submit"]:hover {
  transform: translateY(2px);
  box-shadow: 0 2px 0 #1a5f7a;
  background: linear-gradient(145deg, #3498db, #2980b9);
}

input:focus {
  outline: none;
  border-color: #2980b9;
  box-shadow: 0 4px 0 #1a5f7a;
}
</style>