<template>
  <div class="mainPage">
    <!-- 최상단  -->
    <div class="top"> 
      <div class="topContent">
        
        <!-- 메인 로고  -->
        <div class="topMiddle">
          <div class="logo">
            <RouterLink :to="{name: 'Home'}">
              <img src="@/assets/coin.png" alt="logo">
              <h1>DREAM POCKET</h1>
              </RouterLink>
          </div>
        </div>
       
        <!-- 오른쪽 부분 -->
        <div class="topRight">
          <div id="beforeLogIn" v-if="!store.isLogin">
            <div class="signUp">
              <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
            </div> 
            <div class="logIn">
              <button type="button" class="logInBtn" @mouseover="changeColor" @mouseout="resetColor">
                <RouterLink :to="{ name: 'LogInView'}">로그인</RouterLink>
              </button>
            </div>
          </div>        
          <div id="afterLogIn" v-if="store.isLogin">
            <div class="profile">
              <RouterLink :to="{ name: 'ProfileView' }">회원정보</RouterLink>
            </div>
            <div class='logOut'>
              <form @submit.prevent="logOut" class='logOutBtn'>
                <input type="submit" value="Logout">
              </form> 
            </div>
          </div>  
        </div>
      </div>
    </div>   

    <!-- Nav bar  -->
    <nav class="navbar">
      <div class="navContainer">
          <div class="navItem ">
            <RouterLink :to="{ name: 'ArticleView'}">Articles</RouterLink>
            <ul>
              <li>금융 뉴스</li>
              <li>온라인 교육</li>
              <li>환율이란?</li>
            </ul>
          </div>
          <div class="navItem">
            <RouterLink :to="{ name: 'LicenseView'}">라이센스</RouterLink>
            <ul>
              <li>금융 상식</li>
              <li>금융 퀴즈</li>
              <li>금융 게임</li>
            </ul>
          </div>
          <div class="navItem">
            <RouterLink :to="{ name: 'RateConvertView' }">환율 계산</RouterLink>
          </div>
          <div class="navItem">
            <RouterLink :to="{ name:'ProductsView'}">금융 상품 리스트</RouterLink>
            <ul>
              <li>예적금 리스트</li>
              <li>금융상품 추천</li>
              <li>가계부 작성</li>
            </ul>
          </div>
          <div class="navItem">
            <RouterLink :to="{ name: 'QuizGame' }">퀴즈 게임</RouterLink>
          </div>
          <div class="navItem">
            <RouterLink :to="{name: 'map'}">map</RouterLink>
          </div>
        </div>
      </nav>

  <div class="mainContent">
    <RouterView/>
    <ChatBot />
    <!-- 챗봇 버튼 및 창 추가 -->
  </div>



</div>
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router';
  import { useEggStore } from './stores/egg';
  import { ref } from 'vue';
  import ChatBot from './components/chatbot/Chatbot.vue';

  const store = useEggStore()

  const logOut = function () {
    store.logOut()
  }

  const isChatOpen = ref(false)

  const toggleChat = () => {
  isChatOpen.value = !isChatOpen.value
}
  
</script>

<style  scoped>

.mainPage{
  background-color: rgb(255, 255, 255);
  min-height: 100vh;
  min-width: 1000px; /* Set the minimum width */
  
}

.top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 20px;
  height: 100px;
  width: 1080;
  padding-bottom: 0;
}

.topContent{
  display: inline-block;
  position: relative;
  vertical-align: text-top;
  text-align: center;
  height: 60px;
  width: 100%;
  margin-right: 60px;
}

.topMiddle {
  width: 100%; /* 전체 폭 사용 */
  height: 100%;
  display: flex; /* 가운데 정렬을 위한 flex 사용 */
  align-items: center;
  margin-bottom: 0;
  justify-content: center; /* 중앙 정렬 */
}

.topMiddle a {
  text-decoration-line: none;
}

.logo{
  display: flex;
  align-items: center; /* 텍스트를 세로 가운데 정렬 */
  justify-content: center; /* 수평 가운데 정렬 */
  position: relative; /* img의 절대 위치를 기준으로 할 부모 요소 */
}

