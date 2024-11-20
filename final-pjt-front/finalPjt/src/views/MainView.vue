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
</template>

<script setup>

</script>

<style scoped>

  .carousel-inner > .carousel-item {
    text-align: center;
    background-color: rgb(133, 132, 132);
  }

  .carousel-item, .carousel-item > img{
    height: 560px;
    min-width: 100%;
  }

</style>