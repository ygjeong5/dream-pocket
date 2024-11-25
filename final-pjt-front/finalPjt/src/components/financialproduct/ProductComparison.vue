<template>
    <div>
        <FinancialProductComparison
        v-for="finProduct in financialList"
        :key = finProduct
        :fin-product="finProduct"
        />
        <SavingProductComparison
        v-for="saveProduct in savingList"
        :key = saveProduct
        :save-product="saveProduct"
        />
    </div>
</template>

<script setup>
import { useEggStore } from '@/stores/egg'
import { watch, ref } from 'vue'
import FinancialProductComparison from './FinancialProductComparison.vue'
import SavingProductComparison from './SavingProductComparison.vue'

const store = useEggStore()

const financialList = ref(store.financialCartList)
const savingList = ref(store.savingCartList)

watch(
  () => store.financialCartList, // 추적할 데이터
  (newVal) => {
    financialList.value = [...newVal] // 새 값으로 갱신
  }
)

watch(
  () => store.savingCartList, // 추적할 데이터
  (newVal) => {
    savingList.value = [...newVal] // 새 값으로 갱신
  }
)

</script>

<style scoped>

</style>