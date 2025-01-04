<template>
  <div class="top">  
    <!-- 메인 로고  -->
    <article class="logo">
      <img src="@/assets/coin2.png" alt="logo">
      <RouterLink :to="{name: 'Home'}">
        <h1>DREAM POCKET</h1>
      </RouterLink>
    </article>
    
    <!-- 오른쪽 부분 -->
    <div class="buttonSet">
      <div id="beforeLogIn" v-if="!store.isLogin">
        <div class="btn signUp">
          <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
        </div> 
        <div class="logIn">
          <button type="button" class="btn logInBtn" @mouseover="changeColor" @mouseout="resetColor">
            <RouterLink :to="{ name: 'LogInView'}">로그인</RouterLink>
          </button>
        </div>
      </div>        
      
      <div id="afterLogIn" v-if="store.isLogin">
        <div class="btn ledger-btn">
          <RouterLink :to="{ name: 'Ledger' }">
            <font-awesome-icon :icon="['fas', 'piggy-bank']" size="xl"/>
            <text>가계부</text>
          </RouterLink>
        </div>
        
        <div class="btn profile-btn">
          <RouterLink :to="{ name: 'ProfileView' }">
            <font-awesome-icon :icon="['fas', 'fa-user']" size="xl"/>
            프로필
          </RouterLink>
        </div>
        <div class='btn logOut'>
          <form @submit.prevent="logOut" class='logOutBtn'>
            <input type="submit" value="Logout">
          </form>  
        </div>
      </div>  
    </div>

  </div>   
</template>

<script setup>
  import { useEggStore } from '@/stores/egg';
import { icon } from '@fortawesome/fontawesome-svg-core';
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

<style scoped>
.top {
  height: 110px;
  width: 100%;
  padding: 0;
  background: #e8f1f8;
  border-bottom: 3px solid #7fb3d5;
  display: flex;
  align-items: center;
  text-align: center;
  position: relative;
}

/* 로고 =================================================== */
.logo {
  height: 100%;
  width: 100%; 
  margin-bottom: 0;
  display: flex; 
  align-items: center;
  justify-content: center; 
}

.logo a {
  text-decoration-line: none;
  position: relative; 
}

.logo h1 {
  width: 170px; 
  margin: 0;
  font-size: 20px;
  font-family: 'DNFBitBitv2', sans-serif;
  background: linear-gradient(to left top, #81aef6, #41eb2e);
  -webkit-text-stroke: 2px rgba(39, 54, 154, 0.726);
  -webkit-background-clip: text;
  color: transparent;
  letter-spacing: 0.04rem;
  line-height: 1.1; /* 텍스트 줄 간격 조정 */
  z-index: 1;
}

.logo img{
  width: 160px; /* 이미지 크기 조정 */
  opacity: 25%;
  position: absolute; /* 절대 위치 설정 */
  top: -3%;
}


/* 상단 오른쪽 버튼셋 ======================================= */
.buttonSet {
  height: 40px;
  bottom: 10%;
  right: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
}

/* 공통 버튼 스타일 =========================================*/
.btn {
  width: 90px;
  height: 40px;
  padding: 0;
  margin-right: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 25px;
  background-color: white;
  position: relative;
  overflow: hidden;
}

/* 버튼 내 텍스트 크기 조정 */
.btn a{
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'yg-jalnan';
  font-size: 13px;  /* 폰트 크기 축소 */
  text-decoration-line: none;
  z-index: 1;  /* 텍스트를 배경 위에 보이도록 */
}

/* 버튼 내 텍스트 세부 위치 조절  */
.btn text {
  display:inline-block;
  transform: translateY(7%);
}

/* 로그인 후 ============================================ */
#afterLogIn {
  display: flex;
  align-items: center;
}


/* 가계부 버튼 =========================================== */
.ledger-btn {
  border: 2px solid #FFB5E8;
}

/* 저금통 아이콘 크기 조정 */
.fa-piggy-bank  {
  font-size: 16px ;  /* 아이콘 크기 축소 */
  margin: 3px;
}

.ledger-btn a {
  color: #FFB5E8;
}

.ledger-btn:hover {
  transform: scale(1.05) rotate(2deg);  /* 살짝 회전하면서 커지는 효과 */
  background-color: #FFF0F7;
  box-shadow: 0 4px 12px rgba(255, 181, 232, 0.4);
  border-color: #FF9AE3;
}

/* 호버 시 아이콘 애니메이션 */
.ledger-btn:hover .fa-piggy-bank {
  font-size: 17px;
  transform: rotate(-15deg) scale(1.2);  /* 아이콘만 따로 회전 */
  animation: wiggle 1s ease infinite;    /* 흔들거리는 애니메이션 */
}

.ledger-btn a:hover {
  color: #f341c0;
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

/* 흔들거리는 애니메이션 키프레임 */
@keyframes wiggle {
  0% { transform: rotate(-15deg); }
  25% { transform: rotate(-5deg); }
  50% { transform: rotate(-15deg); }
  75% { transform: rotate(-5deg); }
  100% { transform: rotate(-15deg); }
}

/* 프로필 버튼 ========================================= */

.profile-btn {
  border: 2px solid #A5D8FF;  /* 하늘색 계열 */
}

.profile-btn a {
  color: #A5D8FF;
}

/* 저금통 아이콘 크기 조정 */
.fa-user  {
  font-size: 16px ;  /* 아이콘 크기 축소 */
  margin: 3px;
}

.profile-btn:hover {
  transform: scale(1.05) rotate(1deg);  /* 반대 방향으로 회전 */
  background-color: #EDF5FF;
  box-shadow: 0 4px 12px rgba(165, 216, 255, 0.4);
  border-color: #74C0FC;
}

.profile-btn a:hover {
  color: #5fb4f4;
}

.profile-btn:hover .fa-user {
  font-size: 17px;
  transform: rotate(-15deg) scale(1.2);  /* 아이콘만 따로 회전 */
  animation: wiggle 1s ease infinite;    /* 흔들거리는 애니메이션 */
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

/* 로그인 버튼 ============================ */


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



#beforeLogIn {
  display: flex;
  align-items: center;
  gap: 20px;
  height: 40px;
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




</style>