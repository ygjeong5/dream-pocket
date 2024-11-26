<template>
  <div class="modal">
    <div class="modal-content">
      <button class="close-button" @click="$emit('close')">×</button>
      <iframe 
        :src="gameUrl" 
        frameborder="0" 
        class="game-frame"
        width="1024"
        height="768"
        scrolling="no"
      ></iframe>
    </div>
  </div>
</template>

<script setup>
defineProps({
    gameUrl: {
        type: String,
        required: true
    }
})

defineEmits(['close'])
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1100;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 15px;
  position: relative;
  width: 90vw;  /* 뷰포트 너비의 90% */
  height: 90vh; /* 뷰포트 높이의 90% */
  max-width: 1300px; /* 최대 너비 */
  max-height: 900px; /* 최대 높이 */
  display: flex;
  flex-direction: column;
}

.game-frame {
  width: 100%;
  height: 100%;
  border: none;
  border-radius: 10px;
}

.close-button {
  position: absolute;
  top: -40px;
  right: -40px;
  background: #F25E86;
  border: none;
  color: white;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  border: 3px solid white;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.close-button:hover {
  transform: scale(1.1);
  background: #ff4d7d;
}

/* 반응형 디자인을 위한 미디어 쿼리 */
@media (max-width: 1400px) {
  .modal-content {
    width: 95vw;
    height: 95vh;
  }
}

@media (max-width: 768px) {
  .close-button {
    top: 10px;
    right: 10px;
  }
}
</style>