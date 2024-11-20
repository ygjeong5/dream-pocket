import { createRouter, createWebHistory } from 'vue-router'

import LicenseView from '@/views/LicenseView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ProfileUpdate from '@/components/profile/ProfileUpdate.vue'
import ProfileView from '@/views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
      path: '/profile/update',
      name: 'ProfileUpdate',
      component: ProfileUpdate,
    },
    {
      path: '/profile',
      name: 'ProfileView',
      component: ProfileView,
    },
    
  ],
})

export default router
