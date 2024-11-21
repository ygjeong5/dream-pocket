<template>
  <div>
      <ul v-for="product in productsList">
        <li>
          {{ product.kor_co_nm }}
          {{ product.fin_prdt_nm }}
          <div>
            <button @click="goDetail(product.id)">상세</button>
          </div>
        </li>
      </ul>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const props = defineProps({
  productsList:Array
})

const emit = defineEmits(['detail'])

const goDetail = function (productId) {
  emit('detail', productId)
}


</script>

<style scoped>

</style>