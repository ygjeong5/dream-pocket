<template>
  <div class="rate-convert-container ">
    <RateList />
  </div>
</template>

<script setup>
import RateConverter from '@/components/rate/RateConverter.vue'
import RateList from '@/components/rate/RateList.vue'
</script>

<style scoped>
.rate-convert-container {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

</style>