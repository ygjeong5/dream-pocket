<template>
  <div class="chat-view">
    <h1>챗봇 서비스</h1>
    <ChatBot />
  </div>
</template>

<script setup>
import ChatBot from '@/components/chatbot/Chatbot.vue'
</script>

<style scoped>
.chat-view {
  padding: 20px;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.chat-container {
  display: flex;
  flex-direction: column;
  height: calc(100% - 50px);
}
</style>