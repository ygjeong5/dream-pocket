<template>
  <div class="rate-container">
    <div class="rate-header">
      <h2>환율 정보</h2>
    </div>
    <RateConverter :exchange-list="exchangeList" />
    <div class="exchange-info">
      <pre>{{ exchangeList }}</pre>
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
.rate-container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 2rem;
}

.rate-header {
  text-align: center;
  margin-bottom: 2rem;
}

.rate-header h2 {
  font-family: 'DNFBitBitv2';
  color: transparent;
  background: linear-gradient(to left top, #1E90FF, #00bfff);
  -webkit-background-clip: text;
  -webkit-text-stroke: 2px #1e90ff;
  margin-bottom: 1rem;
}

.exchange-info {
  background: white;
  border: 3px solid #87ceeb;
  border-radius: 15px;
  padding: 1.5rem;
  box-shadow: 0 4px 0 #add8e6;
  margin-top: 2rem;
  font-family: 'Pretendard-Regular';
}

pre {
  white-space: pre-wrap;
  word-wrap: break-word;
  color: #34343f;
}
</style>