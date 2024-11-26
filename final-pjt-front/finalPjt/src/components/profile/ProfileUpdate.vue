<template>
  <div class="edit-profile-container">
    <div class="edit-profile-card">
      <h2>프로필 수정</h2>
      <form @submit.prevent="submitForm">
        <div class="input-group">
          <label for="username">사용자 이름</label>
          <input
            type="text"
            id="username"
            v-model="formData.username"
            placeholder="사용자 이름을 입력하세요"
            required
          />
        </div>
        <div class="input-group">
          <label for="age">나이</label>
          <input
            type="number"
            id="age"
            v-model="formData.age"
            placeholder="나이를 입력하세요"
            required
          />
        </div>
        <div class="input-group">
          <label for="gender">성별</label>
          <select id="gender" v-model="formData.gender">
            <option value="0">미지정</option>
            <option value="1">남성</option>
            <option value="2">여성</option>
          </select>
        </div>
        <div class="input-group">
          <label for="goal_amount">목표 금액</label>
          <input
            type="number"
            id="goal_amount"
            v-model="formData.goal_amount"
            placeholder="목표 금액을 입력하세요"
          />
        </div>
        <button type="submit" class="submit-btn">저장</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useEggStore } from '@/stores/egg'
import { useRouter } from 'vue-router'

const store = useEggStore()
const router = useRouter()

// 수정할 데이터 바인딩
const formData = ref({
  username: '',
  age: '',
  gender: 0,
  goal_amount: ''
})

// 폼 제출 처리
const submitForm = () => {
  axios({
    method: 'put',
    url: `${store.API_URL}accounts/user-info/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: formData.value
  })
    .then(() => {
      console.log('수정된 데이터:', formData.value)
      alert('프로필이 업데이트되었습니다.')
      router.push({ name: 'ProfileView' })
    })
    .catch(err => {
      console.log(err)
    })
}

// 사용자 정보 가져오기
const userProfile = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}accounts/user-info/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      console.log(res)
      // 받아온 사용자 정보를 formData에 반영
      formData.value = {
        username: res.data.username || '',
        age: res.data.age || '',
        gender: res.data.gender || 0,
        goal_amount: res.data.goal_amount || ''
      }
    })
    .catch(err => {
      console.log(err)
    })
}

onMounted(() => {
  userProfile()
})
</script>

<style scoped>
.edit-profile-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to right, #f7f8f9, #e9eff1);
  padding: 2rem;
}

.edit-profile-card {
  background: white;
  border: 1px solid #ddd;
  border-radius: 15px;
  padding: 2rem 2.5rem;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  width: 100%;
  text-align: center;
}

h2 {
  font-family: 'Pretendard-Bold';
  font-size: 1.8rem;
  color: #34495e;
  margin-bottom: 1.5rem;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  margin-bottom: 1.5rem;
}

label {
  font-size: 0.9rem;
  color: #7f8c8d;
  font-family: 'Pretendard-Medium';
}

input,
select {
  padding: 0.8rem;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-top: 0.5rem;
  outline: none;
}

input:focus,
select:focus {
  border-color: #2980b9;
}

button.submit-btn {
  background-color: #3498db;
  color: white;
  font-size: 1rem;
  border: none;
  padding: 1rem 2rem;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button.submit-btn:hover {
  background-color: #2980b9;
}
</style>
