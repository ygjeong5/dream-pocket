<template>
  <div>
    <h3 class="page-title">환율 변환기</h3>
    <div>
      <label for="country">나라 선택:</label>
      <select v-model="selectedCurrency" id="country">
        <option 
          v-for="currency in exchangeList" 
          :key="currency.cur_unit" 
          :value="currency"
        >
          {{ currency.cur_nm }} ({{ currency.cur_unit }})
        </option>
      </select>
    </div>

    <div>
      <label for="amount">환전할 금액:</label>
      <input 
        type="number" 
        id="amount" 
        v-model.number="inputAmount" 
        placeholder="금액을 입력하세요"
        min="0"
      />
    </div>

    <div>
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
.page-title {
  color: #2c3e50;
  margin-bottom: 30px;
  text-align: center;
}

label {
  margin-right: 8px;
}

select, input {
  margin-bottom: 16px;
  display: block;
}

h4 {
  margin-top: 16px;
  color: #333;
}
</style>