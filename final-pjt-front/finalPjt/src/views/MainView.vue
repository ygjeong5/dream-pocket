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
  <div class="youtube">
    <swiper
    :slidesPerView="6"
    :spaceBetween="30"
    :loop="true"
    :pagination="{
      clickable: true,
    }"
    :navigation="true"
    :modules="modules"
    class="mySwiper"
  > 
  <swiper-slide>Slide 1</swiper-slide>
    <swiper-slide>Slide 2</swiper-slide><swiper-slide>Slide 3</swiper-slide>
    <swiper-slide>Slide 4</swiper-slide><swiper-slide>Slide 5</swiper-slide>
    <swiper-slide>Slide 6</swiper-slide><swiper-slide>Slide 7</swiper-slide>
    <swiper-slide>Slide 8</swiper-slide><swiper-slide>Slide 9</swiper-slide>
  </swiper>


  </div>
  <div>chatbot</div>
  <div class="mainContent">
    
    <div class="chatbot">
      chatbot
    </div>
    <div class="mypage">
      mypage
    </div>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';

  // Import Swiper styles
  import 'swiper/css';

  import 'swiper/css/pagination';
  import 'swiper/css/navigation';

  // import required modules
  import { Pagination, Navigation } from 'swiper/modules';

  export default {
    components: {
      Swiper,
      SwiperSlide,
    },
    setup() {
      return {
        modules: [Pagination, Navigation],
      };
    },
  };
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

.youtube{
  border: 1px black solid;
  height: 300px;
  max-height: 300px;
  margin: 0 5%;
  background-color: rgb(61, 61, 63);
  padding: 20px;
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
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;

  /* Center slide text vertically */
  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.swiper {
  margin-left: auto;
  margin-right: auto;
}

</style>