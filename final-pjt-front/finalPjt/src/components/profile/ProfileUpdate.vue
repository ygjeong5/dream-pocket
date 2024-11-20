<template>
  <div>
    <h1>회원 정보 수정</h1>
    <form @submit.prevent="updateProfile">
      <div>
        <label for="name">이름</label>
        <input
          id="name"
          v-model="formData.name"
          type="text"
          placeholder="이름을 입력하세요"
        />
      </div>

      <div>
        <label for="email">이메일</label>
        <input
          id="email"
          v-model="formData.email"
          type="email"
          placeholder="이메일을 입력하세요"
        />
      </div>

      <div>
        <label for="password">비밀번호</label>
        <input
          id="password"
          v-model="formData.password"
          type="password"
          placeholder="새 비밀번호를 입력하세요"
        />
      </div>

      <button type="submit">수정 완료</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useEggStore } from '@/stores/egg'
import axios from 'axios'
import { useRouter } from 'vue-router'

const store = useEggStore()
const router = useRouter()

// 추가적으로 수정 가능하게 만들 데이터 삽입 필요
const formData = ref({
  name: '',
  email: '',
  password: ''
})

const fetchUserProfile = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}accounts/user-info/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      // 가져온 user정보 초기 값으로 설정
      formData.value.name = res.data.username
      formData.value.email = res.data.useremail
    })
    .catch(err => {
      console.error(err)
      alert('회원 정보를 불러오는 데 실패했습니다.')
    })
}

// 사용자 정보 업데이트
const updateProfile = () => {
  axios({
    method: 'put',
    url: `${store.API_URL}accounts/user-info/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: formData.value
  })
    .then(res => {
      alert('회원 정보가 수정되었습니다.')
      router.push({ name: 'ProfileView' }) 
      // 수정 완료 후 프로필 페이지로 이동
    })
    .catch(err => {
      console.error(err)
      alert('회원 정보 수정에 실패했습니다.')
    })
}

onMounted(() => {
  fetchUserProfile()
})
</script>

<style scoped>

</style>
