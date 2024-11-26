<template>
    <div class="product-detail">
        <div class="detail-header">
            <h1>{{ productInfo.fin_prdt_nm }}</h1>
            <button @click="handleDelete" class="delete-button">비교함에서 삭제</button>
        </div>

        <div class="info-section">
            <div class="info-card">
                <div class="info-item">
                    <span class="label">💳 가입 방법</span>
                    <span class="value">{{ productInfo.join_way }}</span>
                </div>
                <div class="info-item">
                    <span class="label">👥 가입 대상</span>
                    <span class="value">{{ productInfo.join_member }}</span>
                </div>
                <div class="info-item">
                    <span class="label">🎁 우대 사항</span>
                    <span class="value">{{ productInfo.spcl_cnd }}</span>
                </div>
            </div>
        </div>

        <div class="options-section">
            <h2>💰 금리 정보</h2>
            <div class="options-grid">
                <div v-for="option in productOptions" 
                     :key="option.id"
                     class="option-card">
                    <div class="option-header">
                        <span class="term">{{ option.save_trm }}개월</span>
                        <span class="type">{{ option.intr_rate_type_nm }}</span>
                    </div>
                    <div class="rates">
                        <div class="rate-item">
                            <span class="rate-label">최저금리</span>
                            <span class="rate-value">{{ option.intr_rate }}%</span>
                        </div>
                        <div class="rate-item">
                            <span class="rate-label">최고금리</span>
                            <span class="rate-value highlight">{{ option.intr_rate2 }}%</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useEggStore } from '@/stores/egg'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const store = useEggStore()
const productInfo = ref({})
const productOptions = ref({})

const props = defineProps({
    saveProduct : Number
})

const getProductInfo = function () {
    axios({
    method: 'get',
    url:`${store.API_URL}finlife/saving-product/detail/${props.saveProduct}/`,
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

const handleDelete = function () {
    store.savingListDelete(props.saveProduct)
}

onMounted(() => {
    getProductInfo()    
})

</script>

<style scoped>
.product-detail {
    padding: 2rem;
    font-family: 'DNFBitBitv2';
}

.detail-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}

.detail-header h1 {
    font-size: 2rem;
    color: #2c3e50;
    margin: 0;
    background: linear-gradient(135deg, #88C9F2, #9CD95F);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.delete-button {
    padding: 0.8rem 1.5rem;
    background: #ff4d4d;
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.delete-button:hover {
    background: #ff3333;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(255, 77, 77, 0.2);
}

.info-section {
    margin-bottom: 2rem;
}

.info-card {
    background: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.info-item {
    padding: 1rem;
    border-bottom: 1px solid #eee;
}

.info-item:last-child {
    border-bottom: none;
}

.info-item .label {
    display: block;
    color: #666;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
}

.info-item .value {
    color: #2c3e50;
    font-size: 1.2rem;
}

.options-section {
    background: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.options-section h2 {
    margin: 0 0 1.5rem 0;
    color: #2c3e50;
}

.options-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1.5rem;
}

.option-card {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 15px;
    transition: all 0.3s ease;
}

.option-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.option-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

.term {
    font-size: 1.2rem;
    font-weight: bold;
    color: #88C9F2;
}

.type {
    color: #666;
    font-size: 0.9rem;
}

.rates {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
}

.rate-item {
    text-align: center;
    padding: 0.8rem;
    background: white;
    border-radius: 10px;
}

.rate-label {
    display: block;
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 0.3rem;
}

.rate-value {
    font-size: 1.3rem;
    font-weight: bold;
    color: #2c3e50;
}

.rate-value.highlight {
    color: #9CD95F;
}

@media (max-width: 768px) {
    .detail-header {
        flex-direction: column;
        gap: 1rem;
        text-align: center;
    }

    .options-grid {
        grid-template-columns: 1fr;
    }
}
</style>