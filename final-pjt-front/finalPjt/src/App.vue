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
            <RouterLink :to="{ name: 'ArticleView'}">Articles</RouterLink>
          </div>
          <div class="navItem">
            <RouterLink :to="{ name: 'LicenseView'}">라이센스</RouterLink>
          </div>
          <div class="navItem">
            <RouterLink :to="{ name: 'RateConvertView' }">환율 계산</RouterLink>
          </div>
          <div class="navItem">
            <RouterLink :to="{ name:'ProductsView'}">금융 상품 리스트</RouterLink>
          </div>
          <div class="navItem">
            <RouterLink :to="{ name: 'QuizGame' }">퀴즈 게임</RouterLink>
          </div>
          <div class="navItem">
            <RouterLink :to="{name: 'map'}">map</RouterLink>
          </div>
    

          
            <!-- 
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                </a> 
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-disabled="true">Disabled</a>
              </li>
              -->
              <!-- <form class="d-flex" role="search">
               <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
               <button class="btn btn-outline-success" type="submit">Search</button>
             </form>  -->
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
  margin: 0 200px;
}

.top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 20px;
  height: 120px;
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
  left: 8%; /* 부모의 왼쪽에 배치 */
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
  height: 60px;
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
  height: 100%;
  text-decoration: none; /* Removes underline from links */
  padding: 0 10px; /* Adds horizontal padding around text */
  display: flex;
  align-items: center; /* 자식 요소를 세로(수직) 기준으로 가운데 정렬시킴 */
  transition: color 0.3s ease, border-bottom 0.3s ease; /* Smooth hover effects */
}

.navContainer a {
  padding: 0 50px;
  text-decoration: none;
  color: #767c8b;
  font-family:'DNFBitBitv2' ;
  font-size: 15px;
  font-weight: 400;
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

/* .d-flex{
  display: flex;
  width: 10px;
  gap: 10px;
  justify-content: flex-end;
} */

.mainContent {
  border: 2px solid black;
  border-top: 0;
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