<template>
  <div>
    <form @submit.prevent="logIn">
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
  import { useEggStore } from '@/stores/egg';

  const store = useEggStore()
  const token = ref(null)

  const username = ref(null)
  const password = ref(null)

  const logIn = function() {
    const payload = {
      username: username.value,
      password: password.value
    }
    store.logIn(payload)
  }
  


 
</script>

<style scoped>

</style>