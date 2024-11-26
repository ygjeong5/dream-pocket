<template>
  <div class="news-view">
    <div class="news-list">
      <div 
        v-for="news in newsList" 
        :key="news.id" 
        class="news-item"
      >
        <a :href="news.link" target="_blank" rel="noopener noreferrer" class="news-link">
          <div class="news-card">
            <img :src="news.image" :alt="news.title" class="news-thumbnail" />
            <div class="news-content">
              <h3 class="news-title">{{ news.title }}</h3>
              <p class="news-description">{{ news.description }}</p>
              <span class="news-source">출처: {{ news.source }}</span>
            </div>
          </div>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// 더미 뉴스 데이터
const newsList = ref([
  {
    title: "카카오뱅크, 3년 내 자산 100조원 목표 발표",
    description: "최근 애널리스트 간담회에서 카카오뱅크가 '밸류업' 전략과 주주환원율 확대 계획을 발표했습니다.",
    link: "https://www.hankyung.com/article/2024112645915",
    image: "news/news1.jpg",
    source: "한경닷컴"
  },
  {
    title: "퇴직연금 수익률 1위 동양생명",
    description: "동양생명이 3분기 디폴트옵션 고위험 상품군에서 수익률 27.3%로 1위를 기록했습니다.",
    link: "https://www.hankyung.com/article/2024112645945",
    image: "news/news2.jpg",
    source: "한경닷컴"
  },
  {
    title: "해외 카드 사용액, 사상 최대",
    description: "3분기 해외 카드 사용액이 역대 최고치를 기록하며 여행 소비의 증가를 반영했습니다.",
    link: "https://www.fnnews.com/news/201710051205061051",
    image: "news/news3.jpg",
    source: "파이낸셜뉴스"
  },
  {
    title: "우리은행장 조병규, 연임 포기 선언",
    description: "조직 쇄신을 위한 결정으로 조병규 우리은행장이 연임을 포기한다고 밝혔습니다.",
    link: "https://www.fnnews.com/news/202411261209174950",
    image: "news/news4.jpg",
    source: "파이낸셜뉴스"
  },
  {
    title: "환율 상승 지속, 수출업계 긴장",
    description: "달러 대비 원화 가치가 지속적으로 하락하며 수출업계가 긴장하고 있습니다.",
    link: "https://www.hankyung.com/financial-market",
    image: "news/news5.jpg",
    source: "한경닷컴"
  },
  {
    title: "ESG 경영 강화하는 국내 은행들",
    description: "주요 은행들이 지속 가능한 금융을 위해 ESG 경영 전략을 강화하고 있습니다.",
    link: "https://www.fnnews.com/",
    image: "news/news6.jpg",
    source: "파이낸셜뉴스"
  },
  {
    title: "금리 인상 가능성, 소비 심리 위축 우려",
    description: "금리 인상 가능성이 높아지며 소비 심리 위축이 우려되고 있습니다.",
    link: "https://www.hankyung.com/financial-market",
    image: "news/news7.jpg",
    source: "한경닷컴"
  },
  {
    title: "금융권, 블록체인 기술 활용 확대",
    description: "블록체인 기술이 금융 서비스에 본격적으로 도입되고 있습니다.",
    link: "https://www.fnnews.com/section/002001002002",
    image: "news/news8.jpg",
    source: "파이낸셜뉴스"
  },
  {
    title: "핀테크 스타트업, 투자 유치 기록 경신",
    description: "국내 핀테크 스타트업들이 올해 투자 유치 규모에서 기록을 경신했습니다.",
    link: "https://www.hankyung.com/financial-market",
    image: "news/news9.jpg",
    source: "한경닷컴"
  },
  {
    title: "글로벌 주식시장, 혼조세 지속",
    description: "주요 글로벌 주식시장이 경기 불확실성 속에서 혼조세를 보이고 있습니다.",
    link: "https://www.fnnews.com/section/002001002002",
    image: "news/news6.jpg",
    source: "파이낸셜뉴스"
  }
])

const loading = ref(false)
const error = ref(false)
</script>

<style scoped>
.news-view {
  padding: 20px;
  background-color: #f7f9fc;
}

.page-title {
  text-align: center;
  font-size: 28px;
  margin-bottom: 30px;
  color: #2c3e50;
  font-family: 'Pretendard', sans-serif;
}

.news-list {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 한 줄에 4개 */
  gap: 20px;
  justify-items: center;
}

.news-item {
  width: 100%;
  text-align: center;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  background: #fff;
  overflow: hidden;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.news-item:hover {
  transform: scale(1.05);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.2);
}

.news-link {
  display: block;
  text-decoration: none;
  color: inherit;
}

.news-card {
  position: relative;
}

.news-thumbnail {
  width: 100%;
  height: 200px; /* 카드의 높이 조정 */
  object-fit: cover;
  border-radius: 8px 8px 0 0;
}

.news-content {
  padding: 15px;
}

.news-title {
  font-size: 18px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.news-description {
  font-size: 14px;
  color: #666;
  margin-bottom: 10px;
}

.news-source {
  font-size: 12px;
  color: #999;
}
</style>
