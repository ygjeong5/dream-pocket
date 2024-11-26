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
            <div class="ledger-btn">
              <RouterLink :to="{ name: 'Ledger' }">
                <font-awesome-icon :icon="['fas', 'piggy-bank']" size="xl"/>
                가계부
              </RouterLink>
            </div>
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
  import { RouterLink, RouterView } from 'vue-router';
  import { useEggStore } from './stores/egg';
  import { ref } from 'vue';

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
  min-width: 1500px /* Set the minimum width */
  
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
  /* margin-right: 60px; */
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
  align-items: center; /* 텍스트를 세로 가운데 렬 */
  justify-content: center; /* 수평 가운데 정렬 */
  position: relative; /* img의 절대 위치를 기준으로 할 부모 요소 */
}

.topMiddle h1 {
  width: 170px; /* 고정 너비 설정 */
  font-size: 24px;
  text-align: center;
  font-family: 'DNFBitBitv2', sans-serif;
  margin-left: 0; /* 여백 제거 */
  margin: 0;
  -webkit-text-stroke: 2px rgba(39, 54, 154, 0.726);
  letter-spacing: 0.04rem;
  background: linear-gradient(to left top, #81aef6, #41eb2e);
  -webkit-background-clip: text;
  color: transparent;

  text-align: center; /* 텍스트 정렬을 왼쪽으로 */
  line-height: 1.1; /* 텍스트 줄 간격 조정 */
}


.topMiddle img{
  width: 52px; /* 이미지 크기 조정 */
  height: auto; /* 비율 유지 */
  position: absolute; /* 절대 위치 설정 */
  left: -11%; /* 부모의 왼쪽에 배치 */
  top: 37%; /* 세로 중앙 정렬 */
  transform: translateY(-50%);
}

.topRight {
  display: flex;
  position: absolute;
  top: 20px;
  right: 5%;
  justify-content: center;
  align-items: center;
}

.signUp, .profile, .ledger-btn {
  display: inline-block;
  font-family: 'yg-jalnan';
  font-size: 15px;
  margin-right: 5px;
}

.signUp a, .profile a, .ledger-btn a {
  color: #3470d0;
  text-decoration-line: none;
  transition: all 0.2s ease;
}

.signUp a:hover, .profile a:hover, .ledger-btn a:hover {
  color: #2563eb;
  transform: translateY(-2px);
}

.logInBtn, .logOutBtn {
  border-radius: 25px;
  padding: 8px 16px;
  text-align: center;
  width: 100px;
  height: 40px;
  background: white;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.logInBtn {
  border: 2px solid #3b82f6;
  color: #3b82f6;
  box-shadow: 0 4px 0 #3b82f640;
}

.logInBtn:hover {
  transform: scale(1.05) rotate(1deg);
  background: linear-gradient(145deg, #3b82f6, #2563eb);
  border-color: #2563eb;
  box-shadow: 0 6px 12px rgba(59, 130, 246, 0.3);
}

.logInBtn a {
  color: #3b82f6;
  text-decoration-line: none;
  font-family: 'yg-jalnan';
  font-size: 15px;
  z-index: 1;
}

.logInBtn:hover a {
  color: white;
}

.logOutBtn {
  border: 2px solid #06b6d4;
  box-shadow: 0 4px 0 #06b6d440;
}

.logOutBtn:hover {
  transform: scale(1.05) rotate(-1deg);
  background: linear-gradient(145deg, #06b6d4, #0891b2);
  border-color: #0891b2;
  box-shadow: 0 6px 12px rgba(6, 182, 212, 0.3);
}

.logOutBtn input {
  background: none;
  border: none;
  color: #06b6d4;
  font-family: 'yg-jalnan';
  font-size: 15px;
  cursor: pointer;
  padding: 0;
  z-index: 1;
}

.logOutBtn:hover input {
  color: white;
}

.logInBtn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent,
    rgba(59, 130, 246, 0.2),
    transparent
  );
  transition: 0.5s;
}

.logInBtn:hover::before {
  left: 100%;
}

.logOutBtn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent,
    rgba(6, 182, 212, 0.2),
    transparent
  );
  transition: 0.5s;
}

