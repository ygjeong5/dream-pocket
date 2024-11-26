<template>
  <div class="products-grid">
    <div v-for="product in productsList" 
         :key="product.fin_prdt_cd" 
         class="product-card">
      <div class="product-header">
        <div class="bank-logo">
          <font-awesome-icon :icon="['fas', 'building-columns']" />
        </div>
        <div class="bank-name">{{ product.kor_co_nm }}</div>
      </div>
      
      <div class="product-body">
        <h3 class="product-name">{{ product.fin_prdt_nm }}</h3>
        <div class="product-info">
        
        </div>
      </div>

      <div class="product-footer">
        <button @click="goDetail(product.id)" class="detail-btn">
          <font-awesome-icon :icon="['fas', 'circle-info']" />
          상세정보
        </button>
        <button @click="store.financialCart(product.id)" class="compare-btn">
          <font-awesome-icon :icon="['fas', 'scale-balanced']" />
          비교하기
        </button>
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
.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px;
  max-width: 1080px;
  margin: 0 auto;
}

.product-card {
  background: white;
  border-radius: 15px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  border: 1px solid #e5e7eb;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
}

.product-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid #e5e7eb;
}

.bank-logo {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f0f7ff;
  border-radius: 50%;
  color: #1a237e;
  font-size: 20px;
}

.bank-name {
  font-family: 'yg-jalnan';
  font-size: 16px;
  color: #2c3e50;
}

.product-name {
  font-family: 'Pretendard-Regular';
  font-size: 15px;
  color: #34343f;
  margin-bottom: 15px;
  line-height: 1.4;
}

.product-info {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 20px;
}

.info-item {
  text-align: center;
  padding: 12px;
  background: #f8f9fa;
  border-radius: 10px;
  transition: all 0.2s ease;
}

.info-item:hover {
  background: #f0f7ff;
}

.label {
  display: block;
  font-family: 'Pretendard-Regular';
  font-size: 13px;
  color: #666;
  margin-bottom: 5px;
}

.value {
  font-family: 'yg-jalnan';
  font-size: 16px;
  color: #1a237e;
}

.product-footer {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.detail-btn, .compare-btn {
  height: 35px;
  border: 2px solid;
  border-radius: 25px;
  font-family: 'yg-jalnan';
  font-size: 13px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  background: white;
}

.detail-btn {
  border-color: #1a237e;
  color: #1a237e;
}

.compare-btn {
  border-color: #06b6d4;
  color: #06b6d4;
}

.detail-btn:hover {
  background: #1a237e;
  color: white;
  transform: scale(1.05) rotate(1deg);
  box-shadow: 0 4px 12px rgba(26, 35, 126, 0.2);
}

.compare-btn:hover {
  background: #06b6d4;
  color: white;
  transform: scale(1.05) rotate(-1deg);
  box-shadow: 0 4px 12px rgba(6, 182, 212, 0.2);
}

/* 아이콘 스타일 */
.fa-building-columns {
  font-size: 20px;
}

.fa-circle-info, .fa-scale-balanced {
  font-size: 14px;
}
</style>
