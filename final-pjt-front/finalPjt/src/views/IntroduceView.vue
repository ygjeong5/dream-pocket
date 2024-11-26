<template>
  <div class="introduce-container">
    <section class="intro-header">
      <h1>Dream Pocket이란?</h1>
      <p class="intro-description">
        Dream Pocket은 금융 기초부터 실생활 활용까지 배울 수 있는<br>
        <span class="highlight">금융 교육 플랫폼</span>입니다.<br>
        여러분의 목표를 이루기 위해 금융을 쉽고 재미있게 알려드려요!
      </p>
    </section>

    <div class="content-sections">
      <section class="info-section">
        <div class="section-header">
          <h2>Dream Pocket에서 무엇을 배울 수 있나요?</h2>
        </div>
        <div class="feature-grid">
          <div class="feature-item">
            <span class="feature-icon">📚</span>
            <h3>경제의 기초 이해</h3>
            <p>용돈 관리부터 시작하는 금융 기초 배우기</p>
          </div>
          <div class="feature-item">
            <span class="feature-icon">🎯</span>
            <h3>목표 기반 플랜 설계</h3>
            <p>여행, 자취, 첫 차 구입 등 목표를 위한 맞춤 금융 계획</p>
          </div>
          <div class="feature-item">
            <span class="feature-icon">✍️</span>
            <h3>실습형 학습</h3>
            <p>가계부 작성, 적금 플랜 설계 등 직접 체험하며 배우기</p>
          </div>
          <div class="feature-item">
            <span class="feature-icon">🌏</span>
            <h3>환율과 경제 흐름</h3>
            <p>글로벌 경제를 이해하는 첫걸음!</p>
          </div>
        </div>
      </section>

      <section class="info-section">
        <div class="section-header">
          <h2>배우는 방식</h2>
        </div>
        <div class="section-content">
          <ul class="learning-list">
            <li>
              <span class="list-icon">🎮</span>
              <div class="list-content">
                <strong>퀘스트 시스템</strong>
                <p>금융 미션을 하나씩 해결하며 실력 업!</p>
              </div>
            </li>
            <li>
              <span class="list-icon">📖</span>
              <div class="list-content">
                <strong>쉽고 간단한 콘텐츠</strong>
                <p>어려운 개념도 그림과 스토리로 쉽게 이해</p>
              </div>
            </li>
            <li>
              <span class="list-icon">🏆</span>
              <div class="list-content">
                <strong>보상 기반 학습</strong>
                <p>목표를 달성하면 포인트와 보상을 받을 수 있어요</p>
              </div>
            </li>
          </ul>
        </div>
      </section>

      <section class="info-section">
        <div class="section-header">
          <h2>왜 Dream Pocket인가요?</h2>
        </div>
        <div class="section-content">
          <div class="why-grid">
            <div class="why-item">
              <span class="why-icon">🌟</span>
              <h3>쉽고 재미있게</h3>
              <p>게임처럼 배우고, 바로 써먹는 금융 교육</p>
            </div>
            <div class="why-item">
              <span class="why-icon">🎓</span>
              <h3>성장 중심</h3>
              <p>단순한 정보 제공이 아닌, 여러분의 성장을 돕는 시스템</p>
            </div>
            <div class="why-item">
              <span class="why-icon">🤝</span>
              <h3>함께 배우기</h3>
              <p>커뮤니티에서 친구들과 협력하고 경험 공유</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
// 추가 스크립가 필요하면 여기에 작성합니다.
</script>

<style scoped>
.introduce-container {
  max-width: 1200px;
  min-width: 1000px;
  margin: 0 auto;
  padding: 2rem;
  background: 
    linear-gradient(120deg, 
      #ffffff 0%,
      rgba(242, 94, 134, 0.02) 25%,  /* 더 연한 핑크 */
      rgba(136, 201, 242, 0.03) 50%, /* 더 연한 하늘 */
      rgba(156, 217, 95, 0.02) 75%,  /* 더 연한 라임 */
      #ffffff 100%
    );
  border-radius: 20px;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.05);
  position: relative;
}

/* 배경 패턴 제거하고 더 단순하게 수정 */
.introduce-container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    linear-gradient(
      -45deg,
      transparent 0%,
      rgba(242, 183, 5, 0.01) 50%,
      transparent 100%
    );
}

.intro-header {
  background: linear-gradient(145deg, #F25E86, #F29F05);
  padding: 2.5rem;
  border-radius: 20px;
  box-shadow: 0 6px 0 #F25E86, 0 10px 20px rgba(0,0,0,0.2);
  border: 4px solid #F2B705;
  margin-bottom: 2rem;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.intro-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg, transparent 45%, rgba(255,255,255,0.1) 50%, transparent 55%);
  animation: shine 3s infinite;
}

