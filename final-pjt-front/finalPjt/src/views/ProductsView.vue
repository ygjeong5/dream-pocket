<template>
  <div class="products-container">
    <h1>금융 상품 리스트</h1>
    <div class="products-nav">
      <RouterLink :to="{ name:'FinancialProductsView' }" class="product-link">
        <div class="product-button">
          <span>예금 상품</span>
        </div>
      </RouterLink>
      
      <RouterLink :to="{ name:'SavingProductsView' }" class="product-link">
        <div class="product-button">
          <span>적금 상품</span>
        </div>
      </RouterLink>
      
      <RouterLink :to="{ name:'ProductComparison'}" class="product-link">
        <div class="product-button">
          <span>상품 비교</span>
        </div>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

</script>

<style scoped>
.products-container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 2rem;
  text-align: center;
}

h1 {
  font-family: 'DNFBitBitv2';
  color: transparent;
  background: linear-gradient(to left top, #1E90FF, #00bfff);
  -webkit-background-clip: text;
  -webkit-text-stroke: 2px #1e90ff;
  margin-bottom: 2rem;
}

.products-nav {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-top: 2rem;
}

.product-link {
  text-decoration: none;
}

.product-button {
  background: #f8f9fa;
  border: 3px solid #7fb3d5;
  color: #2c3e50;
  box-shadow: 0 4px 0 #85929e;
  border-radius: 19px;
  padding: 1rem 2rem;
  font-family: 'DNFBitBitv2';
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  min-width: 150px;
}

.product-button:hover {
  background: linear-gradient(145deg, #2980b9, #3498db);
  border-color: #7fb3d5;
  transform: translateY(2px);
  box-shadow: 0 2px 0 #85929e;
}

.product-button span {
  display: block;
  text-align: center;
}
</style>