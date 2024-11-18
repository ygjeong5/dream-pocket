<template>
  <div>
    <RouterLink :to="{ name: 'LicenseView'}">회원가입</RouterLink>
    <span> | </span>
    <RouterLink :to="{ name: 'SignUpView'}">회원가입 2</RouterLink>
  </div>
  <RouterView/>
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router';
</script>

<style  scoped>
  
</style>