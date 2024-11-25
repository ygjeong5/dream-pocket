<template>
    <div>
        <button @click="handleDelete">삭제</button>
        <h1>{{ productInfo.fin_prdt_nm  }}</h1>
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
    </div>
</template>

<script setup>
import { useEggStore } from '@/stores/egg'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const store = useEggStore()
const productInfo = ref({})
const productOptions = ref({})

const props = defineProps({
    finProduct : Number
})

const getProductInfo = function () {
    axios({
    method: 'get',
    url:`${store.API_URL}finlife/financial-product/detail/${props.finProduct}/`,
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

const handleDelete = function () {
    store.financialListDelete(props.finProduct)
    getProductInfo()
}

onMounted(() => {
    getProductInfo()    
})

</script>

<style scoped>

</style>