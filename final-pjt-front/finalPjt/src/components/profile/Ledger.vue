<template>
    <div class="ledger-content">
        <h1>가계부 관리</h1>

        <div class="form-container">
            <h2>새로운 항목 추가</h2>
            <form @submit.prevent="addLedger" class="ledger-form">
                <div class="form-group">
                    <label for="date">날짜</label>
                    <input id="date" type="date" v-model="newLedger.date" required />
                </div>
                <div class="form-group">
                    <label for="category">분류</label>
                    <select id="category" v-model="newLedger.category" required>
                        <option value="income">수입</option>
                        <option value="expense">지출</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="amount">금액</label>
                    <input id="amount" type="number" v-model="newLedger.amount" required />
                </div>
                <div class="form-group">
                    <label for="description">설명</label>
                    <input id="description" type="text" v-model="newLedger.description" placeholder="내용을 입력하세요" />
                </div>
                <button type="submit" class="submit-button">추가</button>
            </form>
        </div>

        <div v-if="ledgers.length" class="table-container">
            <h2>가계부 항목</h2>
            <table>
                <thead>
                    <tr>
                        <th>날짜</th>
                        <th>분류</th>
                        <th>금액</th>
                        <th>설명</th>
                        <th>관리</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="ledger in ledgers" :key="ledger.id">
                        <td>{{ ledger.date }}</td>
                        <td>{{ ledger.category === 'income' ? '수입' : '지출' }}</td>
                        <td>{{ ledger.amount }}원</td>
                        <td>{{ ledger.description }}</td>
                        <td>
                            <button @click="deleteLedger(ledger.id)" class="delete-button">삭제</button>
                        </td>
                    </tr>
                </tbody>
            </table>
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
const userInfo = ref({})
// 가계부 항목 가져오기
const fetchLedgers = () => {
    axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/ledgers/',
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
    axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/user-info/',
        headers: {
            Authorization: `Token ${store.token}`,
        },
    })
    .then(res => {
        userInfo.value = res.data
    })
    .catch(err => {
        console.log(err)
    })
}

// 가계부 항목 추가하기
const addLedger = () => {
    axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/ledgers/',
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
    axios({
        method: 'put',
        url: 'http://127.0.0.1:8000/accounts/user-info/',
        headers: {
            Authorization: `Token ${store.token}`,
        },
        data: {
            point: userInfo.value.point + 10,
        },
    })
}

// 가계부 항목 삭제하기
const deleteLedger = (id) => {
    axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/accounts/ledgers/${id}/`,
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
.ledger-content {
    max-width: 1136px; /* 너비를 늘림 */
    margin: 2rem auto;
    padding: 2rem;
    background: #e8f1f8;
    border-radius: 15px;
    box-shadow: 0 8px 0 #7fb3d5;
    border: 3px solid #2980b9;
}

h1 {
    text-align: center;
    color: #2980b9;
}

h2 {
    text-align: center;
    color: #2980b9;
}

.form-container {
    margin-bottom: 2rem;
}

.ledger-form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.form-group {
    display: flex;
    flex-direction: column;
}

label {
    margin-bottom: 0.5rem;
    color: #2c3e50;
}

input, select {
    padding: 0.8rem;
    border: 3px solid #7fb3d5;
    border-radius: 10px;
    background: white;
    transition: all 0.2s ease;
}

input[type="submit"], .submit-button {
    background: linear-gradient(145deg, #2980b9, #3498db);
    border: 3px solid #7fb3d5;
    border-radius: 19px;
    color: white;
    font-size: 1.1rem;
    cursor: pointer;
    box-shadow: 0 4px 0 #1a5f7a;
    margin-top: 1rem;
}

input[type="submit"]:hover, .submit-button:hover {
    transform: translateY(2px);
    box-shadow: 0 2px 0 #1a5f7a;
    background: linear-gradient(145deg, #3498db, #2980b9);
}

input:focus {
    outline: none;
    border-color: #2980b9;
    box-shadow: 0 4px 0 #1a5f7a;
}

.table-container {
    margin-top: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    border: 1px solid #ccc;
    padding: 10px;
    text-align: center;
}

th {
    background-color: #f8f9fa;
}

.delete-button {
    cursor: pointer;
    color: white;
    background-color: #ff6666; /* 더 진한 파스텔 톤 색상 */
    border: none;
    padding: 10px 15px; /* 크기를 화면 비율에 맞춰 조정 */
    border-radius: 4px;
    font-size: 1rem; /* 폰트 크기 조정 */
    width: 100%; /* 버튼이 셀의 너비에 맞게 조정 */
}

.delete-button:hover {
    background-color: #ff4d4d; /* hover 시 색상 */
}
</style>