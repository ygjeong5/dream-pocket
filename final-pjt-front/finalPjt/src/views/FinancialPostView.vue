<template>
    <div>
        <h2>금융 뉴스</h2>
        <FinancialNews />
        <h2>금융 영상</h2>
        <Youtube />
    </div>
</template>

<script setup>
import Youtube from '@/components/post/Youtube.vue'
import FinancialNews from '@/components/post/FinancialNews.vue'
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useEggStore } from "@/stores/egg"
import { useRouter } from 'vue-router'


const router = useRouter()
const store = useEggStore()
const posts = ref([])
const videos = ref([])

const fetchPosts = () => {
    axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/financial-posts/',
        headers: {
            Authorization: `Token ${store.token}`,
            },
    })
    .then(res => {
        posts.value = res.data
    })
    .catch(err => {
        console.log('Error fetching posts:', err)
    })
}


// 페이지 로드 시 초기 데이터 가져오기
onMounted(() => {
    fetchPosts()
})

const goToDetail = (id) => {
    router.push(`/financial-posts/${id}`) // 상세 페이지로 이동
}

</script>
