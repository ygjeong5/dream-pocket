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
.article-item {
  padding: 15px;
  margin: 10px 0;
  border: 1px solid #ddd;
  border-radius: 8px;
  cursor: pointer;
}

.article-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.like-info {
  display: flex;
  align-items: center;
  gap: 4px;
}

.heart-icon {
  font-size: 1em;
  color: #ff4444;
}

.like-count {
  font-size: 0.9em;
  color: #666;
}

.article-footer {
  display: flex;
  justify-content: space-between;
  color: #666;
  font-size: 0.9em;
  margin-top: 10px;
}

.article-stats {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.comment-info {
  display: flex;
  align-items: center;
  gap: 4px;
}

.comment-icon {
  font-size: 1em;
  color: #666;
}

.comment-count {
  font-size: 0.9em;
  color: #666;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 2rem;
  gap: 1rem;
}

.page-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #1a237e;
  border-radius: 4px;
  background: white;
  color: #1a237e;
  cursor: pointer;
  transition: all 0.2s ease;
}

.page-btn:disabled {
  border-color: #ccc;
  color: #ccc;
  cursor: not-allowed;
}

.page-btn:not(:disabled):hover {
  background: #1a237e;
  color: white;
}

.page-info {
  font-size: 0.9rem;
  color: #666;
}
</style>