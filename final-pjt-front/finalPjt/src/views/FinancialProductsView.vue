<template>
  <div>
    <h1>예금 상품 리스트</h1>
    <div>
      <button @click="goBack">뒤로 가기</button>
    </div>
    
    <!-- 검색 및 필터링 UI -->
    <div class="filters">
      <input
        type="text"
        placeholder="은행 이름 검색"
        v-model="searchBankName"
        @input="fetchProducts"
      />
      <select v-model="sortBy" @change="fetchProducts">
        <option value="id">정렬 기준 선택</option>
        <option value="highest_rate">최고 금리 내림차순</option>
      </select>
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
    <!-- 상세 정보 컴포넌트 -->
    <div v-if="detailId !== 0">
      <FinancialProductDetail 
        :product-id="detailId"
        @close="close"
      />
    </div>

    <!-- 금융 상품 리스트 컴포넌트 -->
    <FinancialProductsList 
      :products-list="productsList"
      @detail="handleDetail"
    />

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

// 검색 및 필터링 파라미터
const searchBankName = ref("")
const sortBy = ref("id")
const minTerm = ref(null)
const maxTerm = ref(null)

// 금융 상품 리스트를 가져오는 함수
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

// 상세 보기 핸들링
const handleDetail = (productId) => {
  detailId.value = productId
}

// 상세 정보 닫기
const close = () => {
  detailId.value = 0
}

const goBack = function () {
  router.push({ name:'ProductsView'})
}

// 컴포넌트 마운트 시 데이터 가져오기
onMounted(() => {
  fetchProducts()
})
</script>

<style scoped>
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}
.term-filter input {
  width: 100px;
}
</style>
