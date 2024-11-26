<template>
  <div>
    <ul>
      <li v-for="product in productsList" :key="product.fin_prdt_cd">
        <div>
          <p>{{ product.kor_co_nm }} - {{ product.fin_prdt_nm }}</p>
          <button @click="goDetail(product.id)">상세</button>
          <p>
            <button @click="store.financialCart(product.id)">예금 상품 비교</button>
          </p>
        </div>
      </li>
    </ul>
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
/* 스타일은 기존과 동일 */
</style>


<!-- <template>
  <div class="products-grid">
    <div v-for="product in productsList" 
         :key="product.fin_prdt_cd" 
         class="product-card">
      <div class="product-header">
        <div class="bank-logo">🏦</div>
        <div class="bank-name">{{ product.kor_co_nm }}</div>
      </div>
      
      <div class="product-body">
        <h3 class="product-name">{{ product.fin_prdt_nm }}</h3>
        <div class="product-info">
          <div class="info-item">
            <span class="label">최고금리</span>
            <span class="value">{{ product.max_rate }}%</span>
          </div>
          <div class="info-item">
            <span class="label">가입기간</span>
            <span class="value">{{ product.save_trm }}개월</span>
          </div>
        </div>
      </div>

      <div class="product-footer">
        <button @click="goDetail(product.id)" class="detail-btn">
          상세정보 보기
        </button>
        <button @click="store.financialCart(product.id)" class="compare-btn">
          비교함에 담기
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
    gap: 2rem;
}

.product-card {
    background: white;
    border-radius: 20px;
    padding: 1.5rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    transition: transform 0.3s ease;
    border: 1px solid rgba(136, 201, 242, 0.1);
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.product-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.bank-logo {
    font-size: 2rem;
}

.bank-name {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
}

.product-name {
    font-size: 1.3rem;
    color: #2c3e50;
    margin-bottom: 1rem;
}

.product-info {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.info-item {
    text-align: center;
    padding: 0.8rem;
    background: #f8f9fa;
    border-radius: 12px;
}

.info-item .label {
    display: block;
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 0.3rem;
}

.info-item .value {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
}

.product-footer {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
}

.detail-btn, .compare-btn {
    padding: 0.8rem;
    border: none;
    border-radius: 10px;
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

.detail-btn {
    background: #88C9F2;
    color: white;
}

.compare-btn {
    background: #9CD95F;
    color: white;
}

.detail-btn:hover, .compare-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}
</style> -->
