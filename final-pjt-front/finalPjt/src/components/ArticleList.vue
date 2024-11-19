<template>
  <div>
    <h2>ArticleList</h2>
    <ArticleListItem
    v-for="article in store.articles"
    :key="article.id"
    :article="article"/>
  </div>
</template>

<script setup>
  import ArticleListItem from '@/components/ArticleListItem.vue';
  import { onMounted } from 'vue';
  import { useEggStore } from '@/stores/egg';

  const store = useEggStore()

  onMounted(() => {
    store.getArticles()
  })
</script>

<style  scoped>

</style>