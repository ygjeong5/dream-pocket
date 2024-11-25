<template>
  <div class="mainPage">
    <!-- 최상단  -->
    <div class="top"> 
      <div class="topContent">
        <!-- 메인 로고  -->
        <div class="topMiddle">
          
          <div class="logo">
            <img src="@/assets/coin.png" alt="">
            <h1>
              DREAM POCKET</h1>
          </div>
        </div>
  

        
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
        <div class="navLeftItem">
          <div class="navItem">
            <RouterLink :to="{ name: 'ArticleView'}">Articles</RouterLink>
          </div>
          <div class="navItem">
            <RouterLink :to="{ name: 'LicenseView'}">라이센스</RouterLink>
          </div>
          <div class="navItem">
            <RouterLink :to="{ name: 'RateConvertView' }">환율 계산</RouterLink>
          </div>
          <div>
            <RouterLink :to="{ name:'ProductsView'}">금융 상품 리스트</RouterLink>
          </div>
        </div>
        
        <div class="mainLogo navItem">
          <RouterLink :to="{name: 'Home'}">Home</RouterLink>
        </div>
            
        <div>
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
  </div>

  <!-- 챗봇 버튼 및 창 추가 -->
  <div class="chat-view">
  <div class="chat-window">
    <div class="chat-header">
      <span>금융 상담사</span>
    </div>
    <ChatBot />
    </div>
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

  const changeColor = function(event) {
    const a = event.currentTarget.querySelector('a')
    a.style.color = 'white'
  }
  
  const resetColor = function(event){
        const a = event.currentTarget.querySelector('a')
    a.style.color = 'black'
  }

  const isChatOpen = ref(false)

  const toggleChat = () => {
  isChatOpen.value = !isChatOpen.value
}
  
</script>

<style  scoped>


.mainPage{
  background-color: rgb(247, 253, 254);
  min-height: 100vh;
}

.top {
  display: flex;
  justify-content: space-between;
  padding: 12px 20px;
  align-items: center;
}

.topContent{
  display: inline-block;
  height: 60px;
  width: 100%;
  vertical-align: text-top;
  text-align: center;
  margin-right: 60px;
}

.topMiddle {
  width: 100%; /* 전체 폭 사용 */
  display: flex; /* 가운데 정렬을 위한 flex 사용 */
  align-items: center;
  justify-content: center; /* 중앙 정렬 */
}

.logo{
  display: flex; /* 플렉스 사용 */
  position: relative;
  width: 230px;
  align-items: center; /* 세로 정렬 */
  justify-content: center; /* 가로 정렬 */
}

.topMiddle h1 {
  width: 130px;
  font-size: 23px;
  font-family: 'DNFBitBitv2', sans-serif;
  margin-left: 50px;
  -webkit-text-stroke: 2px rgba(39, 54, 154, 0.726);
  letter-spacing: .01rem;
  background: linear-gradient(to left top, #81aef6, #41eb2e);
  -webkit-background-clip: text;
  color: transparent;
}

.topMiddle img{
  position: absolute;
  width: 60px; /* SVG 크기 */
  left: 35px;
  height: 70px;
  margin-right: 0px;
  margin-bottom: 12px;
  padding-bottom: 10px;
}


.topRight {
  position: absolute;
  top: 0;
  right: 0;
  padding-right: 5px;
}

.signUp, .profile {
  display: inline-block;
  margin-right: 5px;
  font-family: 'Pretendard-Regular';
  font-weight: 500;
}

.signUp a {
  color: black;
  text-decoration-line: none;
}

.signUp a:hover {
  color: #1E90FF
}

.logIn, .logOut {
  display: inline-block;
  padding: 11px 9px 0;
  margin-right: 8px;
}

.logInBtn, .logOutBtn {
  border: 2px solid black;
  border-radius: 19px;
  padding: 6px 18px;
  text-align: center;
  min-width: 85px;
  
}

.logInBtn:hover, .logOutBtn:hover {
  background-color : #1E90FF;
  border: 1px solid #1E90FF
}


.logInBtn a, .logOutBtn a {
  color: black;
  text-decoration-line: none;
  font-family: 'Pretendard-Regular';
  font-weight: 600;
}

.navbar {
  position: absolute;
  z-index: 1001; 
  background: linear-gradient(to right, #ffffff, #f8f9fa);
  border-radius: 10px;
  min-width: 100%;
  height: 61px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05); 
}

.navContainer {
  padding: 0 .625rem;
  width: 100%;
  display: grid;
  grid-template-columns: 1fr auto 1fr; /* 왼쪽, 가운데(Home), 오른쪽 */
  align-items: center; 
}

.navContainer a {
  padding: 0 25px;
  color: black;
  text-decoration-line: none;
  font-family: 'Pretendard-Regular';
  font-weight: 600;
  margin: 0;
}

.navItem:hover {
  border-bottom: 2px solid rgb(19, 54, 229);
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
  margin-top: 68px;
}
  
@font-face {
    font-family: 'Pretendard-Regular';
    src: url('https://fastly.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
    font-weight: 400;
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
font-style:normal;font-weight:400;src:url('//cdn.df.nexon.com/img/common/font/DNFBitBitv2.otf')format('opentype')}


</style>