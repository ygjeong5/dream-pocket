<template>
  <div>
    <h2>ArticleList</h2>
    <div v-if="props.articles && props.articles.length > 0">
      <div 
        v-for="article in articles"
        :key="article.id"
        class="article-item"
        @click="goToDetail(article.id)"
      >
        <div class="article-header">
          <h3>{{ article.title }}</h3>
          <p>{{ article }}</p>
          <span class="like-info">
            <span class="heart-icon">❤️</span>
            <span class="like-count">{{ article.like_count || 0 }}</span>
          </span>
        </div>
        <p>{{ article.content }}</p>
        <div class="article-footer">
          <span>작성자: {{ article.user.username }}</span>
          <span>{{ formatDate(article.created_at) }}</span>
        </div>
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
import { onMounted } from 'vue'

const store = useEggStore()
const { articles } = storeToRefs(store)

const router = useRouter()
const props = defineProps({
  articles: {
    type: Array,
    required: true
  }
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
</style>