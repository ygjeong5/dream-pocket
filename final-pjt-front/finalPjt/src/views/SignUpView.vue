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

  const store = useEggStore()

  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  const API_URL = store.API_URL
  
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
  })
  }
 
  

</script>

<style scoped>
    .license-content {
    margin: 50px auto 0;
    padding: 70px 40px;
    padding-bottom: 80px;
    text-align: center;
    width: 800px;
    border: 1px solid #e5e5e5;
    vertical-align: baseline;
  }
  h3 { 
    font-size: 30px;
    padding: 0 0 10px 0;
    border-bottom: 2px solid #000000;
  }
  
</style>