<template>
  <div>
    <h2>ArticleList</h2>
    <div v-if="props.articles && props.articles.length > 0">
      <div 
        v-for="article in paginatedArticles"
        :key="article.id"
        class="article-item"
        @click="goToDetail(article.id)"
      >
        <div class="article-header">
          <h3>{{ article.title }}</h3>
          <div class="article-stats">
            <span class="like-info">
              <span class="heart-icon">❤️</span>
              <span class="like-count">{{ article.like_count || 0 }}</span>
            </span>
            <span class="comment-info">
              <span class="comment-icon">💬</span>
              <span class="comment-count">{{ article.comments?.length || 0 }}</span>
            </span>
          </div>
        </div>
        <p>{{ article.content }}</p>
        <div class="article-footer">
          <span>작성자: {{ article.user.username }}</span>
          <span>{{ formatDate(article.created_at) }}</span>
        </div>
      </div>
      
      <!-- 페이지네이션 -->
      <div class="pagination">
        <button 
          :disabled="currentPage === 1"
          @click="currentPage--"
          class="page-btn"
        >
          이전
        </button>
        <span class="page-info">{{ currentPage }} / {{ totalPages }}</span>
        <button 
          :disabled="currentPage === totalPages"
          @click="currentPage++"
          class="page-btn"
        >
          다음
        </button>
      </div>
    </div>
    <div v-else>
      <p>작성된 게시글이 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useEggStore } from '@/stores/egg'
import { storeToRefs } from 'pinia'
import { onMounted, ref, computed } from 'vue'

const store = useEggStore()
const { articles } = storeToRefs(store)
const router = useRouter()
const currentPage = ref(1)
const itemsPerPage = 10

const props = defineProps({
  articles: {
    type: Array,
    required: true
  }
})

const totalPages = computed(() => {
  return Math.ceil(props.articles.length / itemsPerPage)
})

const paginatedArticles = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return props.articles.slice(start, end)
})

const goToDetail = (articleId) => {
  router.push({
    name: 'ArticleListDetail',
    params: { id: articleId }
  })
}

onMounted(async () => {
  await store.getArticles()
})
</script>

<style scoped>
.article-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.header-section {
  background: white;
  padding: 1.5rem 2rem;
  border: 2px solid #7fb3d5;
  border-radius: 12px;
  box-shadow: 0 4px 0 #85929e;
  margin-bottom: 2rem;
}

.category-buttons {
  display: flex;
  gap: 0.8rem;
  margin: 1rem 0;
  flex-wrap: wrap;
}

.category-btn {
  background: white;
  border: 2px solid #7fb3d5;
  color: #2980b9;
  border-radius: 12px;
  padding: 8px 0;
  font-family: 'DNFBitBitv2';
  font-size: 14px;
  width: 120px;
  text-align: center;
  box-shadow: 0 2px 0 #85929e;
  transition: all 0.2s ease;
}

.category-btn:hover, .category-btn.active {
  background: #2980b9;
  color: white;
  transform: translateY(1px);
  box-shadow: 0 1px 0 #85929e;
}

.category-btn::before {
  display: none;
}

.article-item {
  background: white;
  padding: 1.2rem 1.5rem;
  margin-bottom: 1rem;
  border: 2px solid #7fb3d5;
  border-radius: 12px;
  box-shadow: 0 3px 0 #85929e;
}

.article-content {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

h2 {
  font-family: 'Pretendard-Regular';
  font-size: 1.8rem;
  color: #2980b9;
  margin-bottom: 1.5rem;
}

.article-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.9rem;
  color: #666;
}

.stats-info {
  display: flex;
  gap: 1rem;
}

.like-info, .comment-info {
  display: flex;
  align-items: center;
  gap: 0.3rem;
}

.heart-icon {
  color: #ff4444;
  animation: heartBeat 3s infinite;  /* 애니메이션 주기 증가 */
}

@keyframes heartBeat {
  0% { transform: scale(1); }
  50% { transform: scale(1.03); }  /* 크기 변화 감소 */
  100% { transform: scale(1); }
}

.category-tag {
  background: #2980b9;
  color: white;
  padding: 4px 10px;
  border-radius: 8px;
  font-family: 'Pretendard-Regular';
  font-size: 0.85rem;
  display: inline-block;
  margin-bottom: 0.3rem;
}

.pagination {
  margin-top: 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
}

.page-btn {
  padding: 0.5rem 1rem;
  border: 2px solid #7fb3d5;
  border-radius: 8px;
  background: white;
  color: #2980b9;
  font-size: 0.9rem;
  min-width: 70px;
  box-shadow: 0 2px 0 #85929e;
}

.page-numbers {
  display: flex;
  gap: 0.3rem;
}

.page-num-btn {
  padding: 0.5rem 0.8rem;
  border: 2px solid #7fb3d5;
  border-radius: 8px;
  background: white;
  color: #2980b9;
  font-size: 0.9rem;
}

.page-num-btn.active {
  background: #2980b9;
  color: white;
}
</style>