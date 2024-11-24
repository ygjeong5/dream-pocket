<template>
  <div>
    <ul>
      <li v-for="product in productsList" :key="product.fin_prdt_cd">
        <div>
          <p>{{ product.kor_co_nm }} - {{ product.fin_prdt_nm }}</p>
          <button @click="goDetail(product.id)">상세</button>
          <p>
            <button @click="store.savingCart(product.id)">적금 상품 비교</button>
          </p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useEggStore } from '@/stores/egg'

const store = useEggStore()
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