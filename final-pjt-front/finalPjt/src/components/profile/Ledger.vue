<template>
    <div>
        <h1>가계부 관리</h1>

        <div>
            <h2>새로운 항목 추가</h2>
            <form @submit.prevent="addLedger">
                <div>
                    <label>날짜:</label>
                    <input type="date" v-model="newLedger.date" required />
                </div>
                <div>
                    <label>분류:</label>
                    <select v-model="newLedger.category" required>
                        <option value="income">수입</option>
                        <option value="expense">지출</option>
                    </select>
                </div>
                <div>
                    <label>금액:</label>
                    <input type="number" v-model="newLedger.amount" required />
                </div>
                <div>
                    <label>설명:</label>
                    <input type="text" v-model="newLedger.description" />
                </div>
                <button type="submit">추가</button>
            </form>
        </div>

        <div v-if="ledgers.length">
            <h2>가계부 항목</h2>
            <ul>
                <li v-for="ledger in ledgers" :key="ledger.id">
                    <p>
                        {{ ledger.date }} | 
                        {{ ledger.category === 'income' ? '수입' : '지출' }} | 
                        {{ ledger.amount }}원 | 
                        {{ ledger.description }}
                    </p>
                    <button @click="deleteLedger(ledger.id)">삭제</button>
                </li>
            </ul>
        </div>
        <div v-else>
            <p>등록된 가계부 항목이 없습니다.</p>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useEggStore } from "@/stores/egg"

const store = useEggStore()
const ledgers = ref([])
const newLedger = ref({
    date: '',
    category: 'income',
    amount: '',
    description: '',
})

// 가계부 항목 가져오기
const fetchLedgers = () => {
    axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accouts/ledgers/',
        headers: {
            Authorization: `Token ${store.token}`,
        },
    })
    .then(res => {
        ledgers.value = res.data
    })
    .catch(err => {
        console.log('Error fetching ledgers:', err)
    })
}

// 가계부 항목 추가하기
const addLedger = () => {
    axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accouts/ledgers/',
        headers: {
            Authorization: `Token ${store.token}`,
        },
        data: newLedger.value,
    })
    .then(res => {
        ledgers.value.push(res.data)
        newLedger.value = {
            date: '',
            category: 'income',
            amount: '',
            description: '',
        }
    })
    .catch(err => {
        console.log('Error adding ledger:', err)
    })
}

// 가계부 항목 삭제하기
const deleteLedger = (id) => {
    axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/accouts/ledgers/${id}/`,
        headers: {
            Authorization: `Token ${store.token}`,
        },
    })
    .then(() => {
        ledgers.value = ledgers.value.filter(ledger => ledger.id !== id)
    })
    .catch(err => {
        console.log('Error deleting ledger:', err)
    })
}

// 페이지 로드 시 가계부 항목 가져오기
onMounted(() => {
    fetchLedgers()
})
</script>

<style scoped>
/* 필요에 따라 스타일 추가 */
button {
    margin-left: 10px;
    cursor: pointer;
}
</style>
