import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useEggStore = defineStore('counter', () => {
  const count = ref(0)
  
  const articles = ref([])
  const API_URL = ref('http://127.0.0.1:8000/')
  
  const token = ref('9e77ac96e5b7045e00e90474997c63c79f7ba7ae')

  const getArticles = function() {
    console.log(token.value)
    axios({
      method: 'get',
      url: `${API_URL.value}api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      console.log('성공')
      articles.value = res.data
      console.log(articles.value)
    })
  }


  const logIn = function(payload) {
    const username = payload.username
    const password = payload.password
    axios({
      method:'post',
      url: `${API_URL.value}accounts/login/`,
      data: { 
        username, password
      }
    }) 
    .then((res)=> {
      // token.value = res.data.key
      articles.value = res.data
      console.log('성공')
    })
  }



  return { API_URL, articles, getArticles, logIn}
}, { persist: true})