.logOutBtn:hover::before {
  left: 100%;
}

#afterLogIn, #beforeLogIn {
  display: flex;
  align-items: center;
  gap: 15px;
  height: 40px;
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

.ledger-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 15px;
  font-family: 'Pretendard-Regular';
  font-size: 15px;
  font-weight: 600;
  padding: 8px 16px;
  border-radius: 25px;
  transition: all 0.3s ease;
  background-color: white;
  border: 2px solid #FFB5E8;
  position: relative;  /* 애니메이션을 위한 position 설정 */
  overflow: hidden;    /* 애니메이션 효과가 버튼 밖으로 넘치지 않도록 */
}

.ledger-btn a {
  color: #FFB5E8;
  text-decoration-line: none;
  display: flex;
  align-items: center;
  gap: 8px;
  z-index: 1;  /* 텍스트를 배경 위에 보이도록 */
}

.ledger-btn:hover {
  transform: scale(1.05) rotate(2deg);  /* 살짝 회전하면서 커지는 효과 */
  background-color: #FFF0F7;
  box-shadow: 0 4px 12px rgba(255, 181, 232, 0.4);
  border-color: #FF9AE3;
}

.ledger-btn a:hover {
  color: #FF9AE3;
}

/* FontAwesome 아이콘 스타일링 */
.ledger-btn .fa-piggy-bank {
  font-size: 20px !important;
  transition: all 0.3s ease;
}

/* 호버 시 아이콘 애니메이션 */
.ledger-btn:hover .fa-piggy-bank {
  transform: rotate(-15deg) scale(1.2);  /* 아이콘만 따로 회전 */
  animation: wiggle 1s ease infinite;    /* 흔들거리는 애니메이션 */
}

/* 텍스트 스타일링 */
.ledger-btn span {
  font-family: 'yg-jalnan';
  font-size: 15px;
}

/* 흔들거리는 애니메이션 키프레임 */
@keyframes wiggle {
  0% { transform: rotate(-15deg); }
  25% { transform: rotate(-5deg); }
  50% { transform: rotate(-15deg); }
  75% { transform: rotate(-5deg); }
  100% { transform: rotate(-15deg); }
}

/* 배경 효과 애니메이션 */
.ledger-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent,
    rgba(255, 181, 232, 0.2),
    transparent
  );
  transition: 0.5s;
}

.ledger-btn:hover::before {
  left: 100%;
}

#afterLogIn {
  display: flex;
  align-items: center;
  gap: 20px;
  height: 40px;
}

#beforeLogIn {
  display: flex;
  align-items: center;
  gap: 20px;
  height: 40px;
}

.profile {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 15px;
  font-family: 'Pretendard-Regular';
  font-size: 15px;
  font-weight: 600;
  padding: 8px 16px;
  border-radius: 25px;
  transition: all 0.3s ease;
  background-color: white;
  border: 2px solid #A5D8FF;  /* 하늘색 계열 */
  position: relative;
  overflow: hidden;
}

.profile a {
  color: #A5D8FF;
  text-decoration-line: none;
  display: flex;
  align-items: center;
  gap: 8px;
  z-index: 1;
  font-family: 'yg-jalnan';
  font-size: 15px;
}

.profile:hover {
  transform: scale(1.05) rotate(-2deg);  /* 반대 방향으로 회전 */
  background-color: #EDF5FF;
  box-shadow: 0 4px 12px rgba(165, 216, 255, 0.4);
  border-color: #74C0FC;
}

.profile a:hover {
  color: #74C0FC;
}

/* 배경 효과 애니메이션 */
.profile::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent,
    rgba(165, 216, 255, 0.2),
    transparent
  );
  transition: 0.5s;
}

.profile:hover::before {
  left: 100%;
}

/* afterLogIn 컨테이너 정렬 조정 */
#afterLogIn {
  display: flex;
  align-items: center;
  gap: 20px;
  height: 40px;
}

