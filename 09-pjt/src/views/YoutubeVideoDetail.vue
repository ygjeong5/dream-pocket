<template>
  <div v-if="video">
    <h2>{{ video.snippet.title }}</h2>
    <iframe 
      :src="`https://www.youtube.com/embed/${video.id.videoId}`" 
      frameborder="0" 
      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen 
      width="560" 
      height="315">
    </iframe>
    <p>{{ video.snippet.description }}</p>
    <button @click="toggleSave">{{ isSaved ? '저장 취소' : '저장' }}</button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useYoutubeStore } from '@/stores/counter'

const store = useYoutubeStore()
const route = useRoute()
const video = ref(null)

const savedVideos = computed(() => {
  // LocalStorage에서 저장된 동영상 목록을 가져옵니다.
  const saved = JSON.parse(localStorage.getItem('savedVideos')) || []
  return saved
})

// 동영상을 저장하거나 저장 취소
const toggleSave = () => {
  const currentVideo = video.value
  if (currentVideo) {
    const saved = savedVideos.value
    const videoIndex = saved.findIndex(v => v.id.videoId === currentVideo.id.videoId)

    if (videoIndex === -1) {
      // 저장되지 않은 동영상일 경우
      saved.push(currentVideo)
      localStorage.setItem('savedVideos', JSON.stringify(saved))
    } else {
      // 이미 저장된 동영상일 경우
      saved.splice(videoIndex, 1)
      localStorage.setItem('savedVideos', JSON.stringify(saved))
    }
  }
}

// 현재 선택된 동영상이 저장되었는지 확인
const isSaved = computed(() => {
  const saved = savedVideos.value
  return saved.some(v => v.id.videoId === video.value?.id.videoId)
})
onMounted(() => {
  const videoId = route.params.id
  const foundVideo = store.videos.find(v => v.id.videoId === videoId)
  if (foundVideo) {
    video.value = foundVideo
  } else {
    console.error('Video not found')
  }
})
</script>

<style scoped>

</style>
