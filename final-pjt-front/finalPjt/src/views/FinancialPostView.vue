<template>
  <div class="post-container">
    <div class="tab-container">
      <button 
        :class="['tab-button', { active: activeTab === 'news' }]" 
        @click="switchTab('news')"
      >
        금융 뉴스
      </button>
      <button 
        :class="['tab-button', { active: activeTab === 'education' }]" 
        @click="switchTab('education')"
      >
        유튜브 교육
      </button>
    </div>

    <FinancialNews v-show="activeTab === 'news'" />
    <Youtube v-show="activeTab === 'education'" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import FinancialNews from '@/components/post/FinancialNews.vue'
import Youtube from '@/components/post/Youtube.vue'

const route = useRoute()
const activeTab = ref('news')

const switchTab = (tab) => {
  activeTab.value = tab
}

onMounted(() => {
  // URL의 query parameter에 따라 초기 탭 설정
  if (route.query.tab === 'education') {
    activeTab.value = 'education'
  }
})
</script>

<style scoped>
.post-container {
  max-width: 1080px;
  margin: 0 auto;
  padding: 20px;
}

.tab-container {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  justify-content: flex-end;
}

.tab-button {
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  background-color: #f0f0f0;
  cursor: pointer;
  font-family: 'DNFBitBitv2';
  transition: all 0.3s ease;
}

.tab-button.active {
  background-color: #7fb3d5;
  color: white;
}

.tab-button:hover {
  background-color: #e0e0e0;
}

.tab-button.active:hover {
  background-color: #6b99b8;
}
</style>
