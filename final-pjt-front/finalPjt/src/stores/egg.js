import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useEggStore = defineStore('counter', () => {
  const count = ref(0)
  
  const articles = ref([])
  const API_URL = ref('http://127.0.0.1:8000/')

  const getArticles = function() {
    axios({
      method: 'get',
      url: `${API_URL}/articles/`
    })
    .then(res=>{
      articles.value = res.data
    })
  }

  return { API_URL, articles, getArticles}
}, { persist: true})
