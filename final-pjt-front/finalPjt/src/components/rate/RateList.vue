<template>
  <div>
    <h2>환율 정보</h2>
    {{ excahngList }}
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useEggStore } from '@/stores/egg'
import { onMounted } from 'vue'

const store = useEggStore()

const excahngList = ref([])

const getExchangRate = function () {
  axios({
    mathod: 'get',
    url: `${store.API_URL}finlife/rate/`,
    headers:{
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      excahngList.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
}

onMounted(() => {
  getExchangRate()
})
</script>

<style scoped>

</style>