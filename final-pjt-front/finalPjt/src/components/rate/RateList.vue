<template>
  <div>
    <RateConverter :exchange-list="exchangeList" />
    <h2>환율 정보</h2>
    <div>
      <pre>
        {{ exchangeList }}
      </pre>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useEggStore } from '@/stores/egg'
import { onMounted } from 'vue'
import RateConverter from '@/components/rate/RateConverter.vue'

const store = useEggStore()

const exchangeList = ref([])

const getExchangRate = function () {
  axios({
    mathod: 'get',
    url: `${store.API_URL}finlife/rate/`,
    headers:{
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      exchangeList.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
}

onMounted(() => {
  getExchangRate()
})
</script>

<style scoped>

</style>