import ArticleCreate from '@/components/article/ArticleCreate.vue'
import ArticleList from '@/components/article/ArticleList.vue'
import ArticleUpdate from '@/components/article/ArticleUpdate.vue'
import ArticleListDetail from '@/components/article/ArticleListDetail.vue'
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
import MapView from '@/views/MapView.vue'

// Define Routes

 const router = createRouter({
    history : createWebHistory(import.meta.env.BASE_URL),
    routes: [
    {
    path: '/',
    name: 'Home',
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
    path: '/',
    name: 'ArticleView',
    component: ArticleView,
  },
  {
    path: '/article/list',
    name: 'ArticleList',
    component: ArticleList,
  },  
  {
    path: '/article/detail/:id',
    name: 'ArticleListDetail',
    component: ArticleListDetail,
  },
  {
    path: '/article/create',
    name: 'ArticleCreate',
    component: ArticleCreate,
  },
  {
    path: '/article/update/:id',
    name: 'ArticleUpdate',
    component: ArticleUpdate,
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
    {
      path: '/map',
      name: 'map',
      component: MapView,
    },
  ],  
})

router.beforeEach((to, from) => {
  const store = useEggStore()
  if ((to.name !== 'LogInView' && to.name !== 'SignUpView' && to.name !== 'Home' ) && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView'}
  }
  if ((to.name === 'LogInView' || to.name === 'SignUpView') && store.isLogin) {
    window.alert('로그인 되어 있습니다.')
    return { name: 'Home'}
  }
})

export default router

