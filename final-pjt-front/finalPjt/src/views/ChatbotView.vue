<template>
  <div class="chat-view">
    <div class="chat-header">
      <h1>AI 금융 상담사</h1>
      <div class="header-placeholder"></div>
    </div>
    
    <div class="chat-container">
      <ChatBot />
    </div>
  </div>
</template>

<script setup>
import ChatBot from '@/components/chatbot/Chatbot.vue'
</script>

<style scoped>
.chat-view {
  max-width: 1400px;
  margin: 2rem auto;
  padding: 2rem;
  font-family: 'DNFBitBitv2';
}

.chat-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  height: 80px;
}

.chat-header h1 {
  font-size: 2.5rem;
  color: #2c3e50;
  margin: 0;
  background: linear-gradient(to left top, #2980b9, #3498db);
  -webkit-background-clip: text;
  -webkit-text-stroke: 2px rgba(39, 54, 154, 0.726);
  color: transparent;
  animation: titleFloat 3s ease-in-out infinite;
}

@keyframes titleFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.chat-container {
  background: white;
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  min-height: calc(100vh - 200px);
}

.header-placeholder {
  width: 200px;
}
</style>