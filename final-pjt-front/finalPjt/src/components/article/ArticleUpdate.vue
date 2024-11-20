<template>
  <div class="article-update">
    <h2>게시글 수정</h2>
    <form @submit.prevent="updateArticle">
      <div class="form-group">
        <label for="title">제목</label>
        <input 
          type="text" 
          id="title" 
          v-model="title" 
          required
        >
      </div>
      <div class="form-group">
        <label for="content">내용</label>
        <textarea 
          id="content" 
          v-model="content" 
          required
        ></textarea>
      </div>
      <div class="form-actions">
        <button type="submit" class="btn-submit">수정</button>
        <button type="button" @click="goBack" class="btn-cancel">취소</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useEggStore } from '@/stores/egg'

const route = useRoute()
const router = useRouter()
const store = useEggStore()

const title = ref('')
const content = ref('')

onMounted(async () => {
  try {
    const article = await store.getArticleDetail(route.params.id)
    title.value = article.title
    content.value = article.content
  } catch (error) {
    console.error('게시글 정보 불러오기 실패:', error)
  }
})

const updateArticle = async () => {
  try {
    await store.updateArticle(route.params.id, {
      title: title.value,
      content: content.value
    })
    router.push({
      name: 'ArticleListDetail',
      params: { id: route.params.id }
    })
  } catch (error) {
    console.error('게시글 수정 실패:', error)
  }
}

const goBack = () => {
  router.go(-1)
}
</script>

<style scoped>
.article-update {
  max-width: 800px;
  margin: 20px auto;
}
.form-group {
  margin-bottom: 15px;
}
.form-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}
.btn-submit, .btn-cancel {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
}
</style>
