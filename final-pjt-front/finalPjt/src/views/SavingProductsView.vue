<template>
  <div>
    <h1>적금 상품 리스트</h1>
    <div>
      <button @click="goBack">뒤로 가기</button>
    </div>

    <!-- 검색 및 필터링 옵션 -->
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

    <div v-if="detailId !== 0">
      <SavingProductDetail 
        :product-id="detailId"
        @close="close"
      />
    </div>

    <!-- 금융 상품 리스트 -->
    <SavingProductsList 
      :products-list="productsList"
      @detail="handleDetail"
    />
    
  </div>
</template>

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
