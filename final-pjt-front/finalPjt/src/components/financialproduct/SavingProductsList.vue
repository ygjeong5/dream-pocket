<template>
  <div class="products-container">
    <div class="products-grid">
      <div v-for="product in productsList" 
           :key="product.fin_prdt_cd" 
           class="product-card">
        <div class="product-header">
          <div class="bank-logo">
            <font-awesome-icon :icon="['fas', 'piggy-bank']" />
          </div>
          <div class="bank-name">{{ product.kor_co_nm }}</div>
        </div>
        
        <div class="product-body">
          <h3 class="product-name">{{ product.fin_prdt_nm }}</h3>
          <div class="product-info">
            <!-- 추가 정보를 표시할 수 있는 공간 -->
          </div>
        </div>

        <div class="product-footer">
          <button @click="goDetail(product.id)" class="detail-btn">
            <font-awesome-icon :icon="['fas', 'circle-info']" />
            상세정보
          </button>
          <button @click="store.savingCart(product.id)" class="compare-btn">
            <font-awesome-icon :icon="['fas', 'scale-balanced']" />
            비교하기
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useEggStore } from '@/stores/egg'

const store = useEggStore()
const props = defineProps({
  productsList: Array,
})

const emit = defineEmits(["detail"])

const goDetail = (productId) => {
  emit("detail", productId)
}
</script>

<style scoped>
.products-container {
  max-width: 1400px;
  margin: 2rem auto;
  padding: 1.5rem;
  font-family: 'DNFBitBitv2';
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  width: 100%;
}

.product-card {
  background: white;
  border-radius: 15px;
  padding: 1.5rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.product-header {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  margin-bottom: 1rem;
  padding-bottom: 0.8rem;
  border-bottom: 1px solid #e0e0e0;
}

.bank-logo {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff0f7;
  border-radius: 8px;
  color: #d4126e;
  font-size: 1.2rem;
}

.bank-name {
  font-family: 'DNFBitBitv2';
  font-size: 1.1rem;
  color: #2c3e50;
}

.product-name {
  font-family: 'DNFBitBitv2';
  font-size: 1rem;
  color: #2c3e50;
  margin-bottom: 0.8rem;
  line-height: 1.4;
}

.product-info {
  background: #f8f9fa;
  padding: 0.8rem;
  border-radius: 8px;
  margin-bottom: 1rem;
}

.product-footer {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.8rem;
}

.detail-btn, .compare-btn {
  padding: 0.6rem;
  border: none;
  border-radius: 8px;
  font-family: 'DNFBitBitv2';
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
}

.detail-btn {
  background: #d4126e;
  color: white;
}

.compare-btn {
  background: #fff0f7;
  color: #d4126e;
}

.detail-btn:hover {
  background: #b30f5d;
  transform: translateY(-2px);
}

.compare-btn:hover {
  background: #ffe0ef;
  transform: translateY(-2px);
}

@media (max-width: 1024px) {
  .products-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .products-grid {
    grid-template-columns: 1fr;
  }
}
</style>