import SavedView from '@/views/SavedView.vue'
import SearchView from '@/views/SearchView.vue'
import YoutubeVideoDetail from '@/views/YoutubeVideoDetail.vue'
import { createRouter, createWebHistory } from 'vue-router'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/search',
      name: 'search',
      component: SearchView
    },
    {
      path:'/detail/:id',
      name: 'detail',
      component: YoutubeVideoDetail
    },
    {
      path:'/saved',
      name: 'saved',
      component: SavedView
    },
  ],
})

export default router
