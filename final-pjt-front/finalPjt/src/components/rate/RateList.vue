<template>
  <div class="rate-content">
    <div class="rate-header">
      <h1>환율 정보</h1>
    </div>

    <div class="rate-grid">
      <!-- 왼쪽: 환율 변환기 -->
      <div class="input-section">
        <div class="form-container">
          <RateConverter :exchange-list="exchangeList" />
        </div>
      </div>

      <!-- 오른쪽: 환율 정보 목록 -->
      <div class="list-section">
        <div class="list-header">
          <h2>📊 실시간 환율</h2>
        </div>
        <div class="rate-list">
          <div v-for="(item, index) in exchangeList" 
               :key="index"
               class="rate-item">
            <div class="currency-name">{{ item.cur_nm }}</div>
            <div class="rate-value">{{ item.deal_bas_r }}</div>
          </div>
        </div>
      </div>
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
.rate-content {
    max-width: 1400px;
    margin: 2rem auto;
    padding: 2rem;
    font-family: 'DNFBitBitv2';
}

.rate-header {
    margin-bottom: 2rem;
}

.rate-header h1 {
    font-size: 2.5rem;
    color: #2c3e50;
    margin: 0;
}

.rate-grid {
    display: grid;
    grid-template-columns: 350px 1fr;
    gap: 2rem;
}

.input-section {
    position: sticky;
    top: 2rem;
    height: fit-content;
}

.form-container {
    background: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.list-section {
    background: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.list-header {
    margin-bottom: 2rem;
}

.list-header h2 {
    color: #2c3e50;
    font-size: 1.5rem;
    margin: 0;
}

.rate-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.rate-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 10px;
    border-left: 4px solid #88C9F2;
    transition: all 0.3s ease;
}

.rate-item:hover {
    transform: translateX(5px);
}

.currency-name {
    color: #2c3e50;
    font-weight: bold;
}

.rate-value {
    color: #88C9F2;
    font-weight: bold;
}

@media (max-width: 1024px) {
    .rate-grid {
        grid-template-columns: 1fr;
    }
    
    .input-section {
        position: static;
    }
}
</style>