@keyframes shine {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

.intro-header h1 {
  font-family: 'DNFBitBitv2';
  font-size: 3rem;
  margin: 0 0 1rem 0;
  color: white;
  text-shadow: 3px 3px 0 #F25E86;
  letter-spacing: 2px;
}

.intro-description {
  font-family: 'DNFBitBitv2';
  font-size: 1.3rem;
  color: #fff;
  line-height: 1.8;
  margin: 0;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
}

.highlight {
  color: #F2B705;
  font-weight: bold;
  font-size: 1.4rem;
  text-shadow: 1px 1px 0 rgba(0,0,0,0.2);
}

.info-section {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  border: 4px solid #88C9F2;
  box-shadow: 0 8px 0 #F25E86;
  overflow: hidden;
  margin-bottom: 2rem;
  transition: all 0.3s ease;
  position: relative;
}

.info-section:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 0 #F25E86, 
              0 14px 24px rgba(0,0,0,0.15);
  border-color: #F2B705;
}

.section-header {
  background: linear-gradient(145deg, #88C9F2, #9CD95F);
  padding: 1.2rem 1.5rem;
  border-bottom: 4px solid #F2B705;
}

.section-header h2 {
  font-family: 'DNFBitBitv2';
  font-size: 1.8rem;
  color: white;
  margin: 0;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.2);
}

.feature-item, .why-item {
  background: linear-gradient(145deg, #fff, #f8f9fa);
  padding: 2rem;
  border-radius: 15px;
  text-align: center;
  border: 3px solid #88C9F2;
  box-shadow: 0 4px 0 #F25E86;
  transition: all 0.3s ease;
  position: relative;
}

.feature-item:hover, .why-item:hover {
  transform: translateY(-4px) scale(1.02);
  border-color: #F2B705;
  box-shadow: 0 8px 0 #F25E86, 
              0 10px 20px rgba(0,0,0,0.1);
}

.feature-icon, .why-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  display: block;
  filter: drop-shadow(2px 2px 0 rgba(0,0,0,0.1));
  background: linear-gradient(145deg, #9CD95F, #88C9F2);
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
  border: 2px solid #F2B705;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.learning-list li {
  background: linear-gradient(145deg, #fff, #f8f9fa);
  margin-bottom: 1rem;
  padding: 1.2rem;
  border-radius: 12px;
  border: 3px solid #88C9F2;
  box-shadow: 0 4px 0 #F25E86;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
}

.learning-list li:hover {
  transform: translateX(10px);
  border-color: #F2B705;
}

.list-content strong {
  font-family: 'DNFBitBitv2';
  color: #F25E86;
  font-size: 1.2rem;
  text-shadow: 1px 1px 0 rgba(0,0,0,0.1);
}

h3 {
  font-family: 'DNFBitBitv2';
  color: #34343f;
  font-size: 1.4rem;
  margin: 0.5rem 0;
  text-shadow: 1px 1px 0 rgba(0,0,0,0.1);
}

p {
  font-family: 'DNFBitBitv2';
  color: #666;
  margin: 0;
  line-height: 1.4;
  font-size: 1.1rem;
}

/* 추가 애니메이션 효과 */
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
  100% { transform: translateY(0px); }
}

.feature-icon, .why-icon {
  animation: float 3s ease-in-out infinite;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  padding: 1.5rem;
}

.feature-item {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 12px;
  text-align: center;
  border: 2px solid #7fb3d5;
  transition: all 0.3s ease;
}

.feature-item:hover {
  transform: translateY(-2px);
  border-color: #2980b9;
}

.feature-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
  display: block;
}

.learning-list li {
  display: flex;
  align-items: center;
  padding: 1rem 0;
  border-bottom: 1px solid #e8f1f8;
}

.learning-list li:last-child {
  border-bottom: none;
}

.list-icon {
  font-size: 1.5rem;
  margin-right: 1rem;
}

.list-content strong {
  font-family: 'DNFBitBitv2';
  color: #1E90FF;
  display: block;
  margin-bottom: 0.3rem;
}

.why-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.why-item {
  text-align: center;
  padding: 1.5rem;
  background: #f8f9fa;
  border-radius: 12px;
  border: 2px solid #7fb3d5;
  transition: all 0.3s ease;
}

.why-item:hover {
  transform: translateY(-2px);
  border-color: #2980b9;
}

.why-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
  display: block;
}

h3 {
  font-family: 'DNFBitBitv2';
  color: #34343f;
  margin: 0.5rem 0;
}

p {
  font-family: 'DNFBitBitv2';
  color: #666;
  margin: 0;
  line-height: 1.4;
}

@font-face {
  font-family: 'DNFBitBitv2';
  font-style: normal;
  font-weight: 400;
  src: url('//cdn.df.nexon.com/img/common/font/DNFBitBitv2.otf') format('opentype');
}
</style>
