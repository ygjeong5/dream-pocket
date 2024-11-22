<template>
  <div>
    <ul>
      <li v-for="product in productsList" :key="product.fin_prdt_cd">
        <div>
          <p>{{ product.kor_co_nm }} - {{ product.fin_prdt_nm }}</p>
          <button @click="goDetail(product.id)">상세</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
const props = defineProps({
  productsList: Array,
})

const emit = defineEmits(["detail"])

const goDetail = (productId) => {
  emit("detail", productId)
}
</script>

<style scoped>
/* 스타일은 기존과 동일 */
</style>
