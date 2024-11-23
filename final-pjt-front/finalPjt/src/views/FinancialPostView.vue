<template>
    <div>
        <h1>금융 정보 게시판</h1>

        <div v-if="posts.length">
            <h2>게시글 목록</h2>
            <ul>
                <li v-for="post in posts" :key="post.id" @click="goToDetail(post.id)" style="cursor: pointer;">
                    <h3>{{ post.title }}</h3>
                    <p>{{ post.content }}</p>
                </li>
            </ul>
        </div>
        <div v-else>
            <p>게시글이 없습니다.</p>
        </div>

        <h2>관련 유튜브 영상</h2>
        <div v-if="videos.length">
            <ul>
                <li v-for="video in videos" :key="video.id.videoId">
                    <a :href="`https://www.youtube.com/watch?v=${video.id.videoId}`" target="_blank">
                        {{ video.snippet.title }}
                    </a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useEggStore } from "@/stores/egg"


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

const fetchYouTubeVideos = () => {
    const apiKey = 'YOUR_YOUTUBE_API_KEY'
    const defaultQuery = '금융 정보'

    axios({
        method: 'get',
        url: `https://www.googleapis.com/youtube/v3/search`,
        params: {
            part: 'snippet',
            q: defaultQuery,
            type: 'video',
            key: apiKey
        }
    })
    .then(res => {
        videos.value = res.data.items || []
    })
    .catch(err => {
        console.log('Error fetching YouTube videos:', err)
    })
}

// 페이지 로드 시 초기 데이터 가져오기
onMounted(() => {
    fetchPosts()
    fetchYouTubeVideos()
})

const goToDetail = (id) => {
    router.push(`/financial-posts/${id}`) // 상세 페이지로 이동
}

</script>
