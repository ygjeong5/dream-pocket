<template>
  <div>
    <h1>상세 정보</h1>
    <p>가입 방법 : {{ productInfo.join_way }}</p>
    <p>가입 대상 : {{ productInfo.join_member }}</p>
    <p>우대 사항 : {{ productInfo.spcl_cnd }}</p>
    
    <ul v-for="option in productOptions" :key="option.id">
      <li>
        <p>기간 : {{ option.save_trm }}</p>
        <p>{{ option.intr_rate_type_nm }}</p>
        <p>최저 : {{ option.intr_rate }}</p>
        <p>최고 : {{ option.intr_rate2 }}</p>
      </li>
    </ul>
    <button @click="close">닫기</button>
  </div>
</template>

<script setup>
import axios from 'axios'
import { useEggStore } from '@/stores/egg'
import { onMounted, ref, watch } from 'vue'

const store = useEggStore()
const props = defineProps({
  productId: Number
})

const productInfo = ref({})
const productOptions = ref({})

const getProductDetail = function () {
  axios({
    method: 'get',
    url:`${store.API_URL}finlife/saving-product/detail/${props.productId}/`,
    headers:{
      Authorization: `Token ${store.token}`
    }
  })
  .then(res => {
    productInfo.value = res.data.product
    productOptions.value = res.data.options
  })
  .catch(err => {
    console.log(err)
  })
}
watch(() => props.productId, getProductDetail)

onMounted(() => {
  getProductDetail()
})

const emit = defineEmits(['close'])

const close = function () {
  emit('close')
}

</script>

<style scoped>

</style>