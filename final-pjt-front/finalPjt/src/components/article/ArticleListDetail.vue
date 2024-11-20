<template>
  <div v-if="article" class="article-detail">
    <div class="article-actions">
      <button @click="goBack" class="btn-back">목록으로</button>
      <button @click="goUpdate" class="btn-update">수정</button>
      <button @click="deleteArticle" class="btn-delete">삭제</button>
    </div>
    <h2>{{ article.title }}</h2>
    <p>{{ article.content }}</p>
    <div class="article-info">
      <p>작성자: {{ article.user }}</p>
      <p>작성일: {{ article.created_at }}</p>
    </div>
    
  </div>
  <div v-else>
    <p>게시글을 불러오는 중...</p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useEggStore } from '@/stores/egg'
import { storeToRefs } from 'pinia'

const route = useRoute()
const router = useRouter()
const store = useEggStore()
const { article } = storeToRefs(store)

const getArticleDetail = async () => {
  try {
    const articleId = route.params.id
    await store.getArticleDetail(articleId)
  } catch (error) {
    console.error('게시글 상세 정보 불러오기 실패:', error)
  }
}

const goBack = () => {
  router.push({ name: 'ArticleView' })
}

const goUpdate = () => {
  router.push({
    name: 'ArticleUpdate',
    params: { id: route.params.id }
  })
}

const deleteArticle = async () => {
  try {
    if (confirm('정말로 이 게시글을 삭제하시겠습니까?')) {
      await store.deleteArticle(route.params.id)
      router.push({ name: 'ArticleView' })
    }
  } catch (error) {
    console.error('게시글 삭제 실패:', error)
  }
}

onMounted(() => {
  getArticleDetail()
})
</script>

<style scoped>
.article-detail {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: white;
}
.article-actions {
  display: flex;
  justify-content: space-between;
}
.btn-back, .btn-update, .btn-delete {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
}

</style>
