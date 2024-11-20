<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{ name: 'ArticleCreate' }">
      <button>게시글 작성</button>
    </RouterLink>
    <div v-if="store.articles && store.articles.length > 0" class="article-list">
      <div 
        v-for="article in store.articles" 
        :key="article.id"
        class="article-item"
        @click="goToDetail(article.id)"
      >
        <h3>{{ article.title }}</h3>
        <p>{{ article.content }}</p>
      </div>
    </div>
    <div v-else>
      <p>작성된 게시글이 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { useEggStore } from '@/stores/egg'
import { onMounted, watchEffect } from 'vue'
import { useRouter } from 'vue-router'

const store = useEggStore()
const router = useRouter()

// store의 articles 변화를 감지
watchEffect(() => {
  console.log('현재 게시글 목록:', store.articles)
})

const getArticles = async () => {
  try {
    await store.getArticles()
    console.log('불러온 게시글:', store.articles)
  } catch (error) {
    console.error('게시글 불러오기 실패:', error)
  }
}

const goToDetail = (articleId) => {
  router.push({
    name: 'ArticleListDetail',
    params: { id: articleId }
  })
}

onMounted(() => {
  getArticles()
})
</script>

<style scoped>
.article-list {
  margin: 20px;
}

.article-item {
  margin: 10px 0;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.2s;
}



</style>