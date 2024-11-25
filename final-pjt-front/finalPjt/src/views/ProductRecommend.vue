<template>
  <div class="container">
    <div class="recommender-section">
      <div class="savings-recommender">
        <h2>적금/예금 추천받기</h2>

        <form @submit.prevent="submitForm">
          <label for="age">나이:</label>
          <select id="age" v-model="form.age" required>
            <option value="">선택</option>
            <option value="10대">10대</option>
            <option value="20대">20대</option>
            <option value="30대">30대</option>
            <option value="40대">40대</option>
            <option value="50대 이상">50대 이상</option>
          </select>

          <label for="period">목표 기간:</label>
          <select id="period" v-model="form.period" required>
            <option value="">선택</option>
            <option value="6개월">6개월</option>
            <option value="1년">1년</option>
            <option value="2년">2년</option>
            <option value="3년 이상">3년 이상</option>
          </select>

          <label for="amount">월 저축 가능 금액 (만원):</label>
          <input
            type="number"
            id="amount"
            v-model.number="form.amount"
            placeholder="예: 50"
            required
          />

          <label for="purpose">목적:</label>
          <select id="purpose" v-model="form.purpose" required>
            <option value="">선택</option>
            <option value="비상금">비상금</option>
            <option value="목표 달성">목표 달성</option>
            <option value="단순 저축">단순 저축</option>
            <option value="여행 준비">여행 준비</option>
            <option value="취미 활동">취미 활동</option>
            <option value="학자금 마련">학자금 마련</option>
          </select>

          <label for="preferential_conditions">우대 조건:</label>
          <select id="preferential_conditions" v-model="form.preferential_conditions" required>
            <option value="">선택</option>
            <option value="카드사용">카드사용</option>
            <option value="미션달성">미션달성</option>
            <option value="공과금연동">공과금연동</option>
            <option value="급여연동">급여연동</option>
            <option value="비대면가입">비대면가입</option>
            <option value="주택청약">주택청약</option>
            <option value="첫거래">첫거래</option>
            <option value="예적금가입">예적금가입</option>
            <option value="재예치">재예치</option>
            <option value="입출금통장">입출금통장</option>
            <option value="추천">추천</option>
            <option value="은행앱사용">은행앱사용</option>
            <option value="마케팅/기타동의">마케팅/기타동의</option>
            <option value="적금금액자동이체">적금금액자동이체</option>
            <option value="기타">기타</option>
          </select>

          <button type="submit">추천받기</button>
        </form>
      </div>

      <div v-if="response" class="recommendations">
        <h3>추천 상품</h3>
        <div v-html="response"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useEggStore } from '@/stores/egg'
import { marked } from 'marked'

const store = useEggStore()
const API_URL = store.API_URL

const form = ref({
  age: "",
  period: "",
  amount: null,
  purpose: "",
  preferential_conditions: "",
})

const response = ref("")

const submitForm = async () => {
  try {
    const { data } = await axios.post(
      `${API_URL}chatbot/recommend/`,
      { message: form.value },
      { 
        headers: { 
          Authorization: `Token ${store.token}`
        }
      }
    )
    response.value = marked(data.response)
  } catch (error) {
    console.error("API 요청 실패:", error.response?.data || error.message)
    response.value = "추천을 가져오는 데 실패했습니다."
  }
}
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.recommender-section {
  display: flex;
  gap: 30px;
  flex-wrap: wrap;
}

.savings-recommender {
  flex: 1;
  min-width: 300px;
  font-family: Arial, sans-serif;
}

.recommendations {
  flex: 1;
  min-width: 300px;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 4px;
  margin-top: 0;
}

/* 화면 너비가 768px 이하일 때 */
@media (max-width: 768px) {
  .recommender-section {
    flex-direction: column;
  }

  .savings-recommender,
  .recommendations {
    width: 100%;
  }

  .recommendations {
    margin-top: 30px;
  }
}

form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

label {
  font-weight: bold;
  color: #333;
}

input,
select,
button {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

select {
  cursor: pointer;
}

button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 12px;
  cursor: pointer;
  font-weight: bold;
  margin-top: 10px;
}

button:hover {
  background-color: #0056b3;
}

.recommendations h3 {
  color: #333;
  margin-bottom: 15px;
}

.recommendations :deep(h3) {
  margin: 1.5em 0 0.5em;
  color: #2c3e50;
}

.recommendations :deep(ul),
.recommendations :deep(ol) {
  padding-left: 20px;
  margin: 0.5em 0;
}

.recommendations :deep(li) {
  margin: 0.3em 0;
}

.recommendations :deep(p) {
  margin: 0.8em 0;
  line-height: 1.6;
}
</style>
