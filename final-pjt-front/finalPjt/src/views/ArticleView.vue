<template>
  <div class="article-container">
    <div class="header-section">
      <h1>Article Page</h1>
      <RouterLink :to="{ name: 'ArticleCreate' }">
        <button class="create-btn">게시글 작성</button>
      </RouterLink>
    </div>


    <div v-if="store.articles && store.articles.length > 0" class="article-list">
      <div 
        v-for="article in store.articles" 
        :key="article.id"
        class="article-item"
        @click="goToDetail(article.id)"
      >
        <div class="article-content">
          <h3>{{ article.title }}</h3>
          <p>{{ article.content }}</p>
          <span class="like-info"></span>
          <span class="heart-icon">❤️</span>
          <span class="like-count">{{ article.like_count || 0 }}</span>
        </div>
      </div>
    </div>
    <div v-else class="empty-state">
        <i class="fas fa-newspaper"></i>
        <p>아직 작성된 게시글이 없습니다.</p>
        <p class="sub-text">첫 게시글의 주인공이 되어보세요!</p>
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
  // console.log('현재 게시글 목록:', store.articles)
})

const getArticles = async () => {
  try {
    await store.getArticles()
    // console.log('불러온 게시글:', store.articles)
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
.article-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.header-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.header-section h1 {
  color: #1a237e;
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0;
}

.header-section a {
  text-decoration-line: none;
}

.create-btn {
  background: linear-gradient(135deg, #1a237e, #0d47a1);
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
  display: flex;
  align-items: center;
  gap: 8px;
}

.create-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(26, 35, 126, 0.2);
}

.article-list {
  display: grid;
  gap: 1.5rem;
}


.article-item {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.article-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
  border-color: #1a237e;
}

.article-content h3 {
  color: #1a237e;
  margin: 0 0 0.5rem 0;
  font-size: 1.25rem;
}


</style>