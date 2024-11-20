import { createRouter, createWebHistory } from 'vue-router';

// Import Views and Components
import LicenseView from '@/views/LicenseView.vue';
import SignUpView from '@/views/SignUpView.vue';
import LogInView from '@/views/LogInView.vue';
import ArticleView from '@/views/ArticleView.vue';
import ProfileUpdate from '@/components/profile/ProfileUpdate.vue';
import ProfileView from '@/views/ProfileView.vue';
import ArticleCreate from '@/components/article/ArticleCreate.vue';
import ArticleList from '@/components/article/ArticleList.vue';
import ArticleUpdate from '@/components/article/ArticleUpdate.vue';
import ArticleListDetail from '@/components/article/ArticleListDetail.vue';

// Define Routes
const routes = [
  // 회원가입 및 로그인 관련
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

  // 메인 페이지 및 게시글 관련
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

  // 프로필 관련
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView,
  },
  {
    path: '/profile/update',
    name: 'ProfileUpdate',
    component: ProfileUpdate,
  },
];

// Create Router
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
