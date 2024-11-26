<template>
  <div class="rate-converter">
    <h3 class="page-title">환율 변환기</h3>
    <div class="form-group">
      <label for="country" class="form-label">나라 선택:</label>
      <select v-model="selectedCurrency" id="country" class="form-select">
        <option 
          v-for="currency in exchangeList" 
          :key="currency.cur_unit" 
          :value="currency"
        >
          {{ currency.cur_nm }} ({{ currency.cur_unit }})
        </option>
      </select>
    </div>

    <div class="form-group">
      <label for="amount" class="form-label">환전할 금액:</label>
      <input 
        type="number" 
        id="amount" 
        v-model.number="inputAmount" 
        class="form-input"
        placeholder="금액을 입력하세요"
        min="0"
      />
    </div>

    <div class="result">
      <h4>환전 결과:</h4>
      <p v-if="selectedCurrency">
        {{ inputAmount }} 원 ➡️ {{ convertedAmount }} {{ selectedCurrency.cur_unit }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

// 부모로부터 전달받는 props
const props = defineProps({
  exchangeList: Array
})

// 선택한 통화와 입력된 금액
const selectedCurrency = ref(null)
const inputAmount = ref(0)

// 환전된 금액 계산
const convertedAmount = computed(() => {
  if (!selectedCurrency.value) return 0
  const rate = parseFloat(selectedCurrency.value.deal_bas_r.replace(/,/g, ''))
  return (inputAmount.value * (1 / rate)).toFixed(2)
})

// 디폴트 통화 선택
watch(
  () => props.exchangeList,
  (newVal) => {
    if (Array.isArray(newVal) && newVal.length > 0) {
      selectedCurrency.value = newVal[0]
    }
  },
  { immediate: true }
)
</script>

<style scoped>
.rate-converter {
  max-width: 500px;
  margin: 0 auto;
  padding: 30px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.page-title {
  text-align: center;
  font-size: 24px;
  color: #333;
  margin-bottom: 20px;
  font-family: 'Pretendard', sans-serif;
}

.form-group {
  margin-bottom: 20px;
}

.form-label {
  font-size: 16px;
  color: #333;
  margin-bottom: 8px;
  display: inline-block;
  font-family: 'Pretendard', sans-serif;
}

.form-select,
.form-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 16px;
  font-family: 'Pretendard', sans-serif;
  background-color: #fff;
}

.form-select:focus,
.form-input:focus {
  border-color: #1e90ff;
  outline: none;
}

.result h4 {
  font-size: 18px;
  color: #333;
  margin-bottom: 10px;
  font-family: 'Pretendard', sans-serif;
}

.result p {
  font-size: 18px;
  font-weight: bold;
  color: #333;
  background-color: #f1f8ff;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #87ceeb;
  text-align: center;
}
</style>
