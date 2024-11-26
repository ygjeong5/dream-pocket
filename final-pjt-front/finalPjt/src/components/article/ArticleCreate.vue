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
  max-width: 1000px;
  margin: 3rem auto;
  padding: 2rem;
  background: linear-gradient(145deg, #e8f1f8, #d4e6f1);
  border: 3px solid #2980b9;
  border-radius: 15px;
  box-shadow: 0 6px 0 #85929e;
}

h1 {
  font-family: 'DNFBitBitv2';
  font-size: 2.5rem;
  background: linear-gradient(to left top, #2980b9, #3498db);
  -webkit-background-clip: text;
  -webkit-text-stroke: 2px rgba(39, 54, 154, 0.726);
  color: transparent;
  text-align: center;
  margin-bottom: 2rem;
  animation: titleFloat 3s ease-in-out infinite;
}

.form-group {
  margin-bottom: 1.5rem;
  background: white;
  padding: 1.2rem;
  border: 3px solid #7fb3d5;
  border-radius: 15px;
  box-shadow: 0 4px 0 #85929e;
}

.form-group label {
  display: block;
  margin-bottom: 0.8rem;
  font-family: 'DNFBitBitv2';
  font-size: 1.2rem;
  color: #2980b9;
}

input[type="text"],
select,
textarea {
  width: 100%;
  padding: 1rem;
  border: 2px solid #7fb3d5;
  border-radius: 10px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

input[type="text"]:focus,
select:focus,
textarea:focus {
  outline: none;
  border-color: #2980b9;
  box-shadow: 0 0 0 2px rgba(41, 128, 185, 0.2);
}

select {
  background-color: white;
  cursor: pointer;
  font-family: 'DNFBitBitv2';
}

textarea {
  min-height: 200px;
  resize: vertical;
}

.button-group {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
  justify-content: center;
}

.submit-btn, .cancel-btn {
  padding: 0.8rem 1.5rem;
  border: 3px solid #7fb3d5;
  border-radius: 19px;
  cursor: pointer;
  font-family: 'DNFBitBitv2';
  font-size: 15px;
  box-shadow: 0 4px 0 #85929e;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

.submit-btn {
  background: linear-gradient(145deg, #2980b9, #3498db);
  color: white;
}

.cancel-btn {
  background: white;
  color: #2980b9;
}

.submit-btn::before,
.cancel-btn::before {
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

.submit-btn:hover::before,
.cancel-btn:hover::before {
  left: 100%;
}

.submit-btn:hover,
.cancel-btn:hover {
  transform: translateY(2px);
  box-shadow: 0 2px 0 #85929e;
}

@keyframes titleFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
</style>