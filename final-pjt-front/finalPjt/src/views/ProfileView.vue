<template>
  <div class="profile-view">
    <div class="profile-header">
      <h1>회원 정보</h1>
      <RouterLink :to="{ name:'ProfileUpdate' }">
        <button class="edit-button">✏️ 회원 정보 수정</button>
      </RouterLink>
    </div>
    <Profile :user-info="userInfo" />
  </div>
</template>

<script setup>
import Profile from '@/components/profile/Profile.vue'
import { onMounted } from 'vue'
import { useEggStore } from '@/stores/egg'
import { RouterLink } from 'vue-router'
import axios from 'axios'
import { ref } from 'vue'

const store = useEggStore()
const userInfo = ref({})

const userProfile = function () {
  axios({
    method: 'get',
    url:`${store.API_URL}accounts/user-info/`,
    headers:{
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      userInfo.value = res.data
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
.profile-view {
    max-width: 1400px;
    margin: 2rem auto;
    padding: 2rem;
    font-family: 'DNFBitBitv2';
}

.profile-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}

.profile-header h1 {
    font-size: 2.5rem;
    color: #2c3e50;
    margin: 0;
}

.edit-button {
    padding: 0.8rem 1.5rem;
    background: linear-gradient(135deg, #88C9F2, #9CD95F);
    color: white;
    border: none;
    border-radius: 10px;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    font-family: 'DNFBitBitv2';
}

.edit-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

@media (max-width: 768px) {
    .profile-view {
        padding: 1rem;
    }

    .profile-header {
        flex-direction: column;
        gap: 1rem;
        text-align: center;
    }

    .profile-header h1 {
        font-size: 2rem;
    }

    .edit-button {
        width: 100%;
    }
}
</style>