<template>
  <div class="article-container">
    <div class="header-section">
      <h1>게시판</h1>
      <div class="category-buttons">
        <button 
          v-for="category in categories" 
          :key="category.value"
          :class="['category-btn', { active: currentCategory === category.value }]"
          @click="filterByCategory(category.value)"
        >
          {{ category.name }}
        </button>
      </div>
      <RouterLink v-if="store.token" :to="{ name: 'ArticleCreate' }">
        <button class="create-btn">게시글 작성</button>
      </RouterLink>
      <RouterLink v-else :to="{ name: 'LogInView' }">
        <button class="create-btn">로그인하고 글쓰기</button>
      </RouterLink>
    </div>

    <div v-if="filteredArticles.length > 0" class="article-list">
      <div 
        v-for="article in paginatedArticles" 
        :key="article.id"
        class="article-item"
        @click="goToDetail(article.id)"
      >
        <div class="article-content">
          <span class="category-tag">{{ getCategoryName(article.category) }}</span>
          <h3>{{ article.title }}</h3>
          <div class="article-meta">
            <span class="author">{{ article.user.username }}</span>
            <div class="stats-info">
              <div class="like-info">
                <span class="heart-icon">❤️</span>
                <span class="like-count">{{ article.like_count || 0 }}</span>
              </div>
              <div class="comment-info">
                <span class="comment-icon">💬</span>
                <span class="comment-count">{{ article.comments?.length || 0 }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 페이지네이션 -->
      <div v-if="totalPages > 1" class="pagination">
        <button 
          :disabled="currentPage === 1"
          @click="currentPage--"
          class="page-btn"
        >
          이전
        </button>

        <!-- 페이지 숫자 버튼 -->
        <div class="page-numbers">
          <button 
            v-for="pageNum in displayedPages" 
            :key="pageNum"
            :class="['page-num-btn', { active: currentPage === pageNum }]"
            @click="currentPage = pageNum"
          >
            {{ pageNum }}
          </button>
        </div>

        <button 
          :disabled="currentPage === totalPages"
          @click="currentPage++"
          class="page-btn"
        >
          다음
        </button>
      </div>
    </div>
    <div v-else class="empty-state">
      <p>아직 작성된 게시글이 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { useEggStore } from '@/stores/egg'
import { onMounted, ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const store = useEggStore()
const router = useRouter()
const currentPage = ref(1)
const itemsPerPage = 10

const categories = [
  { name: '전체', value: 'all' },
  { name: '자유게시판', value: 'free' },
  { name: '금융지식 나누기', value: 'knowledge' },
  { name: '상품 추천', value: 'recommendation' },
  { name: '공지사항', value: 'notice' }
]

const currentCategory = ref('all')

const filteredArticles = computed(() => {
  if (!store.articles) return []
  return currentCategory.value === 'all' 
    ? store.articles 
    : store.articles.filter(article => article.category === currentCategory.value)
})

// 페이지네이션 관련 computed 속성
const totalPages = computed(() => {
  return Math.ceil(filteredArticles.value.length / itemsPerPage)
})

const paginatedArticles = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return filteredArticles.value.slice(start, end)
})

// 페이지 번호 표시 로직
const maxDisplayPages = 5
const displayedPages = computed(() => {
  if (totalPages.value <= maxDisplayPages) {
    return Array.from({ length: totalPages.value }, (_, i) => i + 1)
  }

  let start = currentPage.value - Math.floor(maxDisplayPages / 2)
  let end = currentPage.value + Math.floor(maxDisplayPages / 2)

  if (start < 1) {
    start = 1
    end = maxDisplayPages
  }

  if (end > totalPages.value) {
    end = totalPages.value
    start = totalPages.value - maxDisplayPages + 1
  }

  return Array.from(
    { length: end - start + 1 },
    (_, i) => start + i
  )
})

const filterByCategory = (category) => {
  currentCategory.value = category
  currentPage.value = 1  // 카테고리 변경시 첫 페이지로 이동
}

const getCategoryName = (categoryValue) => {
  const category = categories.find(cat => cat.value === categoryValue)
  return category ? category.name : '기타'
}

const goToDetail = (articleId) => {
  router.push({
    name: 'ArticleListDetail',
    params: { id: articleId }
  })
}

// onMounted 수정
onMounted(async () => {
  try {
    await store.getArticles()
  } catch (error) {
    console.error('게시글 로딩 실패:', error)
  }
})
</script>

<style scoped>
.article-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 0.5rem;
  color: #666;
  font-size: 0.9rem;
}

.author {
  font-weight: 500;
}

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
  flex-wrap: wrap;
  gap: 1rem;
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

.category-buttons {
  display: flex;
  gap: 1rem;
  margin: 0 2rem;
}

.category-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #1a237e;
  border-radius: 20px;
  background: white;
  color: #1a237e;
  cursor: pointer;
  transition: all 0.2s ease;
}

.category-btn.active {
  background: #1a237e;
  color: white;
}

.category-btn:hover {
  background: #1a237e15;
}

.category-tag {
  display: inline-block;
  padding: 0.3rem 0.8rem;
  background: #e8eaf6;
  color: #1a237e;
  border-radius: 15px;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.stats-info {
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
  min-width: 70px;  /* 버튼 너비 통일 */
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
  display: none;  /* 페이지 정보 숨김 */
}

.page-numbers {
  display: flex;
  gap: 0.5rem;
}

.page-num-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #1a237e;
  border-radius: 4px;
  background: white;
  color: #1a237e;
  cursor: pointer;
  transition: all 0.2s ease;
  min-width: 40px;
}

.page-num-btn:hover {
  background: #1a237e15;
}

.page-num-btn.active {
  background: #1a237e;
  color: white;
  cursor: default;
}

</style>