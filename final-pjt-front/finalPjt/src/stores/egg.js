import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router'

export const useEggStore = defineStore('egg', () => {
  // state
  const count = ref(0)
  const articles = ref([])
  const article = ref(null)
  const API_URL = 'http://127.0.0.1:8000/'
  const token = ref(localStorage.getItem('token'))
  const financialCartList = ref(JSON.parse(localStorage.getItem('financialCart')) || [])
  const savingCartList = ref(JSON.parse(localStorage.getItem('savingCart')) || [])

  // getters
  const isLogin = computed(() => token.value !== null)

  // actions
  const getArticles = async () => {
    try {
      const response = await axios({
        method: 'get',
        url: `${API_URL}articles/`,
        headers: token.value ? { Authorization: `Token ${token.value}` } : {}
      })
      articles.value = response.data
    } catch (error) {
      if (error.response && error.response.status === 401) {
        const response = await axios.get(`${API_URL}articles/`)
        articles.value = response.data
      } else {
        console.error('게시글 로딩 실패:', error)
        articles.value = []
      }
    }
  }

  const getArticleDetail = async (articleId) => {
    try {
      const response = await axios({
        method: 'get',
        url: `${API_URL}articles/${articleId}`,
        headers: token.value ? { Authorization: `Token ${token.value}` } : {}
      })
      article.value = response.data
      return article.value
    } catch (error) {
      if (error.response && error.response.status === 401) {
        const response = await axios.get(`${API_URL}articles/${articleId}`)
        article.value = response.data
        return article.value
      } else {
        console.error('게시글 상세 조회 실패:', error)
        throw error
      }
    }
  }

  const deleteArticle = async (articleId) => {
    try {
      await axios({
        method: 'delete',
        url: `${API_URL}articles/${articleId}`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      console.log('게시글 삭제 성공')
      await getArticles()
    } catch (error) {
      console.error('게시글 삭제 실패:', error)
      throw error
    }
  }

  const updateArticle = async (articleId, articleData) => {
    try {
      const response = await axios({
        method: 'put',
        url: `${API_URL}articles/${articleId}/`,
        data: articleData,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      console.log('게시글 수정 성공')
      article.value = response.data
      return response.data
    } catch (error) {
      console.error('게시글 수정 실패:', error)
      throw error
    }
  }

  const createComment = async (commentData) => {
    try {
      const response = await axios.post(
        `${API_URL}articles/comments/`,
        commentData,
        {
          headers: {
            Authorization: `Token ${token.value}`
          }
        }
      )
      console.log('댓글 작성 성공')
      return response.data
    } catch (error) {
      console.error('댓글 작성 실패:', error)
      throw error
    }
  }

  const deleteComment = async (commentId) => {
    try {
      await axios({
        method: 'delete',
        url: `${API_URL}/articles/comments/${commentId}/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      console.log('댓글 삭제 성공')
    } catch (error) {
      console.error('댓글 삭제 실패:', error)
      throw error
    }
  }

  const logIn = async (payload) => {
    try {
      const response = await axios({
        method: 'post',
        url: `${API_URL}accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password
        }
      })
      token.value = response.data.key
      localStorage.setItem('token', response.data.key)
      console.log('로그인 성공')
      router.push({ name: 'Home' })
    } catch (error) {
      console.error('로그인 실패:', error.response?.data || error.message)
      if (error.response?.data?.non_field_errors) {
        window.alert(error.response.data.non_field_errors[0])
      } else {
        window.alert('아이디 또는 비밀번호를 확인해주세요.')
      }
      throw error
    }
  }

  const logOut = async () => {
    try {
      await axios({
        method: 'post',
        url: `${API_URL}accounts/logout/`,
      })
      token.value = null
      localStorage.removeItem('token')
      window.alert('로그아웃 되었습니다.')
      router.push({ name: 'Home' })
    } catch (error) {
      console.error('로그아웃 실패:', error)
      token.value = null
      localStorage.removeItem('token')
      router.push({ name: 'Home' })
    }
  }

  const financialCart = (productId) => {
    if (!financialCartList.value.includes(productId)) {
      financialCartList.value.push(productId)
      localStorage.setItem('financialCart', JSON.stringify(financialCartList.value))
    }
  }

  const financialListDelete = (productId) => {
    financialCartList.value = financialCartList.value.filter((id) => id !== productId)
    localStorage.setItem('financialCart', JSON.stringify(financialCartList.value))
  }

  const savingCart = (productId) => {
    if (!savingCartList.value.includes(productId)) {
      savingCartList.value.push(productId)
      localStorage.setItem('savingCart', JSON.stringify(savingCartList.value))
    }
  }

  const savingListDelete = (productId) => {
    savingCartList.value = savingCartList.value.filter((id) => id !== productId)
    localStorage.setItem('savingCart', JSON.stringify(savingCartList.value))
  }

  const createArticle = async (articleData) => {
    if (!token.value) {
      throw new Error('로그인이 필요합니다.')
    }

    try {
      const response = await axios({
        method: 'post',
        url: `${API_URL}articles/`,
        data: {
          title: articleData.title,
          content: articleData.content,
          category: articleData.category
        },
        headers: {
          Authorization: `Token ${token.value}`,
          'Content-Type': 'application/json'
        }
      })
      await getArticles()
      return response.data
    } catch (error) {
      console.error('게시글 생성 실패:', error)
      throw error
    }
  }

  return {
    count,
    articles,
    article,
    token,
    financialCartList,
    savingCartList,
    isLogin,
    getArticles,
    getArticleDetail,
    deleteArticle,
    updateArticle,
    createComment,
    deleteComment,
    logIn,
    logOut,
    financialCart,
    financialListDelete,
    savingCart,
    savingListDelete,
    createArticle
  }
})
