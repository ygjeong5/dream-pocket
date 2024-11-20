import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router'
import { faL } from '@fortawesome/free-solid-svg-icons'


export const useEggStore = defineStore('counter', () => {
  const count = ref(0)
  
  const articles = ref([])
  const API_URL = ref('http://127.0.0.1:8000/')
  
  const token = ref(null)


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

  // 로그인 로직
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
      token.value = res.data.key
      console.log('로그인성공')
      // 로그인 성공 시 홈으로 이동
      router.push({ name: 'home'})
    })
  }

  // 로그인 상태 표시 
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // 로그아웃
  const logOut = function () {
    console.log('gg')
    axios({
      method: 'post',
      url: `${API_URL.value}accounts/logout/`,
    })
      .then((res) => {
        console.log(res.data)
        window.alert('로그아웃 되었습니다.')
        token.value = null
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { API_URL, articles, getArticles, logIn, logOut, isLogin, token}
}, { persist: true})
