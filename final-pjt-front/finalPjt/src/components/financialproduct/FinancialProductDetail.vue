<template>
  <div class="product-detail">
    <div class="detail-container">
      <h2 class="detail-title">상세 정보</h2>
      
      <div class="info-section">
        <div class="info-item">
          <div class="info-label">
            <font-awesome-icon :icon="['fas', 'door-open']" />
            가입 방법
          </div>
          <div class="info-value">{{ productInfo.join_way }}</div>
        </div>

        <div class="info-item">
          <div class="info-label">
            <font-awesome-icon :icon="['fas', 'users']" />
            가입 대상
          </div>
          <div class="info-value">{{ productInfo.join_member }}</div>
        </div>

        <div class="info-item">
          <div class="info-label">
            <font-awesome-icon :icon="['fas', 'star']" />
            우대 사항
          </div>
          <div class="info-value">{{ productInfo.spcl_cnd }}</div>
        </div>
      </div>

      <div class="options-section">
        <h3 class="options-title">금리 정보</h3>
        <div class="options-grid">
          <div v-for="option in productOptions" :key="option.id" class="option-card">
            <div class="option-header">
              <span class="term">{{ option.save_trm }}개월</span>
              <span class="rate-type">{{ option.intr_rate_type_nm }}</span>
            </div>
            <div class="rate-info">
              <div class="rate-item">
                <span class="rate-label">최저금리</span>
                <span class="rate-value">{{ option.intr_rate }}%</span>
              </div>
              <div class="rate-item">
                <span class="rate-label">최고금리</span>
                <span class="rate-value">{{ option.intr_rate2 }}%</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <button @click="close" class="close-btn">
        <font-awesome-icon :icon="['fas', 'xmark']" />
        닫기
      </button>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { useEggStore } from '@/stores/egg'
import { onMounted, ref, watch } from 'vue'

const store = useEggStore()
const props = defineProps({
  productId: Number
})

const productInfo = ref({})
const productOptions = ref({})

const getProductDetail = function () {
  axios({
    method: 'get',
    url:`${store.API_URL}finlife/financial-product/detail/${props.productId}/`,
    headers:{
      Authorization: `Token ${store.token}`
    }
  })
  .then(res => {
    productInfo.value = res.data.product
    productOptions.value = res.data.options
  })
  .catch(err => {
    console.log(err)
  })
}
watch(() => props.productId, getProductDetail)

onMounted(() => {
  getProductDetail()
})

const emit = defineEmits(['close'])

const close = function () {
  emit('close')
}

</script>

<style scoped>
.product-detail {
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.detail-container {
  background: white;
  border-radius: 20px;
  padding: 30px;
  width: 90%;
  max-width: 800px;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

.detail-title {
  font-family: 'yg-jalnan';
  font-size: 24px;
  color: #2c3e50;
  text-align: center;
  margin-bottom: 30px;
  padding-bottom: 15px;
  border-bottom: 2px solid #e5e7eb;
}

.info-section {
  display: grid;
  gap: 20px;
  margin-bottom: 30px;
}

.info-item {
  background: #f8f9fa;
  border-radius: 12px;
  padding: 20px;
  transition: all 0.3s ease;
}

.info-item:hover {
  background: #f0f7ff;
  transform: translateY(-2px);
}

.info-label {
  font-family: 'Pretendard-Regular';
  font-size: 15px;
  color: #666;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.info-value {
  font-family: 'Pretendard-Regular';
  font-size: 16px;
  color: #2c3e50;
  line-height: 1.6;
}

.options-section {
  margin-top: 30px;
}

.options-title {
  font-family: 'yg-jalnan';
  font-size: 20px;
  color: #2c3e50;
  margin-bottom: 20px;
}

.options-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 15px;
}

.option-card {
  background: #f8f9fa;
  border-radius: 12px;
  padding: 20px;
  transition: all 0.3s ease;
}

.option-card:hover {
  background: #f0f7ff;
  transform: translateY(-2px);
}

.option-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
  padding-bottom: 10px;
  border-bottom: 1px solid #e5e7eb;
}

.term {
  font-family: 'yg-jalnan';
  font-size: 18px;
  color: #1a237e;
}

.rate-type {
  font-family: 'Pretendard-Regular';
  font-size: 14px;
  color: #666;
  background: #e5e7eb;
  padding: 4px 8px;
  border-radius: 15px;
}

.rate-info {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.rate-item {
  text-align: center;
}

.rate-label {
  display: block;
  font-family: 'Pretendard-Regular';
  font-size: 13px;
  color: #666;
  margin-bottom: 5px;
}

.rate-value {
  font-family: 'yg-jalnan';
  font-size: 16px;
  color: #06b6d4;
}

.close-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin: 30px auto 0;
  padding: 12px 24px;
  border: 2px solid #e5e7eb;
  border-radius: 25px;
  background: white;
  font-family: 'yg-jalnan';
  font-size: 15px;
  color: #666;
  cursor: pointer;
  transition: all 0.3s ease;
}

.close-btn:hover {
  background: #f0f7ff;
  border-color: #1a237e;
  color: #1a237e;
  transform: scale(1.05);
}

/* 스크롤바 스타일링 */
.detail-container::-webkit-scrollbar {
  width: 8px;
}

.detail-container::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.detail-container::-webkit-scrollbar-thumb {
  background: #c1c1c1;
  border-radius: 4px;
}

.detail-container::-webkit-scrollbar-thumb:hover {
  background: #a1a1a1;
}
</style>