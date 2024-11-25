<template>
  <div v-if="article" class="article-detail">
    <div class="article-actions">
      <button @click="goBack">목록으로</button>
      <div v-if="isArticleAuthor">
        <button @click="goUpdate">수정</button>
        <button @click="deleteArticle">삭제</button>
      </div>
    </div>

    <div class="article-header">
      <div class="title-category">
        <span class="category-tag">{{ getCategoryName(article.category) }}</span>
        <h2>{{ article.title }}</h2>
      </div>
      <div class="like-section">
        <button 
          v-if="store.token"
          @click="toggleLike" 
          class="like-button"
          :class="{ 'liked': article.is_liked }"
        >
          {{ article.is_liked ? '❤️' : '🤍' }}
          <span>{{ article.like_count || 0 }}</span>
        </button>
        <div v-else class="like-count-only">
          ❤️ {{ article.like_count || 0 }}
        </div>
      </div>
    </div>

    <div class="article-content">
      <p>{{ article.content }}</p>
    </div>

    <div class="article-info">
      <p>작성자: {{ article.user.username }}</p>
      <p>작성일: {{ formatDate(article.created_at) }}</p>
    </div>

    <div class="comments-section">
      <div v-if="store.token">
        <ArticleComment 
          :article="article" 
          :comments="article.comments"
          @comment-added="refreshArticle" 
        />
      </div>
      <div v-else>
        <div class="comments-list">
          <div v-if="article.comments?.length > 0">
            <div 
              v-for="comment in article.comments" 
              :key="comment.id"
              class="comment-item"
            >
              <div class="comment-header">
                <span class="comment-author">{{ comment.user.username }}</span>
                <span class="comment-date">{{ formatDate(comment.created_at) }}</span>
              </div>
              <p class="comment-content">{{ comment.content }}</p>
            </div>
          </div>
          <p v-else>아직 댓글이 없습니다.</p>
        </div>
        <p class="login-message">
          댓글을 작성하려면 <RouterLink to="/login">로그인</RouterLink>이 필요합니다.
        </p>
      </div>
    </div>
  </div>
  <div v-else class="loading">
    <p>게시글을 불러오는 중...</p>
  </div>
</template>

<script setup>
import { onMounted, computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useEggStore } from '@/stores/egg'
import { storeToRefs } from 'pinia'
import ArticleComment from './ArticleComment.vue'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const store = useEggStore()
const { article } = storeToRefs(store)

const currentUsername = ref(null)

const getCurrentUser = async () => {
  if (!store.token) return
  
  try {
    const response = await axios({
      method: 'get',
      url: `${store.API_URL}accounts/user/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    currentUsername.value = response.data.username
    console.log('현재 사용자:', currentUsername.value)
  } catch (error) {
    console.error('사용자 정보 가져오기 실패:', error)
  }
}

const isArticleAuthor = computed(() => {
  return article.value?.user?.username === currentUsername.value
})

const getArticleDetail = async () => {
  try {
    await store.getArticleDetail(route.params.id)
  } catch (error) {
    console.error('게시글 상세 정보 불러오기 실패:', error)
  }
}

const refreshArticle = async () => {
  await getArticleDetail()
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

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ko-KR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const toggleLike = async () => {
  try {
    await axios({
      method: 'post',
      url: `${store.API_URL}articles/${route.params.id}/like/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    await getArticleDetail()  // 게시글 정보 새로고침
  } catch (error) {
    console.error('좋아요 토글 실패:', error)
  }
}

const categories = [
  { name: '자유게시판', value: 'free' },
  { name: '금융지식 나누기', value: 'knowledge' },
  { name: '상품 추천', value: 'recommendation' },
  { name: '공지사항', value: 'notice' }
]

const getCategoryName = (categoryValue) => {
  const category = categories.find(cat => cat.value === categoryValue)
  return category ? category.name : '기타'
}

onMounted(async () => {
  await getCurrentUser()
  await getArticleDetail()
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
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.article-actions {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.article-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 20px;
}

.like-button {
  padding: 8px 16px;
  border: 1px solid #ddd;
  border-radius: 20px;
  background-color: white;
  cursor: pointer;
  transition: all 0.3s ease;
}

.like-button.liked {
  background-color: #ffe0e0;
  border-color: #ff4444;
}

.article-info {
  display: flex;
  gap: 20px;
  color: #666;
  margin: 15px 0;
}

.title-category {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.category-tag {
  display: inline-block;
  padding: 0.3rem 0.8rem;
  background: #e8eaf6;
  color: #1a237e;
  border-radius: 15px;
  font-size: 0.9rem;
  align-self: flex-start;
}

.article-header h2 {
  margin: 0;
}

.comments-section {
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid #eee;
}

.comment-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.comment-author {
  font-weight: 500;
}

.comment-date {
  color: #666;
  font-size: 0.9rem;
}

.comment-content {
  margin: 0;
  line-height: 1.5;
}

.login-message {
  text-align: center;
  margin-top: 1rem;
  padding: 1rem;
  background: #f5f5f5;
  border-radius: 8px;
}

.login-message a {
  color: #1a237e;
  text-decoration: none;
  font-weight: 500;
}

.login-message a:hover {
  text-decoration: underline;
}
</style>
