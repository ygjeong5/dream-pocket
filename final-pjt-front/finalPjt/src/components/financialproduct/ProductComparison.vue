<template>
    <div>
        <FinancialProductComparison
        v-for="finProduct in financialList"
        :key = finProduct.id
        :fin-product="finProduct"
        />
        <SavingProductComparison
        v-for="saveProduct in savingList"
        :key = saveProduct.id
        :save-product="saveProduct"
        />
    </div>
</template>

<script setup>
import { useEggStore } from '@/stores/egg'
import FinancialProductComparison from './FinancialProductComparison.vue'
import SavingProductComparison from './SavingProductComparison.vue'

const store = useEggStore()

const financialList = store.financialCartList
const savingList = store.savingCartList

</script>

<style scoped>

</style>