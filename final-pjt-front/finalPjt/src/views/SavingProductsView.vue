<template>
  <div class="products-content">
    <div class="products-header">
      <h1>적금 상품 리스트</h1>
      <button @click="goBack" class="back-button">뒤로 가기</button>
    </div>

    <!-- 검색 및 필터링 옵션 -->
    <div class="products-grid">
      <!-- 왼쪽: 필터 섹션 -->
      <div class="filter-section">
        <div class="form-container">
          <h2>🔍 검색 필터</h2>
          <div class="form-group">
            <label for="bankName">은행 이름</label>
            <input
              id="bankName"
              type="text"
              placeholder="은행 이름 검색"
              v-model="searchBankName"
              @input="fetchProducts"
            />
          </div>

          <div class="form-group">
            <label for="sortBy">정렬 기준</label>
            <select id="sortBy" v-model="sortBy" @change="fetchProducts">
              <option value="id">정렬 기준 선택</option>
              <option value="highest_rate">최고 금리 내림차순</option>
            </select>
          </div>

          <div class="form-group">
            <label>가입 기간 (개월)</label>
            <div class="term-filter">
              <input
                type="number"
                placeholder="최소 기간"
                v-model="minTerm"
                @input="fetchProducts"
              />
              <input
                type="number"
                placeholder="최대 기간"
                v-model="maxTerm"
                @input="fetchProducts"
              />
            </div>
          </div>
        </div>
      </div>

      <!-- 오른쪽: 상품 리스트 -->
      <div class="list-section">
        <div v-if="detailId !== 0">
          <SavingProductDetail 
            :product-id="detailId"
            @close="close"
          />
        </div>
        <SavingProductsList 
          :products-list="productsList"
          @detail="handleDetail"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.products-content {
  max-width: 1400px;
  margin: 2rem auto;
  padding: 2rem;
  font-family: 'DNFBitBitv2';
  background-color: #f8fafc;
}

.products-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  height: 80px;
  padding: 0 1rem;
}

.products-header h1 {
  font-size: 2.5rem;
  color: #2c3e50;
  margin: 0;
}

.back-button {
  padding: 0.8rem 1.5rem;
  background: #d4126e;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'DNFBitBitv2';
}

.back-button:hover {
  background: #b30e5c;
}

.products-grid {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 2rem;
}

.filter-section {
  position: sticky;
  top: 2rem;
  height: fit-content;
}

.form-container {
  background: white;
  padding: 1.5rem;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.form-container h2 {
  margin: 0 0 1.5rem 0;
  color: #2c3e50;
  font-size: 1.3rem;
}

.form-group {
  margin-bottom: 1.2rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #2c3e50;
  font-size: 0.9rem;
}

select, input {
  width: 100%;
  padding: 0.7rem;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  background: white;
  font-size: 0.9rem;
}

.term-filter {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.8rem;
}

.list-section {
  background: white;
  padding: 1.5rem;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  min-width: 0;
}

@media (max-width: 1200px) {
  .products-grid {
    grid-template-columns: 250px 1fr;
  }
}

@media (max-width: 1024px) {
  .products-grid {
    grid-template-columns: 1fr;
  }
  
  .filter-section {
    position: static;
  }

  .products-content {
    padding: 1rem;
  }
}

@media (max-width: 640px) {
  .products-header {
    flex-direction: column;
    height: auto;
    gap: 1rem;
  }

  .products-header h1 {
    font-size: 2rem;
  }
}
</style>

<script setup>
import SavingProductsList from "@/components/financialproduct/SavingProductsList.vue"
import SavingProductDetail from "@/components/financialproduct/SavingProductDetail.vue"
import { ref, onMounted } from "vue"
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
    url: `${store.API_URL}finlife/saving-products/`,
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
