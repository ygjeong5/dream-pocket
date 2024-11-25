<template>
  <div calss="mainPage">
    <!-- card -->
    <div id="carousel" class="carousel slide" data-bs-ride="carousel">
      <!-- 하단 버튼 -->
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      
    <div class="carousel-inner">
      <div class="carousel-item active " data-bs-interval="8000">
        <img src="@/assets/mainbanner1.png" alt="mainbanner">
      </div>

      <div class="carousel-item" data-bs-interval="8000">
        <img src="@/assets/mainbanner2.png"  alt="mainbanner">
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
  <div>chatbot</div>
  <div class="mainContent">
    
    <div class="chatbot">
      chatbot
    </div>
    <div class="mypage">
      mypage
    </div>
  </div>
  <div class="youtube">
    youtube
  </div>
</template>

<script setup>

</script>

<style scoped>

.mainPage {
  background-color: #f8f9fa;
}

.carousel {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  /* border-radius: 8px; */
  overflow: hidden;
  /* margin: 20px auto; */
  /* max-width: 1400px; */
}

.carousel-inner > .carousel-item {
  text-align: center;

}

.carousel-item, .carousel-item > img {
  height: 500px;
  min-width: 80%;
  object-fit: cover;
}

.custom-indicator {
  width: 12px !important;
  height: 12px !important;
  border-radius: 50% !important;
  background-color: rgba(255, 255, 255, 0.5) !important;
  border: none !important;
  margin: 0 6px !important;
}

.custom-indicator.active {
  background-color: #ffffff !important;
  transform: scale(1.2);
  transition: all 0.3s ease;
}

/* 네비게이션 버튼 스타일 */
.custom-carousel-control {
  width: 5%;
  background: linear-gradient(90deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0) 100%);
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

.youtube{
  border: 1px black solid;
  height: 300px;
}
</style>