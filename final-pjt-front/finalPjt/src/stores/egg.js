import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router'
import { faL } from '@fortawesome/free-solid-svg-icons'

export const useEggStore = defineStore('counter', () => {
  const count = ref(0)
  const articles = ref([])
  const article = ref(null)
  const API_URL = ref('http://127.0.0.1:8000/')
  const token = ref(null)

  const getArticles = function() {
    axios({
      method: 'get',
      url: `${API_URL.value}articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      console.log('성공')
      articles.value = res.data
    })
  }

  // 게시글 상세 정보 불러오기
  const getArticleDetail = function(articleId) {
    console.log('요청 URL:', `${API_URL.value}articles/${articleId}`)  // URL 확인용
    return axios({
      method: 'get',
      url: `${API_URL.value}articles/${articleId}`,  // 끝의 슬래시(/) 제거
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      console.log('서버 응답:', res.data)  // 응답 데이터 확인용
      article.value = res.data
      return article.value
    })
    .catch(error => {
      console.error('API 요청 에러:', error.response)  // 자세한 에러 정보 확인
      throw error
    })
  }

  // 게시글 삭제
  const deleteArticle = function(articleId) {
    return axios({
      method: 'delete',
      url: `${API_URL.value}articles/${articleId}`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(() => {
      console.log('게시글 삭제 성공')
      // 게시글 목록 새로고침
      return this.getArticles()
    })
  }

  // 게시글 수정
  const updateArticle = function(articleId, articleData) {
    return axios({
      method: 'put',
      url: `${API_URL.value}articles/${articleId}`,
      data: articleData,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      console.log('게시글 수정 성공')
      article.value = res.data
      return res.data
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
      token.value = res.data.key
      console.log('로그인성공')
      // 로그인 성공 시 홈으로 이동
      router.push({ name: 'Home'})
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

   return { 
    count,
    articles, 
    article,
    getArticles, 
    getArticleDetail,
    deleteArticle,
    updateArticle,
    logIn, 
    logOut,
    token,
    isLogin,
    API_URL
  }

}, { persist: true})
