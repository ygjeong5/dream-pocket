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
            <li><RouterLink :to="{ name: 'FinancialPostView'}">금융 뉴스</RouterLink></li>
            <li><RouterLink :to="{ name: 'FinancialPostView'}">온라인 교육</RouterLink></li>
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
  background-color: #f5f7fa;
  min-height: 100vh;
  min-width: 1000px; /* Set the minimum width */
  
}

.top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 20px;
  height: 110px;
  width: 1080;
  padding-bottom: 0;
  background: #e8f1f8;
  border-bottom: 3px solid #7fb3d5;
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
  color: #2980b9;
  font-weight: 1000;
  font-size: 16px;
  transition: background-color 0.2s ease, color 0.2s ease;
}


.logIn, .logOut {
  display: inline-block;
  font-family: 'Pretendard-Regular';
}

.logInBtn, .logOutBtn {
  border: 3px solid #7fb3d5;
  color: #2980b9;
  border-radius: 19px;
  padding: 4px 13px;
  text-align: center;
  min-width: 85px;
  background: white;
  box-shadow: 0 4px 0 #85929e;
  transition: all 0.2s ease;
}
.logInBtn:hover, .logOutBtn:hover {
  background: linear-gradient(145deg, #2980b9, #3498db);
  border: 3px solid #7fb3d5;
  color: white;
  transform: translateY(2px);
  box-shadow: 0 2px 0 #85929e;
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
}

.navContainer {
  display: flex;
  width: 1080px;
  margin: 0 auto;
  justify-content: space-between;
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

.navItem span {
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
.navItem:hover a {
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
  font-size: 15px;
  font-weight: 400;
  height: 100%;
  line-height: 4.5;
  min-width: 192px;
  transition: color 0.3s ease;
}

.navItem:hover span {
  color: #1E90FF;
  font-size: 16px;
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

@font-face{
font-family:'DNFBitBitv2';
font-style:normal;
font-weight:400;
src:url('//cdn.df.nexon.com/img/common/font/DNFBitBitv2.otf')format('opentype')}

</style>