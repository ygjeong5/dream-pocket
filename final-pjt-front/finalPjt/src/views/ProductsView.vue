<template>
  <div class="products-content">
    <div class="products-header">
      <h1>금융 상품 리스트</h1>
      <div class="header-placeholder"></div>
    </div>

    <div class="products-grid">
      <div class="products-section">
        <div class="list-header">
          <h2>📋 상품 카테고리</h2>
        </div>
        
        <div class="products-list">
          <RouterLink :to="{ name:'FinancialProductsView' }" class="product-link">
            <div class="product-item">
              <div class="product-icon">💰</div>
              <div class="product-info">
                <span class="product-title">예금 상품</span>
                <span class="product-desc">안정적인 수익을 원하시나요?</span>
              </div>
            </div>
          </RouterLink>
          
          <RouterLink :to="{ name:'SavingProductsView' }" class="product-link">
            <div class="product-item">
              <div class="product-icon">🏦</div>
              <div class="product-info">
                <span class="product-title">적금 상품</span>
                <span class="product-desc">목표를 위해 저축하세요</span>
              </div>
            </div>
          </RouterLink>
          
          <RouterLink :to="{ name:'ProductComparison'}" class="product-link">
            <div class="product-item">
              <div class="product-icon">📊</div>
              <div class="product-info">
                <span class="product-title">상품 비교</span>
                <span class="product-desc">최적의 상품을 찾아보세요</span>
              </div>
            </div>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.products-content {
  max-width: 1400px;
  margin: 2rem auto;
  padding: 2rem;
  font-family: 'DNFBitBitv2';
}

.products-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  height: 80px;
}

.products-header h1 {
  font-size: 2.5rem;
    color: #2c3e50;
    margin: 0;
}

.products-section {
  background: white;
  padding: 1.5rem;
  border-radius: 20px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  max-width: 1200px;
  margin: 0 auto;
}

.list-header {
  margin-bottom: 2rem;
}

.list-header h2 {
  color: #2c3e50;
  font-size: 1.5rem;
  margin: 0;
}

.products-list {
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.product-link {
  text-decoration: none;
}

.product-item {
  display: flex;
  align-items: center;
  padding: 1.2rem;
  background: #f8f9fa;
  border-radius: 15px;
  transition: all 0.3s ease;
  border-left: 4px solid #88C9F2;
}

.product-item:hover {
  transform: translateX(5px);
  background: white;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.product-icon {
  font-size: 1.7rem;
  margin-right: 1.2rem;
  width: 45px;
  text-align: center;
}

.product-info {
  flex: 1;
}

.product-title {
  display: block;
  font-size: 1.1rem;
  color: #2c3e50;
  margin-bottom: 0.3rem;
}

.product-desc {
  display: block;
  font-size: 0.9rem;
  color: #666;
}

@media (max-width: 768px) {
  .products-content {
    padding: 1rem;
  }
  
  .product-item {
    padding: 1rem;
  }
  
  .product-icon {
    font-size: 1.5rem;
    margin-right: 1rem;
  }
}

.header-placeholder {
  width: 200px;
}
</style>