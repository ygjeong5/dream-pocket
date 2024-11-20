<template>
  <div>
    <h1>ArticleCreate</h1>
    <form>
      <div>
        <label for="title">제목 : </label>
        <input v-model="formData.title" type="text" />
      </div>
      <div>
        <label for="content">내용 :</label>
        <textarea v-model="formData.content"></textarea>
      </div>
      <button @click.prevent="createArticle">작성완료</button>
      <RouterLink :to="{ name: 'ArticleView' }">
        <button>취소</button>
      </RouterLink>
    </form>
  </div>

</template>

<script setup>
import { useEggStore } from '@/stores/egg'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { ref } from 'vue'
import { defineProps } from 'vue'

const store = useEggStore()
const router = useRouter()

const formData = ref({
  title: '',
  content: '',
})

defineProps({
  article: Object
})

const createArticle = () => {

  axios({
    method: 'post',
    url: `${store.API_URL}articles/`,
    data: formData.value,
    headers: {
      Authorization: `Token b1515d11967ba47d1e295572da7cf4b0e5b7c2c7`
    }
  })
    .then((res) => {
      console.log('게시글이 생성되었습니다.')
      router.push({ name: 'ArticleView' })
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>