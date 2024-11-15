<template>
  <div>
    <h2>저장된 동영상 목록</h2>
    <div v-if="savedVideos.length > 0">
      <div v-for="video in savedVideos" :key="video.id.videoId">
        <h3>{{ video.snippet.title }}</h3>
        <p>{{ video.snippet.description }}</p>
        <img :src="video.snippet.thumbnails.default.url" alt="Video thumbnail">
        <div>
          <button @click="removeFromSaved(video)">삭제</button>
        </div>
        
      </div>
    </div>
    <div v-else>
      <p>등록된 비디오가 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

const savedList = ref([])

const savedVideos = computed(() => {
  const saved = JSON.parse(localStorage.getItem('savedVideos')) || []
  return saved
})

const removeFromSaved = (video) => {
  const saved = savedVideos.value
  const index = saved.findIndex(v => v.id.videoId === video.id.videoId)
  if (index !== -1) {
    saved.splice(index, 1)
    localStorage.setItem('savedVideos', JSON.stringify(saved))
  }
}
</script>

<style scoped>
button {
  background-color: #ff5c5c;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
}
</style>
