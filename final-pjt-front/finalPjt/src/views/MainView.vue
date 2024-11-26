<template>
  <div calss="mainPage">
    <!-- card -->
     <div class="banner">
       <div id="carousel" class="carousel slide" data-bs-ride="carousel">
         <!-- 하단 버튼 -->
         <div class="carousel-indicators">
           <button type="button" data-bs-target="#carousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
           <button type="button" data-bs-target="#carousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
           <button type="button" data-bs-target="#carousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
         </div>
         
       <div class="carousel-inner">
         <div class="carousel-item active ">
           <img src="@/assets/test1.png" alt="mainbanner" class="d-block">
         </div>
   
         <div class="carousel-item">
           <img src="@/assets/test1.png"  alt="mainbanner">
         </div>
         <div class="carousel-item" >
           <img src="@/assets/test1.png"  alt="mainbanner">
         </div>
       </div>
       <button class="carousel-control-prev" type="button" data-bs-target="#carousel" data-bs-slide="prev">
         <span class="carousel-control-prev-icon" aria-hidden="true"></span>
         <span class="visually-hidden">Previous</span>
       </button>
       <button class="carousel-control-next" type="button" data-bs-target="#carousel" data-bs-slide="next">
         <span class="carousel-control-next-icon" aria-hidden="true"></span>
         <span class="visually-hidden">Next</span>
       </button>
     </div>
    </div>
  </div>
  <div class="chatbot-section">
    <div class="chatbot-container">
      <ChatBot/>
    </div>
  </div>
  <div class="mainContent">
    <div class="content-card quiz">
      <div class="card-icon">❓</div>
      <div class="card-info">
        <h3>오늘의 퀴즈</h3>
        <p class="quiz-question">{{ body }}</p>
        <RouterLink :to="{ name: 'QuizGame' }" class="card-button">
          문제풀러 가기
        </RouterLink>
      </div>
    </div>

    <div class="content-card game">
      <div class="card-icon">🎮</div>
      <div class="card-info">
        <h3>금융 게임</h3>
        <p>재미있게 배우는 금융 게임!</p>
        <RouterLink :to="{ name: 'GameView' }" class="card-button">
          게임하러 가기
        </RouterLink>
      </div>
    </div>

    <div class="content-card map">
      <div class="card-icon">🗺️</div>
      <div class="card-info">
        <h3>주변 은행 찾기</h3>
        <p>가까운 은행을 찾아보세요</p>
        <RouterLink :to="{name: 'map'}" class="card-button">
          지도 보기
        </RouterLink>
      </div>
    </div>
  </div>
  <div class="youtube">
    <swiper
    :slidesPerView="5"
    :spaceBetween="30"
    :loop="true"
    :pagination="{
      clickable: true,
    }"
    :navigation="true"
    :modules="modules"
    class="mySwiper"
  > 
    <swiper-slide> 
      <a :href="video[0].url">
        <img :src="video[0].thumbnail" alt="">
      </a></swiper-slide>
    <swiper-slide> 
    <a :href="video[1].url">
      <img :src="video[1].thumbnail" alt="">
    </a></swiper-slide>
    <swiper-slide> 
    <a :href="video[2].url">
      <img :src="video[2].thumbnail" alt="">
    </a></swiper-slide>
    <swiper-slide> 
    <a :href="video[3].url">
      <img :src="video[3].thumbnail" alt="">
    </a></swiper-slide>
    <swiper-slide> 
    <a :href="video[4].url">
      <img :src="video[4].thumbnail" alt="">
    </a></swiper-slide>
    <swiper-slide> 
      <a :href="video[5].url">
        <img :src="video[5].thumbnail" alt="">
      </a></swiper-slide>
    <swiper-slide> 
    <a :href="video[6].url">
      <img :src="video[6].thumbnail" alt="">
    </a></swiper-slide>
    <swiper-slide> 
    <a :href="video[7].url">
      <img :src="video[7].thumbnail" alt="">
    </a></swiper-slide>
    <swiper-slide> 
    <a :href="video[8].url">
      <img :src="video[8].thumbnail" alt="">
    </a></swiper-slide>
    <swiper-slide> 
    <a :href="video[9].url">
      <img :src="video[9].thumbnail" alt="">
    </a></swiper-slide>
    <swiper-slide> 
    <a :href="video[10].url">
      <img :src="video[10].thumbnail" alt="">
    </a></swiper-slide>
  </swiper>
  </div >
 
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { ref, onMounted } from 'vue';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/css/navigation';
import axios from 'axios';

// Import required modules
import { Pagination, Navigation } from 'swiper/modules';

import ChatBot from '@/components/chatbot/Chatbot.vue';
import { useEggStore } from '@/stores/egg';

const quizInfo = ref([]);