.topMiddle h1 {
  width: 170px; /* 고정 너비 설정 */
  font-size: 23px;
  text-align: center;
  font-family: 'DNFBitBitv2', sans-serif;
  margin-left: 0; /* 여백 제거 */
  margin: 0;
  -webkit-text-stroke: 2px rgba(39, 54, 154, 0.726);
  letter-spacing: 0.04rem;
  background: linear-gradient(to left top, #81aef6, #41eb2e);
  -webkit-background-clip: text;
  color: transparent;
  padding-left: 60px; /* 이미지 크기만큼 왼쪽 패딩 추가 */
  text-align: center; /* 텍스트 정렬을 왼쪽으로 */
  line-height: 1.1; /* 텍스트 줄 간격 조정 */
}

.topMiddle img{
  width: 50px; /* 이미지 크기 조정 */
  height: auto; /* 비율 유지 */
  position: absolute; /* 절대 위치 설정 */
  left: 9%; /* 부모의 왼쪽에 배치 */
  top: 38%; /* 세로 중앙 정렬 */
  transform: translateY(-50%);
}

.topRight {
  display: flex;
  position: absolute;
  top: 10px;
  right: 0;
  justify-content: center;
  margin-right: 8px;
}

.signUp, .profile {
  display: inline-block;
  margin-right: 15px;
  font-family: 'Pretendard-Regular';
  font-size: 15px;
  font-weight: 1000;
}

.signUp a, .profile a {
  color: rgb(106, 107, 121);
  text-decoration-line: none;
  
}

.signUp a:hover, .profile a:hover{
  color: #1e40ff;
  transition: background-color 0.2s ease, color 0.2s ease;
}


.logIn, .logOut {
  display: inline-block;
  font-family: 'Pretendard-Regular';
}

.logInBtn, .logOutBtn {
  border: 3px solid rgb(106, 107, 121);
  color: rgb(106, 107, 121);
  border-radius: 19px;
  padding: 4px 13px;
  text-align: center;
  min-width: 85px;
  
}
.logInBtn:hover, .logOutBtn:hover {
  background-color : #1E90FF;
  border: 3px solid #2e8ceb91;
  font-weight: 1200;
  color: white;
}


.logInBtn a, .logOutBtn a {
  color: black;
  text-decoration-line: none;
  font-family: 'Pretendard-Regular';
  font-weight: 600;
}

.navbar {
  position: sticky;
  top: 0; 
  z-index: 1001; 
  background-color: #34343f;
  width: 800px;
  min-width: 100%;
  border: 1px solid black;
  height: 70px;
  padding: 0;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
}

.navContainer {
  display: flex; /* Makes navigation items align horizontally */
  gap: 20px; /* Adds space between navigation items */
  text-align: center;
  width: 100%;
  justify-content: center; /* Centers items horizontally */
  align-items: center; /* Ensures vertical alignment */
  height: 100%; /* Ensures nav items take full height of the navbar */
}

.navItem{
  position: relative;
  padding: 0 10px;
  cursor: pointer;
  height: 100%; /* 기본 높이를 유지 */
  display: flex;
  align-items: center; /* 텍스트 수직 정렬 */
}

.navItem ul {
  display: none; /* 기본적으로 숨김 */
  position: absolute; /* 부모(navItem) 기준으로 위치 */
  top: 100%; /* 부모 아래에 위치 */
  left: 0;
  background-color: #58595be2;
  list-style-type: none; /* 리스트 스타일 제거 */
  padding: 10px 0;
  margin: 0;
  width: 100%;
  z-index: -1; /* 다른 요소 위에 표시되도록 */
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
}

.navItem ul li {
  padding: 10px 20px;
  color: #767c8b;
  font-family: 'DNFBitBitv2';
  font-size: 14px;
  white-space: nowrap; /* 긴 텍스트가 줄바꿈되지 않도록 설정 */
  transition: background-color 0.2s ease, color 0.2s ease;
}

.navItem ul li:hover {
  background-color:  #1E90FF;
  color: #fff;
}

.navItem:hover ul {
  display: block; /* 드롭다운 메뉴 표시 */
}

.navContainer a {
  display: flex;
  justify-self: center;
  padding: 0 50px;
  text-decoration: none;
  color: #767c8b;
  font-family:'DNFBitBitv2' ;
  font-size: 15px;
  font-weight: 400;
  height: 100%;
  line-height: 4.5;
  transition: color 0.3s ease, border-bottom 0.3s ease;
}

.navItem:hover {
  border-bottom: 5px solid rgb(234, 240, 247);
}

.navItem a:hover {
  color: rgb(241, 240, 238);
  font-size: 16px;
  transition: color 0.1s ease, font-size 0.1s ease;
}

.navLeftItem{
  display: flex;
  gap: 20px;
  justify-content: flex-start;
  height: 100%;
  
}

.mainLogo {
  text-align: center;
  height: 100%;
  padding: 0;
  margin: 0;
}

.mainContent {
  position: relative; /* 부모 요소에 위치 설정 */
  width: 100%;
  height: 500px; /* 높이 필수 */
  z-index: 1;
}

.mainContent::before{
    content: '';
    background-color: #e7e7eb;
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

@font-face{
font-family:'DNFBitBitv2';
font-style:normal;
font-weight:400;
src:url('//cdn.df.nexon.com/img/common/font/DNFBitBitv2.otf')format('opentype')}


</style>