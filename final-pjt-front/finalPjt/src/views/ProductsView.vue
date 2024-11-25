<template>
  <div>
    <h1>금융 상품 리스트</h1>
    <RouterLink :to="{ name:'FinancialProductsView' }">예금 상품</RouterLink> |
    <RouterLink :to="{ name:'SavingProductsView' }">적금 상품</RouterLink> |
    <RouterLink :to="{ name:'ProductComparison'}">상품 비교</RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

</script>

<style scoped>

</style>