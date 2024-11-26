<template>
  <div class="article-container">
    <div class="header-section">
      <div class="header-left">
        <h1>게시판</h1>
      </div>
      <div class="header-right">
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
  background: linear-gradient(145deg, #e8f1f8, #d4e6f1);
  border: 3px solid #2980b9;
  border-radius: 15px;
  padding: 1.5rem 2rem;
  box-shadow: 0 6px 0 #85929e;
  margin-bottom: 2rem;
}

.header-left {
  flex: 1;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header-section h1 {
  font-family: 'DNFBitBitv2';
  font-size: 2.5rem;
  background: linear-gradient(to left top, #2980b9, #3498db);
  -webkit-background-clip: text;
  -webkit-text-stroke: 2px rgba(39, 54, 154, 0.726);
  color: transparent;
  animation: titleFloat 3s ease-in-out infinite;
}

@keyframes titleFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.category-buttons {
  display: flex;
  gap: 0.5rem;
  margin: 1rem 0;
  flex-wrap: wrap;
}

.category-btn {
  background: white;
  border: 3px solid #7fb3d5;
  color: #2980b9;
  border-radius: 19px;
  padding: 8px 16px;
  font-family: 'DNFBitBitv2';
  font-size: 14px;
  box-shadow: 0 4px 0 #85929e;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

.category-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent,
    rgba(255, 255, 255, 0.3),
    transparent
  );
  transition: 0.5s;
}

.category-btn:hover::before {
  left: 100%;
}

.category-btn:hover, .category-btn.active {
  background: linear-gradient(145deg, #2980b9, #3498db);
  color: white;
  transform: translateY(2px);
  box-shadow: 0 2px 0 #85929e;
}

.article-item {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 1.5rem;
  align-items: center;
  background: white;
  border: 3px solid #7fb3d5;
  border-radius: 15px;
  padding: 1.2rem 2rem;
  margin-bottom: 1rem;
  box-shadow: 0 6px 0 #85929e;
  transition: all 0.3s ease;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.article-item::after {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.8) 0%, transparent 50%);
  opacity: 0;
  transition: 0.5s;
  transform: scale(0.5);
}

.article-item:hover::after {
  opacity: 0.3;
  transform: scale(1);
}

.article-item:hover {
  transform: translateY(2px);
  box-shadow: 0 4px 0 #85929e;
  border-color: #2980b9;
}

.category-tag {
  background: linear-gradient(145deg, #2980b9, #3498db);
  color: white;
  padding: 5px 12px;
  border-radius: 12px;
  font-family: 'DNFBitBitv2';
  font-size: 0.9rem;
  box-shadow: 0 2px 0 #85929e;
  animation: tagPulse 2s infinite;
}

@keyframes tagPulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

.create-btn {
  background: linear-gradient(145deg, #2980b9, #3498db);
  color: white;
  border: 3px solid #7fb3d5;
  padding: 0.8rem 1.5rem;
  border-radius: 19px;
  font-family: 'DNFBitBitv2';
  font-size: 15px;
  cursor: pointer;
  box-shadow: 0 4px 0 #1a5f7a;
  position: relative;
  overflow: hidden;
  transition: all 0.2s ease;
}

.create-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent,
    rgba(255, 255, 255, 0.4),
    transparent
  );
  transition: 0.5s;
}

.create-btn:hover::before {
  left: 100%;
}

.create-btn:hover {
  transform: translateY(2px);
  box-shadow: 0 2px 0 #145999;
}

.empty-state {
  text-align: center;
  font-family: 'DNFBitBitv2';
  color: #767c8b;
  padding: 3rem;
  background: linear-gradient(145deg, #f5f7fa, #e3e6ed);
  border-radius: 15px;
  box-shadow: 0 6px 0 #d1d4db;
  animation: emptyStateFloat 3s ease-in-out infinite;
}

@keyframes emptyStateFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.article-content {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.article-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.stats-info {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  margin-top: 2rem;
  padding: 1rem;
}

.page-numbers {
  display: flex;
  gap: 0.5rem;
}
</style>