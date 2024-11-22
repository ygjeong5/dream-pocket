<template>
  <div>
    <!-- 최상단  -->
    <div class="top"> 
      <div class="topContent">
       
        <div class="topMiddle">
          베너 넣을 예정
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

</div>
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router';
  import { useEggStore } from './stores/egg';

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
  
</script>

<style  scoped>

.top {
  position: relative;
  z-index: 1000;
}

.topContent{
  display: inline-block;
  height: 60px;
  width: 100%;
  vertical-align: text-top;
  text-align: center;
}

.topMiddle {
  margin-top: 3px;
  width: 200px;
  height: 50px;
  border: 1px solid black;
  display: inline-block;
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
  min-width: 100%; 
  height: 61px;
  background-color: white;
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



</style>