const body = ref('')
const store = useEggStore()
const fetchQuizInfo = () => {
  axios({
    method: 'GET',
    url: 'http://localhost:8000/api/v1/quiz_game/quiz-info/',
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      quizInfo.value = res.data;
      body.value = quizInfo.value[randomInt].body
      
    })
    .catch((err) => {
      console.error(err);
    });
  };

  onMounted(() => {
    fetchQuizInfo();
  });

const n = 90; // 원하는 범위의 상한값
const randomInt = Math.floor(Math.random() * n);
console.log(randomInt);

// Swiper에 필요한 modules 설정
const modules = [Pagination, Navigation];
  
  const video = ref([
    { id: "video_id_1", title: "[부자되는 재테크] 은행원도 알려주지 않는 예금과 적금 활용법!! - 1을 모으는 방법 #.13", url: 'https://youtu.be/aZxYnGO_7wo?si=yhlR5X_A_k8cmnxC', thumbnail: "thumbnail/thumbnail1.jpg" },
    { id: "video_id_2", title: "재테크, 지금도 늦었다.", url: 'https://youtu.be/SpWz5Q4OS1A?si=eGkVJKJBXKmyajtt', thumbnail: "thumbnail/thumbnail2.jpg" },
    { id: "video_id_3", title: '슈카쌤 "설마 이걸 모르지는 않겠지"', url: 'https://youtu.be/X1L5w_pBRhY?si=5kH_OPKp4AZkfG2n', thumbnail: "thumbnail/thumbnail3.jpg" },
    { id: "video_id_4", title: "[경제가 군금해?!] EP 02. 투자성향이 군금해?!", url: 'https://www.youtube.com/watch?v=FGUUw2Jw_qs', thumbnail: "thumbnail/thumbnail4.jpg" },
    { id: "video_id_5", title: "기초편3(금리). 금리가 당신의 삶에 미치는 영향", url: 'https://www.youtube.com/watch?v=fI_u8STJtAc', thumbnail: "thumbnail/thumbnail5.jpg" },
    { id: "video_id_6", title: "[Full] 나의 두 번째 교과서 - 경제 3강 금리와 환율, 밀고 당기는 돈의 역학", url: 'https://www.youtube.com/watch?v=1Onp3C6jYYE', thumbnail: "thumbnail/thumbnail6.jpg" },
    { id: "video_id_7", title: "혹시 청년이세요? 🙋‍ 2024 달라진 청년 지원 정책 종합 선물 풀어보기! 🎁 S3 Ep.3 | 기획재정부", url: 'https://www.youtube.com/watch?v=CEU2_xjoguY', thumbnail: "thumbnail/thumbnail7.jpg" },
    { id: "video_id_8", title: "[재테크의 정석] 파킹통장이 뭐지?? (예적금을 이븐하게 곁들인..)", url: 'https://www.youtube.com/watch?v=bJjN2vrp-Oc', thumbnail: "thumbnail/thumbnail8.jpg" },
    { id: "video_id_9", title: "재테크, 지금도 안늦었다.", url: 'https://www.youtube.com/watch?v=7VDvW1zCZ8c', thumbnail: "thumbnail/thumbnail9.jpg" },
    { id: "video_id_10", title: "[주식] 드디어 배운 '재무제표' 읽는법(홍진경,슈카) [공부왕찐천재]", url: 'https://www.youtube.com/watch?v=bE1iSUYA0KI', thumbnail: "thumbnail/thumbnail10.jpg" },
    { id: "video_id_11", title: "[경제가 군금해?!] EP 03. 신용이 군금해?!", url: 'https://www.youtube.com/watch?v=_khYfd7zDSk', thumbnail: "thumbnail/thumbnail11.jpg" },
    { id: "video_id_12", title: "주식 초보라면 꼭 알아둬야 할 차트 보는 방법", url: 'https://www.youtube.com/watch?v=hI3pzjLbOzY', thumbnail: "thumbnail/thumbnail12.jpg" },
    { id: "video_id_13", title: "[2024 미국 대선-반도체산업] 美 대선 이후 반도체 산업 영향과 그에 따른 대응방안에 대해 알아봤습니다🧐", url: 'https://www.youtube.com/watch?v=ZZ-weu_Ck7A', thumbnail: "thumbnail/thumbnail13.jpg" },
    { id: "video_id_14", title: "가장 기본적인 투자방법", url: 'https://www.youtube.com/watch?v=5lHHAxyXI_g', thumbnail: "thumbnail/thumbnail14.jpg" }
  ]);

</script>

<style scoped>



