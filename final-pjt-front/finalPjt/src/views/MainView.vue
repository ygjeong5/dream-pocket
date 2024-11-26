<template>
  <div calss="mainPage">
    <!-- card -->
     <div class="banner">
       <div id="carousel" class="carousel slide" data-bs-ride="carousel">
         <!-- 하단 버튼 -->
         <div class="carousel-indicators">
           <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
           <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
           <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
         </div>
         
       <div class="carousel-inner">
         <div class="carousel-item active " data-bs-interval="8000">
           <img src="@/assets/test1.png" alt="mainbanner">
         </div>
   
         <div class="carousel-item" data-bs-interval="8000">
           <img src="@/assets/test1.png"  alt="mainbanner">
         </div>
         <div class="carousel-item" data-bs-interval="8000">
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

  <div class="mainContent">
    
    <div class="chatbot">
      chatbot
    </div>
    <div class="mypage">
      mypage
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
  </div>
 
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { ref } from 'vue';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/css/navigation';

// Import required modules
import { Pagination, Navigation } from 'swiper/modules';

// Swiper에 필요한 modules 설정
const modules = [Pagination, Navigation];
  
  const video = ref([
    { id: "video_id_1", title: "[부자되는 재테크] 은행원도 알려주지 않는 예금과 적금 활용법!! - 1억을 모으는 방법 #.13", url: 'https://youtu.be/aZxYnGO_7wo?si=yhlR5X_A_k8cmnxC', thumbnail: "thumbnail/thumbnail1.jpg" },
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
  /* background: linear-gradient(-90deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0) 100%); */
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
  height: 300px;
}

.chatbot{
  width: 50%;
  border: 1px black solid;
}

.mypage{
  border: 1px black solid;
  width: 50%;
}

.swiper {
  width: 100%;
  height: 100%;
  padding: 20px 0;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: transparent;
  height: 280px;
  width: calc(20% - 20px) !important;
  margin: 0 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: transform 0.3s ease;
}

.swiper-slide:hover {
  transform: scale(1.05);
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

/* 네비게이션 버튼 스타일 수정 */
.swiper-button-next,
.swiper-button-prev {
  color: white !important;
  background-color: rgba(0, 0, 0, 0.5);
  width: 40px !important;
  height: 40px !important;
  border-radius: 50%;
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

</style>