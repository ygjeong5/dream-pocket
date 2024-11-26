<template>
  <div class="edit-profile-container">
    <div class="edit-profile-card">
      <h2>✏️ 프로필 수정</h2>
      <form @submit.prevent="submitForm">
        <div class="input-group">
          <label>🏷️ 사용자 이름</label>
          <input
            type="text"
            v-model="formData.username"
            placeholder="사용자 이름을 입력하세요"
            required
          />
        </div>
        <div class="input-group">
          <label>🎂 나이</label>
          <input
            type="number"
            v-model="formData.age"
            placeholder="나이를 입력하세요"
            required
          />
        </div>
        <div class="input-group">
          <label>👥 성별</label>
          <select v-model="formData.gender">
            <option value="0">미지정</option>
            <option value="1">남성</option>
            <option value="2">여성</option>
          </select>
        </div>
        <div class="input-group">
          <label>🎯 목표 금액</label>
          <input
            type="number"
            v-model="formData.goal_amount"
            placeholder="목표 금액을 입력하세요"
          />
        </div>
        <button type="submit" class="submit-btn">저장하기</button>
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

const formData = ref({
  username: '',
  age: '',
  gender: 0,
  goal_amount: ''
})

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
      alert('프로필이 업데이트되었습니다.')
      router.push({ name: 'ProfileView' })
    })
    .catch(err => {
      console.log(err)
    })
}

const userProfile = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}accounts/user-info/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
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
    max-width: 1400px;
    margin: 2rem auto;
    padding: 2rem;
    font-family: 'DNFBitBitv2';
    display: flex;
    justify-content: center;
    align-items: flex-start;
    min-height: calc(100vh - 4rem);
    background: #f5f7fa;
}

.edit-profile-card {
    background: white;
    padding: 2.5rem;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 600px;
}

h2 {
    font-size: 2rem;
    color: #2c3e50;
    margin-bottom: 2rem;
    text-align: center;
}

form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.input-group {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 15px;
    border-left: 4px solid #88C9F2;
    transition: all 0.3s ease;
}

.input-group:hover {
    transform: translateX(5px);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    color: #666;
    font-size: 0.9rem;
    margin-bottom: 0.8rem;
}

input, select {
    width: 100%;
    padding: 0.8rem;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    font-size: 1rem;
    transition: all 0.3s ease;
    background: white;
}

input:focus, select:focus {
    border-color: #88C9F2;
    outline: none;
    box-shadow: 0 0 0 2px rgba(136, 201, 242, 0.1);
}

button.submit-btn {
    width: 100%;
    padding: 1rem;
    background: #9CD95F;
    color: white;
    border: none;
    border-radius: 10px;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-top: 1rem;
}

button.submit-btn:hover {
    background: #8bc34a;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* 반응형 디자인 */
@media (max-width: 768px) {
    .edit-profile-container {
        padding: 1rem;
    }

    .edit-profile-card {
        padding: 1.5rem;
    }

    h2 {
        font-size: 1.8rem;
    }
}
</style>
