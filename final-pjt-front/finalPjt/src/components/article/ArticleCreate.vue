<template>
  <div class="create-form">
    <h1>게시글 작성</h1>
    <form>
      <div class="form-group">
        <label for="category">카테고리 :</label>
        <select v-model="formData.category" id="category" required>
          <option value="" disabled>카테고리를 선택하세요</option>
          <option 
            v-for="category in categories" 
            :key="category.value" 
            :value="category.value"
          >
            {{ category.name }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="title">제목 :</label>
        <input v-model="formData.title" type="text" id="title" required />
      </div>
      <div class="form-group">
        <label for="content">내용 :</label>
        <textarea v-model="formData.content" id="content" required></textarea>
      </div>
      <div class="button-group">
        <button @click.prevent="createArticle" class="submit-btn">작성완료</button>
        <RouterLink :to="{ name: 'ArticleView' }">
          <button class="cancel-btn">취소</button>
        </RouterLink>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useEggStore } from '@/stores/egg'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { defineProps } from 'vue'

const store = useEggStore()
const router = useRouter()

const categories = [
  { name: '자유게시판', value: 'free' },
  { name: '금융지식 나누기', value: 'knowledge' },
  { name: '상품 추천', value: 'recommendation' },
  { name: '공지사항', value: 'notice' }
]

const formData = ref({
  title: '',
  content: '',
  category: ''
})

defineProps({
  article: Object
})

const createArticle = async () => {
  if (!store.token) {
    alert('로그인이 필요합니다.')
    router.push({ name: 'LogIn' })
    return
  }

  if (!formData.value.category) {
    alert('카테고리를 선택해주세요.')
    return
  }

  try {
    console.log('전송할 formData:', formData.value)
    await store.createArticle(formData.value)
    console.log('게시글이 생성되었습니다.')
    router.push({ name: 'ArticleView' })
  } catch (err) {
    console.error('게시글 생성 실패:', err)
    if (err.message === '로그인이 필요합니다.') {
      router.push({ name: 'LogIn' })
    }
  }
}

// 로그인 상태 체크
onMounted(() => {
  if (!store.token) {
    router.push({ name: 'LogIn' })
  }
})
</script>

<style scoped>
.create-form {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #333;
}

input[type="text"],
select,
textarea {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

select {
  background-color: white;
  cursor: pointer;
}

textarea {
  min-height: 200px;
  resize: vertical;
}

.button-group {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.submit-btn, .cancel-btn {
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.submit-btn {
  background-color: #1a237e;
  color: white;
}

.submit-btn:hover {
  background-color: #0d47a1;
}

.cancel-btn {
  background-color: #e0e0e0;
  color: #333;
}

.cancel-btn:hover {
  background-color: #bdbdbd;
}
</style>