import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useYoutubeStore = defineStore('counter', () => {
  const API_URL = 'https://www.googleapis.com/youtube/v3/search'
  const API_KEY = ''
  const videos = ref([])
  const selectedVideo = ref(null)

  const getVideos = (search) => {
    axios.get(API_URL,{
      method: 'get',
      params: {
        part: 'snippet',
        key: API_KEY,
        type: 'video',
        q: search,
        maxResults: 6,
    
    }})
      .then((res) => {
        console.log(res.data)
        videos.value = res.data.items
      })
      .catch(err => {
        console.log(err)
      })
  }

  const setSelectedVideo = (video) => {
    selectedVideo.value = video
  }

  return { videos, getVideos, setSelectedVideo }
})
