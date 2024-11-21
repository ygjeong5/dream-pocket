<template>
  <div>
    <div v-if="detailId !== 0">
      <FinancialProductDetail 
        :product-id="detailId"
        @close="close"
      />
    </div>
    <h1>금융상품 리스트</h1>
    <FinancialProductList 
      :products-list="productsList"
      @detail="handleDetail"
    />
  </div>
</template>

<script setup>
import FinancialProductList from '@/components/financialproduct/FinancialProductList.vue'
import FinancialProductDetail from '@/components/financialproduct/FinancialProductDetail.vue'
import { useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'
import { useEggStore } from '@/stores/egg'
import axios from 'axios'

const store = useEggStore()
const router = useRouter()
const productsList = ref([])
const detailId = ref(0)

const getProductList = function () {
  axios({
    method: 'get',
    url: `${store.API_URL}finlife/financial-products-list/`,
    headers:{
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      productsList.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
}

onMounted(() => {
  getProductList()
})

const handleDetail = (productId) => {
  detailId.value = productId
}

const close = () => {
  detailId.value = 0
}

</script>

<style scoped>

</style>