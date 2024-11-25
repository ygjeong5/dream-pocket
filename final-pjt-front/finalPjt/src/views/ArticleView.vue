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
.article-container {
  max-width: 1200px;
  min-width: 1000px;
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
  background: #e8f1f8;
  padding: 1.5rem;
  border-radius: 15px;
  box-shadow: 0 4px 0 #7fb3d5;
  border: 3px solid #2980b9;
}

.header-section h1 {
  font-family: 'DNFBitBitv2', sans-serif;
  font-size: 2.5rem;
  margin: 0;
  color: transparent;
  background: linear-gradient(to left top, #1E90FF, #00bfff);
  -webkit-background-clip: text;
  -webkit-text-stroke: 2px #1e90ff;
}

.create-btn {
  background: linear-gradient(145deg, #2980b9, #3498db);
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 19px;
  font-family: 'DNFBitBitv2';
  font-size: 15px;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 0 #1a5f7a;
  border: 3px solid #7fb3d5;
}

.create-btn:hover {
  transform: translateY(2px);
  box-shadow: 0 2px 0 #145999;
}

.category-btn {
  padding: 0.5rem 1rem;
  border: 3px solid #87ceeb;
  border-radius: 19px;
  background: white;
  color: #1E90FF;
  font-family: 'DNFBitBitv2';
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 0 #5a5d68;
}

.category-btn.active {
  background: linear-gradient(145deg, #1E90FF, #1a75cc);
  color: white;
  border-color: transparent;
  box-shadow: 0 4px 0 #145999;
}

.category-btn:hover {
  transform: translateY(2px);
  box-shadow: 0 2px 0 #5a5d68;
}

.article-item {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 3px solid #7fb3d5;
  box-shadow: 0 6px 0 #85929e;
  margin-bottom: 8px;
}

.article-item:hover {
  transform: translateY(2px);
  box-shadow: 0 4px 0 #d0d0d0;
  border-color: #2980b9;
}

.article-content h3 {
  font-family: 'DNFBitBitv2';
  color: #34343f;
  margin: 0.5rem 0;
  font-size: 1.2rem;
}

.category-tag {
  display: inline-block;
  padding: 0.3rem 0.8rem;
  background: linear-gradient(145deg, #e8eaf6, #c5cae9);
  color: #1a237e;
  border-radius: 15px;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
  font-family: 'DNFBitBitv2';
  box-shadow: 0 2px 0 #b2b5cc;
}

.stats-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  font-family: 'DNFBitBitv2';
}

/* 페이지네이션 스타일 수정 */
.page-btn, .page-num-btn {
  border: 3px solid #767c8b;
  border-radius: 19px;
  background: white;
  color: #767c8b;
  font-family: 'DNFBitBitv2';
  padding: 0.5rem 1rem;
  transition: all 0.2s ease;
  box-shadow: 0 4px 0 #5a5d68;
}

.page-btn:hover:not(:disabled), 
.page-num-btn:hover:not(.active) {
  transform: translateY(2px);
  box-shadow: 0 2px 0 #5a5d68;
  background: linear-gradient(145deg, #1E90FF, #1a75cc);
  color: white;
  border-color: transparent;
}

.page-num-btn.active {
  background: linear-gradient(145deg, #1E90FF, #1a75cc);
  color: white;
  border-color: transparent;
  box-shadow: 0 4px 0 #145999;
}

/* 좋아요/댓글 아이콘 스타일 */
.like-info, .comment-info {
  display: flex;
  align-items: center;
  gap: 4px;
  background: #f5f5f5;
  padding: 0.3rem 0.8rem;
  border-radius: 15px;
  box-shadow: 0 2px 0 #e0e0e0;
}

.empty-state {
  text-align: center;
  font-family: 'DNFBitBitv2';
  color: #767c8b;
  padding: 2rem;
  background: #f5f5f5;
  border-radius: 12px;
  box-shadow: 0 4px 0 #e0e0e0;
}
</style>