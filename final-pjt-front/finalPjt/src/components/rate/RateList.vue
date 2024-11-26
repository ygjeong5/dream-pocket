<template>
  <div class="rate-container">
    <div class="rate-header">
      <h2>환율 정보</h2>
    </div>
    <RateConverter :exchange-list="exchangeList" />
    <div class="exchange-info">
      <table>
        <thead>
          <tr>
            <th>통화명</th>
            <th>환율</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in exchangeList" :key="index">
            <td>{{ item.cur_nm }}</td>
            <td>{{ item.deal_bas_r }}</td>
          </tr>
        </tbody>
      </table>
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
      exchangeList.value = res.data.map((item) => ({
        cur_nm: item.cur_nm, // 통화명
        deal_bas_r: item.deal_bas_r, // 환율 기준값
        cur_unit: item.cur_unit // 통화 단위
      }))
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
  max-width: 1136px; /* 너비를 App.vue와 동일하게 설정 */
  margin: 2rem auto;
  padding: 2rem;
  background: #e8f1f8; /* 배경색을 App.vue와 유사하게 설정 */
  border-radius: 15px;
  box-shadow: 0 8px 0 #7fb3d5;
  border: 3px solid #2980b9;
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

h1 {
  text-align: center;
  color: #2980b9;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  border: 1px solid #ccc;
  padding: 10px;
  text-align: center;
}

th {
  background-color: #f8f9fa;
  color: #2980b9; /* 제목 색상 설정 */
}
</style>