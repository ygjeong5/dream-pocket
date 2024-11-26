<template>
  <div class="converter-container">
    <h2>💱 환율 변환기</h2>
    <div class="form-group">
      <label>🌏 나라 선택</label>
      <select v-model="selectedCurrency" class="form-select">
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
      <label>💵 환전할 금액 (KRW)</label>
      <input 
        type="number" 
        v-model.number="inputAmount" 
        class="form-input"
        placeholder="금액을 입력하세요"
        min="0"
      />
    </div>

    <div class="result-card" v-if="selectedCurrency">
      <div class="result-label">환전 결과</div>
      <div class="result-value">
        {{ inputAmount.toLocaleString() }} KRW
        <div class="arrow">➡️</div>
        {{ convertedAmount }} {{ selectedCurrency.cur_unit }}
      </div>
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
.converter-container {
    color: #2c3e50;
}

.converter-container h2 {
    margin: 0 0 1.5rem 0;
    font-size: 1.5rem;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    color: #2c3e50;
}

.form-select,
.form-input {
    width: 100%;
    padding: 0.8rem;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    background: white;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.form-select:focus,
.form-input:focus {
    border-color: #88C9F2;
    outline: none;
}

.result-card {
    background: linear-gradient(135deg, #88C9F2, #9CD95F);
    padding: 1.5rem;
    border-radius: 15px;
    color: white;
    margin-top: 1.5rem;
}

.result-label {
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
}

.result-value {
    font-size: 1.2rem;
    font-weight: bold;
}

.arrow {
    margin: 0.5rem 0;
    font-size: 1.5rem;
}
</style>
