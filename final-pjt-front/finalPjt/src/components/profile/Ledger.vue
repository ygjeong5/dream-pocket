<template>
    <div class="ledger-content">
        <div class="ledger-header">
            <h1>가계부 관리</h1>
            <div class="total-amount">
                <div class="amount-card">
                    <span class="label">현재 잔액</span>
                    <span class="value">{{ totalAmount }}원</span>
                </div>
            </div>
        </div>

        <div class="ledger-grid">
            <!-- 왼쪽: 입력 폼 -->
            <div class="input-section">
                <div class="form-container">
                    <h2>✏️ 새로운 내역 추가</h2>
                    <form @submit.prevent="addLedger" class="ledger-form">
                        <div class="form-group">
                            <label for="date">📅 날짜</label>
                            <input id="date" type="date" v-model="newLedger.date" required />
                        </div>
                        <div class="form-group">
                            <label for="category">📊 분류</label>
                            <div class="category-buttons">
                                <button 
                                    type="button"
                                    :class="['category-btn', newLedger.category === 'income' ? 'active' : '']"
                                    @click="newLedger.category = 'income'"
                                >수입</button>
                                <button 
                                    type="button"
                                    :class="['category-btn', newLedger.category === 'expense' ? 'active' : '']"
                                    @click="newLedger.category = 'expense'"
                                >지출</button>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="amount">💵 금액</label>
                            <input id="amount" type="number" v-model="newLedger.amount" required />
                        </div>
                        <div class="form-group">
                            <label for="description">📝 설명</label>
                            <input id="description" type="text" v-model="newLedger.description" placeholder="내용을 입력하세요" />
                        </div>
                        <button type="submit" class="submit-button">추가하기</button>
                    </form>
                </div>
            </div>

            <!-- 오른쪽: 내역 목록 -->
            <div class="list-section">
                <div class="list-header">
                    <h2>📋 가계부 내역</h2>
                    <div class="filter-container">
                        <select v-model="selectedMonth" @change="filterLedgers" class="month-select">
                            <option value="">전체 기간</option>
                            <option v-for="n in 12" :key="n" :value="String(n).padStart(2, '0')">
                                {{ n }}월
                            </option>
                        </select>
                    </div>
                </div>

                <div class="ledger-list" v-if="filteredLedgers.length">
                    <div v-for="ledger in filteredLedgers" 
                         :key="ledger.id" 
                         class="ledger-item"
                         :class="ledger.category">
                        <div class="ledger-date">{{ formatDate(ledger.date) }}</div>
                        <div class="ledger-info">
                            <span class="category-badge">{{ ledger.category === 'income' ? '수입' : '지출' }}</span>
                            <span class="description">{{ ledger.description }}</span>
                        </div>
                        <div class="ledger-amount">{{ formatAmount(ledger.amount) }}원</div>
                        <button @click="deleteLedger(ledger.id)" class="delete-button">×</button>
                    </div>
                </div>
                <div v-else class="empty-state">
                    등록된 가계부 내역이 없습니다.
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, computed } from 'vue'
import { useEggStore } from "@/stores/egg"

const store = useEggStore()
const ledgers = ref([]) // 전체 가계부 항목
const filteredLedgers = ref([]) // 필터링된 가계부 항목
const newLedger = ref({
    date: '',
    category: 'income',
    amount: '',
    description: '',
})
const userInfo = ref({})
const selectedMonth = ref('') // 선택된 달

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
        filteredLedgers.value = res.data // 초기화 시 모든 항목을 표시
    })
    .catch(err => {
        console.log('Error fetching ledgers:', err)
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
        filteredLedgers.value.push(res.data) // 필터링된 목록에도 추가
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
        url: `http://127.0.0.1:8000/accounts/ledgers/${id}/`,
        headers: {
            Authorization: `Token ${store.token}`,
        },
    })
    .then(() => {
        ledgers.value = ledgers.value.filter(ledger => ledger.id !== id)
        filteredLedgers.value = filteredLedgers.value.filter(ledger => ledger.id !== id) // 필터링된 목록에서 삭제
    })
    .catch(err => {
        console.log('Error deleting ledger:', err)
    })
}

