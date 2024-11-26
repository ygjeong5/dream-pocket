<template>
  <div class="products-content">
    <div class="products-header">
      <h1>예금 상품 리스트</h1>
      <button @click="goBack" class="back-button">← 뒤로 가기</button>
    </div>

    <div class="filters-section">
      <div class="filters">
        <div class="filter-group">
          <label>🏦 은행명 검색</label>
          <input
            type="text"
            class="filter-input"
            placeholder="은행 이름을 입력하세요"
            v-model="searchBankName"
            @input="fetchProducts"
          />
        </div>

        <div class="filter-group">
          <label>📊 정렬 기준</label>
          <select v-model="sortBy" @change="fetchProducts" class="filter-input">
            <option value="id">기본 정렬</option>
            <option value="highest_rate">최고 금리순</option>
          </select>
        </div>

        <div class="filter-group">
          <label>⏱️ 가입 기간</label>
          <div class="term-filter">
            <input
              type="number"
              placeholder="최소 기간"
              v-model="minTerm"
              @input="fetchProducts"
              class="filter-input"
            />
            <input
              type="number"
              placeholder="최대 기간"
              v-model="maxTerm"
              @input="fetchProducts"
              class="filter-input"
            />
          </div>
        </div>
      </div>
    </div>

    <div class="detail-section" v-if="detailId !== 0">
      <FinancialProductDetail 
        :product-id="detailId"
        @close="close"
      />
    </div>

    <div class="products-list">
      <FinancialProductsList 
        :products-list="productsList"
        @detail="handleDetail"
      />
    </div>
  </div>
</template>

<script setup>
import FinancialProductsList from "@/components/financialproduct/FinancialProductsList.vue"
import FinancialProductDetail from "@/components/financialproduct/FinancialProductDetail.vue"
import { onMounted, ref } from "vue"
import axios from "axios"
import { useEggStore } from "@/stores/egg"
import { useRouter } from "vue-router"

const router = useRouter()
const store = useEggStore()
const productsList = ref([])
const detailId = ref(0)

const searchBankName = ref("")
const sortBy = ref("id")
const minTerm = ref(null)
const maxTerm = ref(null)

const fetchProducts = () => {
  const params = {
    kor_co_nm: searchBankName.value || undefined,
    sort: sortBy.value || undefined,
    min_term: minTerm.value || undefined,
    max_term: maxTerm.value || undefined,
  }

  axios({
    method: "get",
    url: `${store.API_URL}finlife/financial-products/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
    params,
  })
    .then((res) => {
      productsList.value = res.data;
    })
    .catch((err) => {
      console.error(err)
    })
}

const handleDetail = (productId) => {
  detailId.value = productId
}

const close = () => {
  detailId.value = 0
}

const goBack = function () {
  router.push({ name:'ProductsView'})
}

onMounted(() => {
  fetchProducts()
})
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
}

.products-header h1 {
    font-size: 2.8rem;
    background: linear-gradient(135deg, #2193b0, #6dd5ed);
    -webkit-background-clip: text;
    color: transparent;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

.back-button {
    padding: 1rem 2rem;
    font-size: 1.1rem;
    background: linear-gradient(135deg, #88C9F2, #6dd5ed);
    color: white;
    border: none;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(136, 201, 242, 0.3);
    transition: all 0.3s ease;
}

.back-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(136, 201, 242, 0.4);
}

.filters-section {
    background: linear-gradient(145deg, #ffffff, #f8f9fa);
    padding: 2.5rem;
    border-radius: 25px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
    margin-bottom: 2.5rem;
    border: 1px solid rgba(136, 201, 242, 0.1);
}

.filters {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}

.filter-group {
    background: white;
    padding: 1.5rem;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    transition: transform 0.3s ease;
}

.filter-group:hover {
    transform: translateY(-2px);
}

.filter-group label {
    color: #2c3e50;
    font-size: 1.1rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
    display: block;
}

.filter-input {
    padding: 1rem;
    font-size: 1rem;
    width: 100%;
    border: 2px solid #e0e0e0;
    border-radius: 12px;
    background: white;
    transition: all 0.3s ease;
}

.filter-input:focus {
    border-color: #88C9F2;
    outline: none;
    box-shadow: 0 0 0 3px rgba(136, 201, 242, 0.2);
}

.term-filter {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.2rem;
}

.term-filter input {
    text-align: center;
    font-size: 1rem;
}

select.filter-input {
    cursor: pointer;
    appearance: none;
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 1rem center;
    background-size: 1em;
    padding-right: 2.5rem;
}

.products-list {
    background: linear-gradient(145deg, #ffffff, #f8f9fa);
    padding: 2.5rem;
    border-radius: 25px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
}

.detail-section {
    background: linear-gradient(145deg, #ffffff, #f8f9fa);
    padding: 2.5rem;
    border-radius: 25px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
    margin-bottom: 2.5rem;
    border: 1px solid rgba(136, 201, 242, 0.1);
}

@keyframes slideDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media (max-width: 768px) {
    .products-content {
        padding: 1.5rem;
    }

    .filters-section,
    .products-list,
    .detail-section {
        padding: 1.5rem;
    }

    .filter-group {
        padding: 1.2rem;
    }
}
</style>
