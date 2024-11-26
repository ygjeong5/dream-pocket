<template>
  <div class="finance-education-importance">
    <header class="header">
      <h1>금융 교육과 소비 습관의 중요성</h1>
      <p>
        체계적인 금융 교육을 통해 현명한 소비 습관을 기르고,<br>
        지속 가능한 재무 관리 능력을 키워보세요.
      </p>
    </header>

    <div class="content-grid">
      <!-- 왼쪽 섹션: 금융 교육의 중요성 -->
      <section class="main-section why-important">
        <h2>금융 교육의 필요성</h2>
        <div class="info-box">
          <h3>🎯 금융 교육의 핵심 가치</h3>
          <ul>
            <li>재무적 의사결정 능력 향상</li>
            <li>장기적 자산 관리 역량 개발</li>
            <li>경제적 자립성 확보</li>
            <li>위험 관리 능력 배양</li>
          </ul>
        </div>
        
        <div class="statistics-table">
          <h3>📊 금융 교육 효과 분석</h3>
          <table>
            <thead>
              <tr>
                <th>평가 항목</th>
                <th>교육 이수자</th>
                <th>미이수자</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>월평균 저축률</td>
                <td>30% 이상</td>
                <td>15% 미만</td>
              </tr>
              <tr>
                <td>재무계획 수립률</td>
                <td>85%</td>
                <td>35%</td>
              </tr>
              <tr>
                <td>투자 다각화율</td>
                <td>75%</td>
                <td>30%</td>
              </tr>
              <tr>
                <td>재무목표 달성률</td>
                <td>67%</td>
                <td>25%</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- 오른쪽 섹션: 실천 방안 -->
      <section class="main-section education-focus">
        <h2>현명한 소비 습관 형성</h2>
        <div class="practice-steps">
          <div class="step-item">
            <span class="step-number">01</span>
            <h3>예산 수립과 지출 계획</h3>
            <p>월간 수입의 50-30-20 법칙 적용</p>
            <ul>
              <li>필수 지출: 50%</li>
              <li>여유 지출: 30%</li>
              <li>저축/투자: 20%</li>
            </ul>
          </div>
          <div class="step-item">
            <span class="step-number">02</span>
            <h3>금융상품 이해와 활용</h3>
            <p>목적별 금융상품 선택 전략</p>
            <ul>
              <li>단기 자금: 입출금/CMA</li>
              <li>중기 자금: 적금/채권</li>
              <li>장기 자금: 펀드/주식</li>
            </ul>
          </div>
          <div class="step-item">
            <span class="step-number">03</span>
            <h3>리스크 관리</h3>
            <p>위험 대비 자산 배분</p>
            <ul>
              <li>비상금 확보</li>
              <li>보험 활용</li>
              <li>분산 투자</li>
            </ul>
          </div>
        </div>
      </section>
    </div>

    <section class="call-to-action">
      <h2>지금 바로 시작하세요!</h2>
      <p>Dream Pocket과 함께 체계적인 금융 교육을 시작해보세요.</p>
      <div class="action-buttons">
        <RouterLink :to="{ name: 'FinancialPostView' }" class="action-button">
          <span class="icon">📚</span>
          경제 탐구하기
        </RouterLink>
        <RouterLink :to="{ name: 'GameView' }" class="action-button">
          <span class="icon">🎮</span>
          금융 어드벤처
        </RouterLink>
        <RouterLink :to="{ name: 'ProductsView' }" class="action-button">
          <span class="icon">💰</span>
          실전 금융
        </RouterLink>
        <RouterLink :to="{ name: 'RateConvertView' }" class="action-button">
          <span class="icon">🌏</span>
          환율 모험
        </RouterLink>
      </div>
    </section>
  </div>
</template>

<script setup>
// 필요 시 추가 동적 데이터나 설정을 작성할 수 있습니다.
</script>

<style scoped>
.finance-education-importance {
  max-width: 1200px;
  min-width: 1000px;
  margin: 0 auto;
  padding: 2rem;
  background: linear-gradient(120deg, rgba(255, 255, 255, 0.95), rgba(232, 241, 248, 0.95));
  border-radius: 20px;
  border: 1px solid rgba(127, 179, 213, 0.3);
  box-shadow: 0 0 30px rgba(127, 179, 213, 0.1);
  position: relative;
  overflow: hidden;
}

.header {
  background: linear-gradient(145deg, rgba(136, 201, 242, 0.9), rgba(156, 217, 95, 0.9));
  padding: 2.5rem;
  border-radius: 20px;
  box-shadow: 0 6px 0 rgba(136, 201, 242, 0.8);
  border: 3px solid rgba(242, 183, 5, 0.8);
  margin-bottom: 2rem;
  text-align: center;
  position: relative;
}

