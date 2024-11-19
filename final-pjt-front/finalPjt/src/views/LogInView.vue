<template>
  <div>
    <form @submit.prevent="singUp">
      <label for="username">username :</label>
      <input type="text" id="username" v-model.trim="username"><br>

      <label for="password">password : </label>
      <input type="password" id="password" v-model.trim="password"><br>

      <input type="submit" value="login">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  import { useEggStore } from '@/stores/egg';

  const store = useEggStore()
  const token = ref(null)

  const username = ref(null)
  const password = ref(null)

  const API_URL = store.API_URL
  
  const singUp = function() {

  axios({
    method: 'post',
    url: `${API_URL}accounts/login/`,
    data: {
      username: username.value,
      password: password.value,
    }
  }) 
  .then((res)=> {
    token.value = res.data.key
    console.log('로그인 완료')
    console.log(token.value)
  })
  }
</script>

<style scoped>

</style>