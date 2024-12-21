<template>
  <div class="main">
    <!-- 최상단  -->
    <top/>

    <!-- Nav bar  -->
    <nav class="navbar">
      <div class="navContainer">
        <div class="navItem">
          <span>페이지 소개</span>
          <ul>
            <li><RouterLink :to="{ name: 'IntroduceView'}">DreamPocket이란?</RouterLink></li>
            <li><RouterLink :to="{ name: 'FirstStepFinanceView'}">금융의 첫걸음</RouterLink></li>
          </ul>
        </div>
        <div class="navItem">
          <span>경제 탐구하기</span>
          <ul>
            <li><RouterLink :to="{ name: 'FinancialPostView', query: { tab: 'news' }}">금융 뉴스</RouterLink></li>
            <li><RouterLink :to="{ name: 'FinancialPostView', query: { tab: 'education' }}">유튜브 교육</RouterLink></li>
          </ul>
        </div>
        <div class="navItem">
          <span>금융 어드벤처</span>
          <ul>
            <li><RouterLink :to="{ name: 'QuizInfo' }">금융 용어 사전</RouterLink></li>
            <li><RouterLink :to="{ name: 'QuizGame' }">금융 퀴즈</RouterLink></li>
            <li><RouterLink :to="{ name: 'GameView' }">금융 게임</RouterLink></li>
          </ul>
        </div>
        <div class="navItem">
          <span>실전 금융</span>
          <ul>
            <li><RouterLink :to="{ name: 'map'}">주변 은행 찾기</RouterLink></li>
            <li><RouterLink :to="{ name: 'ProductsView'}">예적금 둘러보기</RouterLink></li>
            <li><RouterLink :to="{ name: 'ProductRecommend'}">금융상품 추천받기</RouterLink></li>
            <li><RouterLink :to="{ name: 'Ledger'}">가계부 작성</RouterLink></li>
          </ul>
        </div>
        <div class="navItem">
          <span>환율 모험</span>
          <ul>
            <li>환율이란?</li>
            <li><RouterLink :to="{ name: 'RateConvertView' }">환율 계산기</RouterLink></li>
          </ul>
        </div>
        <div class="navItem">
          <span>
            <RouterLink :to="{ name: 'ArticleView'}">게시판</RouterLink>
          </span>
        </div>
      </div>
    </nav>
    
    <div class="mainContent">
      <RouterView/>
 
    </div>
    


</div>
</template>

<script setup>
  import top from '@/components/common/top.vue';
  
  import { RouterLink, RouterView } from 'vue-router';

  

</script>

<style  scoped>

.main{
  background: #e8f1f8;
  height: 100%;
  width: 100%;
  min-width: 1300px
}


.navbar {
  top: 0; 
  z-index: 1001; 
  background: linear-gradient(145deg, #e8f1f8, #d4e6f1);
  width: 100%;
  min-width: 1000px;
  border: none;
  border-bottom: 3px solid #7fb3d5;
  height: 70px;
  padding: 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
  display: flex;
  justify-content: center;
  align-items: center;
}

.navContainer {
  max-width: 1080px;
  width: 100%;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  padding: 0;
}

.navItem {
  position: relative;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 1;
  text-align: center;
}

.navItem span{
  padding: 0 50px;
  color: #34343f;
  font-family: 'DNFBitBitv2';
  font-size: 15px;
  font-weight: 400;
  height: 100%;
  line-height: 4.5;
  min-width: 192px;
  transition: color 0.3s ease;
  text-align: center;
  white-space: nowrap;
  display: inline-block;

}

.navItem ul {
  display: none;
  position: absolute;
  top: calc(100% + 6px);
  left: 50%;
  transform: translateX(-50%);
  background-color: #f8f9fa;
  list-style-type: none;
  padding: 10px 0;
  margin: 0;
  width: 192px;
  z-index: 1002;
  border: 3px solid #7fb3d5;
  border-radius: 0 0 15px 15px;
  box-shadow: 0 4px 0 #85929e;
}

.navItem ul li {
  padding: 10px 20px;
  color: #34343f;
  font-family: 'DNFBitBitv2';
  font-size: 15px;
  white-space: nowrap;
  transition: all 0.2s ease;
  text-align: center;
  width: 100%;
}

.navItem ul li a {
  color: #34343f;
  text-decoration: none;
  transition: all 0.2s ease;
  display: block;
  text-align: center;
  white-space: nowrap;
  width: 100%;
}

.navItem:hover ul {
  display: block;
}

.navContainer a {
  text-decoration: none;
  color: #34343f;
  font-family: 'DNFBitBitv2';
  font-size: 15px;
  font-weight: 400;
  transition: color 0.3s ease;
  text-align: center;
  white-space: nowrap;
}

.navItem:hover {
  border-bottom: 6px solid #10467c;
}

.navItem:hover span,
.navItem:hover a{
  /* color: #1E90FF; */
  font-size: 16px;
  transition: all 0.1s ease;
}


.mainContent {
  position: relative; /* 부모 요소에 위치 설정 */
  width: 100%;
  height: 500px; /* 높이 필수 */
  z-index: 1;
}

.mainContent::before{
    content: '';
    background-color: #f5f7fa;
    background-size: contain;
    position: absolute;
    z-index: -1;
    top: 0px;
    left: 0px;
    right: 0px;
    bottom: 0px;
    opacity: 0.8;
    height: 2000px;
  }

.navItem span{
  padding: 0 50px;
  color: #34343f;
  font-family: 'DNFBitBitv2';
  font-size: 17px;
  font-weight: 400;
  height: 100%;
  line-height: 4.5;
  min-width: 192px;
  transition: color 0.3s ease;
}

.navItem:hover span {
  color: #1E90FF;
  font-size: 18px;
  transition: color 0.1s ease, font-size 0.1s ease;
}



  
@font-face {
    font-family: 'Pretendard-Regular';
    src: url('https://fastly.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
    font-weight: auto;
    font-style: normal;
}

@font-face {
    font-family: 'Mungyeong-Gamhong-Apple';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2410-2@1.0/Mungyeong-Gamhong-Apple.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: 'yg-jalnan';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_four@1.2/JalnanOTF00.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

@font-face{
font-family:'DNFBitBitv2';
font-style:normal;
font-weight:400;
src:url('//cdn.df.nexon.com/img/common/font/DNFBitBitv2.otf')format('opentype')}


.title {
  text-align: center; /* 중앙 정렬 */
  width: 100%;
  padding: 20px 0;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  margin: 20px auto; /* 상하 여백 추가, 좌우 중앙 정렬 */
  max-width: 1080px; /* 최대 너비 설정 */
}

.navItem span {
  color: #2c3e50; /* 기본 폰트 색상 변경 */
  font-family: 'DNFBitBitv2';
  font-size: 15px;
}

.navItem:hover span {
  color: #10467c; /* 호버 시 폰트 색상 */
}

.navItem ul li {
  color: #2c3e50; /* 드롭다운 메뉴 폰트 색상 */
}

.navItem ul li:hover {
  color: #10467c; /* 드롭다운 메뉴 호버 시 폰트 색상 */
  background-color: rgba(127, 179, 213, 0.1); /* 호버 시 배경색 */
}

.navItem ul li a {
  color: inherit; /* 부모 요소의 색상 상속 */
}

</style>