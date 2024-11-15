<script setup>
import { RouterLink, RouterView } from 'vue-router'
import SearchView from '@/views/SearchView.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const goBack = function () {
  router.go(-1)
}

</script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink> |
    <RouterLink :to="{name:'search'}">Search</RouterLink> |
    <RouterLink :to="{name:'saved'}">Saved List</RouterLink>
  </nav>

  <button @click="goBack"><-- 뒤로 가기</button>

  <RouterView />
</template>

<style scoped>

</style>