// 필터링된 가계부 항목 업데이트
const filterLedgers = () => {
    if (selectedMonth.value) {
        filteredLedgers.value = ledgers.value.filter(ledger => ledger.date.slice(5, 7) === selectedMonth.value)
    } else {
        filteredLedgers.value = [...ledgers.value] // 전체 항목으로 돌아가기
    }
}

// 총 금액 계산 (수입은 더하고, 지출은 빼는 방식)
const totalAmount = computed(() => {
    return filteredLedgers.value.reduce((sum, ledger) => {
        if (ledger.category === 'income') {
            return sum + parseInt(ledger.amount) // 수입은 더함
        } else if (ledger.category === 'expense') {
            return sum - parseInt(ledger.amount) // 지출은 뺌
        }
        return sum
    }, 0)
})

// 페이지 로드 시 가계부 항목 가져오기
onMounted(() => {
    fetchLedgers()
})

// script에 추가할 함수들
const formatDate = (dateString) => {
    const date = new Date(dateString);
    return `${date.getMonth() + 1}월 ${date.getDate()}일`;
};

const formatAmount = (amount) => {
    return amount.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};
</script>

<style scoped>
.ledger-content {
    max-width: 1400px;
    margin: 2rem auto;
    padding: 2rem;
    font-family: 'DNFBitBitv2';
}

.ledger-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}

.ledger-header h1 {
    font-size: 2.5rem;
    color: #2c3e50;
    margin: 0;
}

.amount-card {
    background: linear-gradient(135deg, #88C9F2, #9CD95F);
    padding: 1.5rem 2rem;
    border-radius: 15px;
    color: white;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.amount-card .label {
    display: block;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
}

.amount-card .value {
    font-size: 1.8rem;
    font-weight: bold;
}

.ledger-grid {
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

.form-container h2 {
    margin: 0 0 1.5rem 0;
    color: #2c3e50;
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

.category-buttons {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
}

.category-btn {
    padding: 0.8rem;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    background: white;
    cursor: pointer;
    transition: all 0.3s ease;
}

.category-btn.active {
    background: #88C9F2;
    color: white;
    border-color: #88C9F2;
}

.submit-button {
    width: 100%;
    padding: 1rem;
    background: #9CD95F;
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.submit-button:hover {
    background: #8bc34a;
}

.list-section {
    background: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.list-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}

.month-select {
    padding: 0.5rem 1rem;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    background: white;
}

.ledger-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.ledger-item {
    display: flex;
    align-items: center;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 10px;
    transition: all 0.3s ease;
}

.ledger-item:hover {
    transform: translateX(5px);
}

.ledger-item.income {
    border-left: 4px solid #9CD95F;
}

.ledger-item.expense {
    border-left: 4px solid #F25E86;
}

.ledger-date {
    width: 100px;
    color: #666;
}

.ledger-info {
    flex: 1;
    display: flex;
    align-items: center;
    gap: 1rem;
}

.category-badge {
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    font-size: 0.9rem;
}

.income .category-badge {
    background: #e8f5e9;
    color: #4caf50;
}

.expense .category-badge {
    background: #fce4ec;
    color: #e91e63;
}

.ledger-amount {
    font-weight: bold;
    margin-right: 1rem;
}

.income .ledger-amount {
    color: #4caf50;
}

.expense .ledger-amount {
    color: #e91e63;
}

.delete-button {
    width: 30px;
    height: 30px;
    border: none;
    border-radius: 50%;
    background: #f8f9fa;
    color: #666;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    transition: all 0.3s ease;
}

.delete-button:hover {
    background: #ff4d4d;
    color: white;
}

.empty-state {
    text-align: center;
    color: #666;
    padding: 3rem;
}

@media (max-width: 1024px) {
    .ledger-grid {
        grid-template-columns: 1fr;
    }
    
    .input-section {
        position: static;
    }
}
</style>