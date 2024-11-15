<template>
  <div>
    <form @submit.prevent="getVideo">
      <label for="search">Search</label>
      <input type="text" id="search" v-model.trim="search">
      <input type="submit">
   </form>

   <template v-if="videos && videos.length > 0">
    <div v-for="video in videos" :key="video.id.videoId" @click="selectVideo(video)">
      <h3>{{ video.snippet.title }}</h3>
      <p>{{ video.snippet.description }}</p>
      <img :src="video.snippet.thumbnails.default.url" alt="Video thumbnail">
    </div>
   </template>
   <template v-else>
     <p>No videos found</p>
   </template>
   <!-- <YoutubeVideoDetail v-if="selectedVideo" :video="selectedVideo"/> -->
  </div>
</template>

<script setup>
import { useYoutubeStore } from '@/stores/counter'
import { ref } from 'vue'
import YoutubeVideoDetail from './YoutubeVideoDetail.vue'
import { useRouter } from 'vue-router';

const router = useRouter()
const search = ref('')
const store = useYoutubeStore()
const videos = store.videos
// const getVideo = () => {
//   if (search.value.trim()) {
//     store.getVideos(search.value)
//   }
// }
const getVideo = async () => {
  if (search.value.trim()) {
    await store.getVideos(search.value)
  }
}

const selectedVideo = ref(null)

const selectVideo = (video) => {
  selectedVideo.value = video
  store.setSelectedVideo(video)
  router.push({name:'detail', params:{id:video.id.videoId, video:video}})
}


</script>

<style scoped>

</style>