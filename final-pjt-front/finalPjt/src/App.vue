<template>
  <div>
    <div class="top"> 
      <div class="topMiddle">
        베너 넣을 예정
      </div>
      
      <div class="topRight">
        <div>
          <RouterLink :to="{ name: 'ProfileView' }">회원정보</RouterLink>
        </div>
        <div class="signUp">
          <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
        </div>
        <div class="logIn">
          <button type="button" class="loginBtn">
            <RouterLink :to="{ name: 'LogInView'}">로그인</RouterLink>
          </button>
        </div>
      </div>   
    
    </div>

    <!-- Nav bar  -->
    <nav class="navbar navbar-expand-lg">
  <div class="container-fluid">
    <RouterLink :to="{ name: 'ArticleView'}">Articles</RouterLink>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <RouterLink :to="{ name: 'LicenseView'}">라이센스</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{ name: 'RateConvertView' }">환율 계산</RouterLink>
        </li>
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
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>











 
    <span> | </span>

  </div>
  <RouterView/>
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router';
</script>

<style  scoped>

.top {
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

.signUp {
  display: inline-block;
  margin-right: 5px;
  font-family: 'Pretendard-Regular';
  font-weight: 500;
}

.signUp a {
  color: black;
  text-decoration-line: none;
}

.logIn {
  display: inline-block;
  padding: 11px 9px 0;
  margin-right: 8px;
}

.loginBtn {
  border: 2px solid black;
  border-radius: 19px;
  padding: 6px 18px;
  text-align: center;
  min-width: 85px;
  
}

.loginBtn a {
  color: black;
  text-decoration-line: none;
  font-family: 'Pretendard-Regular';
  font-weight: 600;
}








.navbar {
  height: 61px;
  background-color: #e3f2fd ;
  border: 1px solid black;
}
  
@font-face {
    font-family: 'Pretendard-Regular';
    src: url('https://fastly.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
    font-weight: 400;
    font-style: normal;
}


</style>