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
import FinancialProductsView from '@/views/FinancialProductsView.vue'
import FinancialProductDetail from '@/components/financialproduct/FinancialProductDetail.vue'
import ChatbotView from '@/views/ChatbotView.vue'
import SavingProductsView from '@/views/SavingProductsView.vue'
import SavingProductDetail from '@/components/financialproduct/SavingProductDetail.vue'
import ProductsView from '@/views/ProductsView.vue'
import FinancialPostView from '@/views/FinancialPostView.vue'
import ProductComparison from '@/components/financialproduct/ProductComparison.vue'
import QuizGame from '@/views/QuizGame.vue'

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
    path: '/article',
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
    { 
      path: '/products',
      name: 'ProductsView',
      component: ProductsView,
    },
    { 
      path: '/financial-products',
      name: 'FinancialProductsView',
      component: FinancialProductsView,
    },
    {
      path: '/financial-product/detail/:id',
      name: 'FinancialProductDetail',
      component: FinancialProductDetail,
    },
    {
      path: '/chatbot',
      name: 'ChatbotView',
      component: ChatbotView,
      meta: { requiresAuth: true }  // 로그인 필요한 경우
    },
    { 
      path: '/saving-products',
      name: 'SavingProductsView',
      component: SavingProductsView,
    },
    {
      path: '/saving-product/detail/:id',
      name: 'SavingProductDetail',
      component: SavingProductDetail,
    },
    {
      path: '/financial-post',
      name: 'FinancialPostView',
      component: FinancialPostView,
    },
    {
      path: '/financial-posts/:id',
      name: 'FinancialPostDetail',
      component: FinancialProductDetail,
    },
    {
      path: '/porduct-comparison',
      name: 'ProductComparison',
      component: ProductComparison,
    },
      {
        path: '/quiz-game',
        name: 'QuizGame',
        component: QuizGame,
        meta: { requiresAuth: true }  // 로그인 필요한 경우
      },
  ],  
})

router.beforeEach((to, from) => {
  const store = useEggStore()
  if ((to.name !== 'LogInView' && to.name !== 'SignUpView' && to.name !== 'Home' && to.name !== 'QuizGame') && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView'}
  }
  if ((to.name === 'LogInView' || to.name === 'SignUpView') && store.isLogin) {
    window.alert('로그인 되어 있습니다.')
    return { name: 'Home'}
  }
})

export default router

