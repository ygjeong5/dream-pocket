<template>
  <div class="game-selection">
      <h1 class="game-header">미니게임 플레이</h1>
      <div class="game-container">게임으로 실전 금융 스킬 기르기 !</div>
      <div class="games-grid">
          <div class="game-card" v-for="(game, index) in games" :key="index">
              <p class="game-title">{{ game.title }}</p>
              <img 
                  @click="changeUrl(game.url)" 
                  :src="game.image" 
                  :alt="game.title"
                  class="game-image"
              >
          </div>
      </div>
      
      <GameModal 
          v-if="gameUrl" 
          :game-url="gameUrl"
          @close="closeGame"
      />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import GameModal from './GameModal.vue'

const gameUrl = ref('')

const games = [
  {
      title: 'Game 1',
      url: 'https://main.krxverse.co.kr/_contents/ACA/02/02010400/ACA02010400P1.jsp',
      image: new URL('@/assets/game1.png', import.meta.url).href
  },
  {
      title: 'Game 2',
      url: 'https://main.krxverse.co.kr/_contents/ACA/02/02010400/ACA02010400P4.jsp',
      image: new URL('@/assets/game2.png', import.meta.url).href
  },
  {
      title: 'Game 3',
      url: 'https://main.krxverse.co.kr/_contents/ACA/02/02010400/ACA02010400P2.jsp',
      image: new URL('@/assets/game3.png', import.meta.url).href
  },
  {
      title: 'Game 4',
      url: 'https://main.krxverse.co.kr/_contents/ACA/02/02010400/ACA02010400P3.jsp',
      image: new URL('@/assets/game4.png', import.meta.url).href
  }
]

const changeUrl = (url) => {
  gameUrl.value = url
}

const closeGame = () => {
  gameUrl.value = ''
}
</script>

<style scoped>
.game-selection {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 2rem;
  font-family: 'DNFBitBitv2';
}

.game-header {
  text-align: center;
  color: #34343f;
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.1);
  background: linear-gradient(145deg, #88C9F2, #9CD95F);
  padding: 1.5rem;
  border-radius: 20px;
  color: white;
  border: 4px solid #F2B705;
  box-shadow: 0 8px 0 #F25E86;
}

.games-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  padding: 1rem;
}

.game-card {
  background: #ffffff;
  border-radius: 20px;
  padding: 1.5rem;
  box-shadow: 0 8px 0 #F25E86;
  border: 4px solid #88C9F2;
  transition: all 0.3s ease;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.game-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 0 #F25E86;
  border-color: #F2B705;
}

.game-title {
  font-size: 1.8rem;
  text-align: center;
  margin: 0 0 1rem 0;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.1);
  background: linear-gradient(145deg, #88C9F2, #9CD95F);
  padding: 0.8rem;
  border-radius: 12px;
  color: white;
  border: 2px solid #F2B705;
}

.game-image {
  width: 100%;
  height: auto;
  border-radius: 12px;
  transition: transform 0.3s ease;
  border: 3px solid transparent;
}

.game-card:hover .game-image {
  transform: scale(1.05);
  border-color: #F2B705;
}

@font-face {
  font-family: 'DNFBitBitv2';
  font-style: normal;
  font-weight: 400;
  src: url('//cdn.df.nexon.com/img/common/font/DNFBitBitv2.otf') format('opentype');
}

.game-container {
  text-align: center;
  font-size: 1.3rem;
  margin-bottom: 2rem;
  color: #34343f;
  text-shadow: 1px 1px 0 rgba(0,0,0,0.1);
}

@media (max-width: 768px) {
  .games-grid {
      grid-template-columns: 1fr;
  }
  
  .game-header {
      font-size: 2rem;
      padding: 1rem;
  }
  
  .game-container {
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
  }
}
</style>