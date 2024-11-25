import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router'
import { faL } from '@fortawesome/free-solid-svg-icons'


export const useEggStore = defineStore('egg', {
  state: () => ({
    count: 0,
    articles: [],
    article: null,
    API_URL: 'http://127.0.0.1:8000/',
    token: null,
    financialCartList: [],
    savingCartList: []
  }),

  getters: {
    isLogin: (state) => {
      return state.token !== null
    }
  },

  actions: {
    async getArticles() {
      try {
        const response = await axios({
          method: 'get',
          url: `${this.API_URL}articles/`,
          headers: this.token ? { Authorization: `Token ${this.token}` } : {}
        })
        this.articles = response.data
      } catch (error) {
        if (error.response && error.response.status === 401) {
          const response = await axios.get(`${this.API_URL}articles/`)
          this.articles = response.data
        } else {
          console.error('게시글 로딩 실패:', error)
          this.articles = []
        }
      }
    },

    async getArticleDetail(articleId) {
      try {
        const response = await axios({
          method: 'get',
          url: `${this.API_URL}articles/${articleId}`,
          headers: this.token ? { Authorization: `Token ${this.token}` } : {}
        })
        this.article = response.data
        return this.article
      } catch (error) {
        if (error.response && error.response.status === 401) {
          const response = await axios.get(`${this.API_URL}articles/${articleId}`)
          this.article = response.data
          return this.article
        } else {
          console.error('게시글 상세 조회 실패:', error)
          throw error
        }
      }
    },

    deleteArticle(articleId) {
      return axios({
        method: 'delete',
        url: `${this.API_URL}articles/${articleId}`,
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
      .then(() => {
        console.log('게시글 삭제 성공')
        // 게시글 목록 새로고침
        this.getArticles()
      })
    },

    updateArticle(articleId, articleData) {
      return axios({
        method: 'put',
        url: `${this.API_URL}articles/${articleId}/`,
        data: articleData,
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
      .then(res => {
        console.log('게시글 수정 성공')
        this.article = res.data
        return res.data
      })
      .catch(error => {
        console.error('게시글 수정 실패:', error)
        throw error
      })
    },

    createComment(commentData) {
      return axios.post(
        `${this.API_URL}articles/comments/`,
        commentData,
        {
          headers: {
            Authorization: `Token ${this.token}`
          }
        }
      )
      .then(response => {
        console.log('댓글 작성 성공')
        return response.data
      })
      .catch(error => {
        console.error('댓글 작성 실패:', error)
        throw error
      })
    },

    deleteComment(commentId) {
      return axios({
        method: 'delete',
        url: `${this.API_URL}/articles/comments/${commentId}/`,
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
      .then(() => {
        console.log('댓글 삭제 성공')
      })
      .catch(error => {
        console.error('댓글 삭제 실패:', error)
        throw error
      })
    },

    logIn(payload) {
      return axios({
        method: 'post',
        url: `${this.API_URL}accounts/login/`,
        data: { 
          username: payload.username,
          password: payload.password
        },
        headers: {
          'Content-Type': 'application/json'
        }
      }) 
      .then((res) => {
        this.token = res.data.key
        console.log('로그인 성공')
        router.push({ name: 'Home' })
      })
      .catch((error) => {
        console.error('로그인 실패:', error.response?.data || error.message)
        if (error.response?.data?.non_field_errors) {
          window.alert(error.response.data.non_field_errors[0])
        } else {
          window.alert('아이디 또는 비밀번호를 확인해주세요.')
        }
        throw error
      })
    },

    logOut() {
      return axios({
        method: 'post',
        url: `${this.API_URL}accounts/logout/`,
      })
      .then((res) => {
        console.log(res.data)
        window.alert('로그아웃 되었습니다.')
        this.token = null
        router.push({ name: 'Home' })
      })
      .catch((err) => {
        console.log(err)
        this.token = null
        router.push({ name: 'Home' })
      })
    },

    financialCart(productId) {
      if (!this.financialCartList.includes(productId)) {
        this.financialCartList.push(productId)
      }
    },

    financialListDelete(productId) {
      this.financialCartList = this.financialCartList.filter((id) => id !== productId)
    },

    savingCart(productId) {
      if (!this.savingCartList.includes(productId)){
        this.savingCartList.push(productId)
      }
    },

    savingListDelete(productId) {
      this.savingCartList = this.savingCartList.filter((id) => id !== productId)
    },

    async createArticle(articleData) {
      if (!this.token) {
        throw new Error('로그인이 필요합니다.')
      }

      try {
        console.log('전송할 데이터:', articleData) // 디버깅용
        const response = await axios({
          method: 'post',
          url: `${this.API_URL}articles/`,
          data: {
            title: articleData.title,
            content: articleData.content,
            category: articleData.category
          },
          headers: {
            Authorization: `Token ${this.token}`,
            'Content-Type': 'application/json'
          }
        })
        // 게시글 생성 후 목록 새로고침
        await this.getArticles()
        return response.data
      } catch (error) {
        console.error('게시글 생성 실패:', error)
        throw error
      }
    }
  }
})
