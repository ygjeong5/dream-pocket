<template>
  <div>
    <h2>게시글 목록</h2>
    <div v-if="props.articles && props.articles.length > 0">
      <div 
        v-for="article in props.articles" 
        :key="article.id"
        class="article-item"
        @click="goToDetail(article.id)"
      >
        <h3>{{ article.title }}</h3>
        <p>{{ article.content }}</p>
      </div>
    </div>
    <div v-else>
      <p>작성된 게시글이 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

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
</script>

<style scoped>

</style>