/* 모든 버튼의 너비를 통일 */
.profile, .ledger-btn, .logOutBtn {
  min-width: 100px;  /* 최소 너비 설정 */
  text-align: center;
  margin-right: 5px;
}

/* 회원가입 버튼 스타일 */
.signUp {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 15px;
  font-family: 'Pretendard-Regular';
  font-size: 15px;
  font-weight: 600;
  padding: 8px 16px;
  border-radius: 25px;
  transition: all 0.3s ease;
  background-color: white;
  border: 2px solid #4ADE80;  /* 밝은 초록색 */
  position: relative;
  overflow: hidden;
  width: 100px;
  height: 40px;
  margin-right: 5px;
}

.signUp a {
  color: #4ADE80;
  text-decoration-line: none;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  z-index: 1;
  font-family: 'yg-jalnan';
  font-size: 15px;
}

.signUp:hover {
  transform: scale(1.05) rotate(1deg);
  background-color: #F0FDF4;
  box-shadow: 0 4px 12px rgba(74, 222, 128, 0.4);
  border-color: #22C55E;
}

.signUp a:hover {
  color: #22C55E;
}

/* 반짝이는 효과 애니메이션 - 회원가입 버튼 */
.signUp::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent,
    rgba(74, 222, 128, 0.2),
    transparent
  );
  transition: 0.5s;
}

.signUp:hover::before {
  left: 100%;
}

/* 모든 버튼의 너비를 통일 */
.signUp, .profile, .ledger-btn, .logOutBtn, .logInBtn {
  min-width: 80px;  /* 너비 축소 */
  height: 35px;    /* 높이 축소 */
  padding: 6px 12px;  /* 패딩 축소 */
}

/* 버튼 내 텍스트 크기 조정 */
.signUp a, .profile a, .ledger-btn a, .logOutBtn input, .logInBtn a {
  font-size: 13px;  /* 폰트 크기 축소 */
}

/* 저금통 아이콘 크기 조정 */
.ledger-btn .fa-piggy-bank {
  font-size: 16px !important;  /* 아이콘 크기 축소 */
}

/* 버튼 간격 유지 */
.topRight {
  gap: 8px;
}

/* afterLogIn, beforeLogIn 간격 조정 */
#afterLogIn, #beforeLogIn {
  gap: 8px;
  height: 35px;  /* 컨테이너 높이도 조정 */
}

/* 공통 버튼 스타일 */
.signUp, .logInBtn, .profile, .ledger-btn, .logOutBtn {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 35px;
  min-width: 80px;
  padding: 6px 12px;
  border-radius: 25px;
  background-color: white;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

/* 회원가입 버튼 */
.signUp {
  border: 2px solid #4ADE80;
}

.signUp a {
  color: #4ADE80;
  text-decoration: none;
  font-family: 'yg-jalnan';
  font-size: 13px;
  z-index: 1;
}

.signUp:hover {
  transform: scale(1.05) rotate(1deg);
  background-color: #F0FDF4;
  box-shadow: 0 4px 12px rgba(74, 222, 128, 0.4);
}

/* 로그인 버튼 */
.logInBtn {
  border: 2px solid #3b82f6;
}

.logInBtn a {
  color: #3b82f6;
  text-decoration: none;
  font-family: 'yg-jalnan';
  font-size: 13px;
  z-index: 1;
}

.logInBtn:hover {
  transform: scale(1.05) rotate(1deg);
  background-color: #EFF6FF;
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
}

/* 반짝이는 효과 - 회원가입 */
.signUp::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent,
    rgba(74, 222, 128, 0.2),
    transparent
  );
  transition: 0.5s;
}

.signUp:hover::before {
  left: 100%;
}

/* 반짝이는 효과 - 로그인 */
.logInBtn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent,
    rgba(59, 130, 246, 0.2),
    transparent
  );
  transition: 0.5s;
}

.logInBtn:hover::before {
  left: 100%;
}

/* 컨테이너 정렬 */
#beforeLogIn {
  display: flex;
  align-items: center;
  gap: 8px;
  height: 35px;
}

.topRight {
  display: flex;
  align-items: center;
  gap: 8px;
}

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