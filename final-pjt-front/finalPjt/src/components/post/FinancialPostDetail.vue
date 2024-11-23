<template>
    <div v-if="post">
        <h1>{{ post.title }}</h1>
        <p>{{ post.content }}</p>
        <p><strong>작성일:</strong> {{ new Date(post.created_at).toLocaleDateString() }}</p>
        <button @click="goBack">목록으로 돌아가기</button>
    </div>
    <div v-else>
        <p>로딩 중...</p>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const post = ref(null)
const route = useRoute()
const router = useRouter()

const fetchPostDetail = () => {
    const postId = route.params.id // URL에서 게시글 ID 추출
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/financial-posts/${postId}/`,
    })
    .then(res => {
        post.value = res.data
    })
    .catch(err => {
        console.log('Error fetching post details:', err)
    })
}

const goBack = () => {
    router.push('/financial-posts') // 목록 페이지로 돌아가기
}

onMounted(() => {
    fetchPostDetail()
})
</script>
