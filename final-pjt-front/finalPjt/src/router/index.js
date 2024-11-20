import { createRouter, createWebHistory } from 'vue-router'
import { useEggStore } from '@/stores/egg'

import LicenseView from '@/views/LicenseView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ProfileUpdate from '@/components/profile/ProfileUpdate.vue'
import ProfileView from '@/views/ProfileView.vue'
import RateConvertView from '@/views/RateConvertView.vue'
import MainView from '@/views/MainView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
    path: '/',
    name: 'home',
    component: MainView,

    },
    {
      path: '/signup/license',
      name: 'LicenseView',
      component: LicenseView,
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView,
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView,
    },
    {
      path: '/article',
      name: 'ArticleView',
      component: ArticleView,
    },
    {
      path: '/profile/update',
      name: 'ProfileUpdate',
      component: ProfileUpdate,
    },
    {
      path: '/profile',
      name: 'ProfileView',
      component: ProfileView,
    },
    {
      path: '/rate-convert',
      name: 'RateConvertView',
      component: RateConvertView,
    },
    
  ],
})

router.beforeEach((to, from) => {
  const store = useEggStore()
  console.log(to.name)
  console.log(store.isLogin)
  if ((to.name !== 'LogInView' && to.name !== 'SignUpView' ) && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView'}
  }
  if ((to.name === 'LogInView' || to.name === 'SignUpView') && store.isLogin) {
    window.alert('로그인 되어 있습니다.')
    return { name: 'home'}
  }
})

export default router
