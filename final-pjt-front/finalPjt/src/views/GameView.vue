<template>
    <div>
        <Game
          :game-url="gameUrl"
          @close="close"
        />
        <div>
            <p>Game 1</p>
            <img @click="changeUrl('https://main.krxverse.co.kr/_contents/ACA/02/02010400/ACA02010400P1.jsp')" src="@/assets/game1.png" alt="">
        </div>
        <div>
            <p>Game 2</p>
            <img @click="changeUrl('https://main.krxverse.co.kr/_contents/ACA/02/02010400/ACA02010400P4.jsp')" src="@/assets/game2.png" alt="">
        </div>
        <div>
            <p>Game 3</p>
            <img @click="changeUrl('https://main.krxverse.co.kr/_contents/ACA/02/02010400/ACA02010400P2.jsp')" src="@/assets/game3.png" alt="">
        </div>
        <div>
            <p>Game 4</p>
            <img @click="changeUrl('https://main.krxverse.co.kr/_contents/ACA/02/02010400/ACA02010400P3.jsp')" src="@/assets/game4.png" alt="">
        </div>
    </div>
</template>

<script setup>
import Game from '@/components/game/Game.vue'
import { ref } from 'vue'

const gameUrl = ref('')

const changeUrl = function (url) {
    gameUrl.value = url
}

const close = function () {
    gameUrl.value = ''
}

</script>

<style scoped>

</style>