.mainPage {
  position: relative;
  height: 1000px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.banner {
  margin: 20px 10%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.carousel-inner > .carousel-item {
  text-align: center;
  /* width: 100%; */
}

.carousel-item, .carousel-item > img {
  width: 100%;
  object-fit: cover;
}

.custom-indicator {
  width: 12px !important;
  height: 12px !important;
  border-radius: 50% !important;
  /* background-color: rgba(255, 255, 255, 0.5) !important; */
  border: none !important;
  margin: 0 6px !important;
}

.custom-indicator.active {
  /* background-color: #ffffff !important; */
  transform: scale(1.2);
  transition: all 0.3s ease;
}

/* 네비게이션 버튼 스타일 */
.custom-carousel-control {
  width: 5%;
  /* background: linear-gradient(90deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0) 100%); */
  opacity: 0;
  transition: opacity 0.3s ease;
}

.custom-carousel-control:hover {
  opacity: 1;
}

.carousel-control-prev {
  background: linear-gradient(90deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0) 100%);
}

.carousel-control-next {
  background: linear-gradient(-90deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0) 100%);
}

@media (max-width: 768px) {
  .carousel-item, .carousel-item > img {
    height: 400px;
}
}

.youtube {
  height: 400px;
  max-height: 400px;
  margin: 40px 10%;
  background-color: rgb(61, 61, 63);
  padding: 20px 40px;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  position: relative;
}

.mainContent {
  display: flex;
  justify-content: center;
  align-items: stretch;
  gap: 2rem;
  padding: 3rem 10%;
  background: linear-gradient(145deg, #f8f9fa, #e8f1f8);
}

.chatbot-section {
  width: 100%;
  padding: 60px 0;
  background: linear-gradient(145deg, #2c3e50, #34495e);
  position: relative;
  overflow: hidden;
}

.chatbot-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('@/assets/pattern.png') repeat; /* 필요한 경우 패턴 이미지 추가 */
  opacity: 0.1;
}

.chatbot-container {
  width: 80%;
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.ad {
  border: none;
  height: 220px;
  width: 500px;
  border-radius: 20px;
  padding: 30px;
  margin: 0 25px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: white;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.ad:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.12);
}

.ad h3 {
  font-size: 22px;
  font-weight: 600;
  color: #2c3e50;
  text-align: center;
  margin-bottom: 20px;
}

.ad a {
  padding: 12px 24px;
  background: linear-gradient(145deg, #3498db, #2980b9);
  color: white;
  border-radius: 25px;
  text-decoration: none;
  font-weight: 500;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.ad a:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.youtube {
  height: 450px;
  max-height: 450px;
  margin: 60px 10%;
  background: linear-gradient(145deg, #2c3e50, #34495e);
  padding: 30px 60px;
  border-radius: 25px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
  position: relative;
}

.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: transparent;
  height: 300px;
  width: calc(20% - 20px) !important;
  margin: 0 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.swiper-slide:hover {
  transform: scale(1.05);
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 220px;
  object-fit: cover;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

/* 네비게이션 버튼 스타일 수정 */
.swiper-button-next,
.swiper-button-prev {
  background-color: rgba(255, 255, 255, 0.9);
  color: #2c3e50 !important;
  width: 45px !important;
  height: 45px !important;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}

.swiper-button-prev {
  left: -50px !important;
}

.swiper-button-next {
  right: -50px !important;
}

.swiper-button-next:hover,
.swiper-button-prev:hover {
  background-color: rgba(0, 0, 0, 0.8);
  transform: translateY(-50%) scale(1.1);
}

.swiper-button-next::after,
.swiper-button-prev::after {
  font-size: 20px !important;
}

/* 슬라이더 컨테이너 여백 조정 */
.swiper-container {
  margin: 0 auto;
  position: relative;
  overflow: visible !important;
}

/* 추가: 버튼이 보이는 영역 확보 */
.youtube {
  margin-left: calc(10% + 50px);
  margin-right: calc(10% + 50px);
}

.content-card {
  flex: 1;
  min-width: 300px;
  background: white;
  border-radius: 20px;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.content-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.15);
}

.card-icon {
  font-size: 2.5rem;
  width: 70px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(145deg, #e8f1f8, #d4e6f1);
  border-radius: 50%;
  margin-bottom: 1rem;
}

.card-info {
  text-align: center;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.card-info h3 {
  font-size: 1.5rem;
  color: #2c3e50;
  margin: 0;
  font-family: 'DNFBitBitv2';
}

.card-info p {
  color: #666;
  margin: 0;
  flex: 1;
}

.quiz-question {
  font-size: 1.1rem;
  color: #2980b9;
  font-weight: 500;
}

.card-button {
  display: inline-block;
  padding: 0.8rem 1.5rem;
  background: linear-gradient(145deg, #3498db, #2980b9);
  color: white;
  border-radius: 25px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  border: none;
  font-family: 'DNFBitBitv2';
}

.card-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  background: linear-gradient(145deg, #2980b9, #2472a4);
}

@media (max-width: 1024px) {
  .mainContent {
    flex-direction: column;
    padding: 2rem 5%;
  }

  .content-card {
    width: 100%;
  }
}

</style>