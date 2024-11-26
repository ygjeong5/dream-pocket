<template>
  <div class="article-update">
    <h2>게시글 수정</h2>
    <form @submit.prevent="updateArticle">
      <div class="form-group">
        <label for="title">제목</label>
        <input 
          type="text" 
          id="title" 
          v-model="title" 
          required
        >
      </div>
      <div class="form-group">
        <label for="content">내용</label>
        <textarea 
          id="content" 
          v-model="content" 
          required
        ></textarea>
      </div>
      <div class="form-actions">
        <button type="submit" class="btn-submit">수정</button>
        <button type="button" @click="goBack" class="btn-cancel">취소</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useEggStore } from '@/stores/egg'

const route = useRoute()
const router = useRouter()
const store = useEggStore()

const title = ref('')
const content = ref('')

onMounted(async () => {
  try {
    const article = await store.getArticleDetail(route.params.id)
    title.value = article.title
    content.value = article.content
  } catch (error) {
    console.error('게시글 정보 불러오기 실패:', error)
  }
})

const updateArticle = async () => {
  try {
    await store.updateArticle(route.params.id, {
      title: title.value,
      content: content.value
    })
    router.push({
      name: 'ArticleListDetail',
      params: { id: route.params.id }
    })
  } catch (error) {
    console.error('게시글 수정 실패:', error || error.message)
    alert('게시글 수정에 실패했습니다. 다시 시도해주세요.')
  }
}

const goBack = () => {
  router.go(-1)
}
</script>

<style scoped>
.article-update {
  max-width: 1000px;
  margin: 3rem auto;
  padding: 2rem;
  background: linear-gradient(145deg, #e8f1f8, #d4e6f1);
  border: 3px solid #2980b9;
  border-radius: 15px;
  box-shadow: 0 6px 0 #85929e;
}

h2 {
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
textarea {
  width: 100%;
  padding: 1rem;
  border: 2px solid #7fb3d5;
  border-radius: 10px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

textarea {
  min-height: 200px;
  resize: vertical;
}

.form-actions {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-top: 2rem;
}

.btn-submit, .btn-cancel {
  padding: 0.8rem 1.5rem;
  border: 3px solid #7fb3d5;
  border-radius: 19px;
  font-family: 'DNFBitBitv2';
  font-size: 15px;
  cursor: pointer;
  box-shadow: 0 4px 0 #85929e;
  transition: all 0.2s ease;
}

.btn-submit {
  background: linear-gradient(145deg, #2980b9, #3498db);
  color: white;
}

.btn-cancel {
  background: white;
  color: #2980b9;
}

.btn-submit:hover,
.btn-cancel:hover {
  transform: translateY(2px);
  box-shadow: 0 2px 0 #85929e;
}

@keyframes titleFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
</style>
