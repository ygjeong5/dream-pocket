<template>
  <div class="recommender-content">
    <div class="recommender-header">
      <h1>적금/예금 추천</h1>
    </div>

    <div class="recommender-grid">
      <!-- 왼쪽: 입력 폼 -->
      <div class="input-section">
        <div class="form-container">
          <h2>✏️ 추천 받기</h2>
          <form @submit.prevent="submitForm" class="recommender-form">
            <div class="form-group">
              <label for="age">👤 나이</label>
              <select id="age" v-model="form.age" required>
                <option value="">선택하세요</option>
                <option value="10대">10대</option>
                <option value="20대">20대</option>
                <option value="30대">30대</option>
                <option value="40대">40대</option>
                <option value="50대 이상">50대 이상</option>
              </select>
            </div>

            <div class="form-group">
              <label for="period">⏰ 목표 기간</label>
              <select id="period" v-model="form.period" required>
                <option value="">선택하세요</option>
                <option value="6개월">6개월</option>
                <option value="1년">1년</option>
                <option value="2년">2년</option>
                <option value="3년 이상">3년 이상</option>
              </select>
            </div>

            <div class="form-group">
              <label for="amount">💰 월 저축 가능 금액 (만원)</label>
              <input
                type="number"
                id="amount"
                v-model.number="form.amount"
                placeholder="예: 50"
                required
              />
            </div>

            <div class="form-group">
              <label for="purpose">🎯 목적</label>
              <select id="purpose" v-model="form.purpose" required>
                <option value="">선택하세요</option>
                <option value="비상금">비상금</option>
                <option value="목표 달성">목표 달성</option>
                <option value="단순 저축">단순 저축</option>
                <option value="여행 준비">여행 준비</option>
                <option value="취미 활동">취미 활동</option>
                <option value="학자금 마련">학자금 마련</option>
              </select>
            </div>

            <div class="form-group">
              <label for="preferential_conditions">🎁 우대 조건</label>
              <select id="preferential_conditions" v-model="form.preferential_conditions" required>
                <option value="">선택하세요</option>
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
            </div>

            <button type="submit" class="submit-button">추천받기</button>
          </form>
        </div>
      </div>

      <!-- 오른쪽: 추천 결과 -->
      <div class="list-section">
        <div class="list-header">
          <h2>📋 추천 상품</h2>
        </div>
        <div v-if="response" class="recommendation-content">
          <div v-html="response"></div>
        </div>
        <div v-else class="empty-state">
          추천받을 정보를 입력해주세요.
        </div>
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
.recommender-content {
    max-width: 1400px;
    margin: 2rem auto;
    padding: 2rem;
    font-family: 'DNFBitBitv2';
}

.recommender-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
    margin-bottom: 2rem;
    height: 80px;
}

.recommender-header h1 {
    font-size: 2.5rem;
    color: #2c3e50;
    margin: 0;
}

.recommender-grid {
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

select, input {
    width: 100%;
    padding: 0.8rem;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    background: white;
    font-size: 1rem;
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
    font-family: 'DNFBitBitv2';
    font-size: 1.1rem;
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
    margin-bottom: 2rem;
}

.list-header h2 {
    color: #2c3e50;
    font-size: 1.5rem;
    margin: 0;
}

.recommendation-content {
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 10px;
}

.recommendation-content :deep(h3) {
    color: #2c3e50;
    margin: 1rem 0;
}

.recommendation-content :deep(ul) {
    padding-left: 1.5rem;
    margin: 1rem 0;
}

.recommendation-content :deep(li) {
    margin: 0.5rem 0;
    color: #2c3e50;
}

.empty-state {
    text-align: center;
    color: #666;
    padding: 3rem;
}

@media (max-width: 1024px) {
    .recommender-grid {
        grid-template-columns: 1fr;
    }
    
    .input-section {
        position: static;
    }
}
</style>
