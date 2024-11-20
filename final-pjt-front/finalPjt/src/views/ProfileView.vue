<template>
  <div>
    <h1>회원 정보</h1>
    <RouterLink :to="{ name:'ProfileUpdate' }">
      <button>회원 정보 수정</button>
    </RouterLink>
    <Profile
      :user-info="userInfo"
    />
  </div>
</template>

<script setup>
import Profile from '@/components/profile/Profile.vue'
import { onMounted } from 'vue'
import { useEggStore } from '@/stores/egg'
import { RouterLink, RouterView } from 'vue-router'

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
      console.log(res)
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

</style>