.header h1 {
  font-family: 'DNFBitBitv2';
  font-size: 2.5rem;
  color: white;
  margin: 0 0 1rem 0;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.2);
}

.header p {
  font-family: 'DNFBitBitv2';
  font-size: 1.2rem;
  color: white;
  line-height: 1.8;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
}

.why-important,
.education-focus,
.external-links,
.call-to-action {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  border: 3px solid #88C9F2;
  box-shadow: 0 4px 0 rgba(136, 201, 242, 0.8);
  overflow: hidden;
  margin-bottom: 2rem;
  padding: 1.5rem;
  transition: all 0.3s ease;
}

.why-important:hover,
.education-focus:hover,
.external-links:hover,
.call-to-action:hover {
  transform: translateY(-4px);
  border-color: rgba(242, 183, 5, 0.8);
}

.why-important h2,
.education-focus h2,
.external-links h2,
.call-to-action h2 {
  font-family: 'DNFBitBitv2';
  font-size: 1.8rem;
  color: #34343f;
  margin-bottom: 1.5rem;
  text-shadow: 1px 1px 0 rgba(0,0,0,0.1);
}

.statistics-table {
  background: #fff;
  border-radius: 12px;
  border: 2px solid #88C9F2;
  padding: 1rem;
  margin: 1.5rem 0;
}

.statistics-table table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
}

.statistics-table th {
  background: linear-gradient(145deg, rgba(136, 201, 242, 0.9), rgba(156, 217, 95, 0.9));
  color: white;
  padding: 1rem;
  font-family: 'DNFBitBitv2';
  text-shadow: 1px 1px 0 rgba(0,0,0,0.2);
}

.statistics-table td {
  padding: 1rem;
  border-bottom: 1px solid rgba(136, 201, 242, 0.3);
  font-family: 'DNFBitBitv2';
  color: #666;
}

.topics ul li {
  background: linear-gradient(145deg, #fff, #f8f9fa);
  margin-bottom: 1rem;
  padding: 1.2rem;
  border-radius: 12px;
  border: 2px solid #88C9F2;
  transition: all 0.3s ease;
  font-family: 'DNFBitBitv2';
}

.topics ul li:hover {
  transform: translateX(10px);
  border-color: rgba(242, 183, 5, 0.8);
}

.external-links ul li a {
  color: #1E90FF;
  font-family: 'DNFBitBitv2';
  transition: all 0.3s ease;
}

.external-links ul li a:hover {
  color: #F25E86;
}

.call-to-action {
  background: linear-gradient(145deg, #fff, #f8f9fa);
  text-align: center;
  padding: 2rem;
}

.call-to-action p {
  font-family: 'DNFBitBitv2';
  font-size: 1.2rem;
  color: #666;
  line-height: 1.6;
}

@font-face {
  font-family: 'DNFBitBitv2';
  font-style: normal;
  font-weight: 400;
  src: url('//cdn.df.nexon.com/img/common/font/DNFBitBitv2.otf') format('opentype');
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-bottom: 2rem;
}

.main-section {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  border: 3px solid #88C9F2;
  padding: 2rem;
}

.info-box {
  background: linear-gradient(145deg, #fff, #f8f9fa);
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  border: 2px solid rgba(136, 201, 242, 0.5);
}

.practice-steps {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.step-item {
  background: linear-gradient(145deg, #fff, #f8f9fa);
  border-radius: 12px;
  padding: 1.5rem;
  border: 2px solid rgba(136, 201, 242, 0.5);
  position: relative;
}

.step-number {
  position: absolute;
  top: -15px;
  left: -15px;
  background: linear-gradient(145deg, #88C9F2, #9CD95F);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  font-family: 'DNFBitBitv2';
  border: 2px solid white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.action-buttons {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  margin-top: 2rem;
}

.action-button {
  background: linear-gradient(145deg, #88C9F2, #9CD95F);
  color: white;
  padding: 1rem;
  border-radius: 12px;
  text-decoration: none;
  text-align: center;
  font-family: 'DNFBitBitv2';
  transition: all 0.3s ease;
  border: 2px solid transparent;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.action-button:hover {
  transform: translateY(-4px);
  border-color: #F2B705;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.action-button .icon {
  font-size: 2rem;
}

.statistics-table table {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.statistics-table th,
.statistics-table td {
  text-align: center;
  padding: 1rem;
}

.statistics-table th {
  background: linear-gradient(145deg, #88C9F2, #9CD95F);
  color: white;
}

.statistics-table tr:nth-child(even) {
  background: rgba(136, 201, 242, 0.1);
}
</style>
