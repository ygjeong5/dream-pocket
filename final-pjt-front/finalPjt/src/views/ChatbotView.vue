<template>
  <div class="chat-view">
    <div class="chat-header">
      <h1>AI 금융 상담사</h1>
      <div class="menu-container">
        <button class="menu-icon" @click="isMenuOpen = !isMenuOpen">
          <i class="fas fa-bars"></i>
        </button>
        <div class="dropdown-menu" :class="{ 'open': isMenuOpen }">
          <ul>
            <li>메뉴 1</li>
            <li>메뉴 2</li>
            <li>메뉴 3</li>
          </ul>
        </div>
      </div>
    </div>
    
    <div class="chat-container">
      <ChatBot />
    </div>
  </div>
</template>

<script setup>
import ChatBot from '@/components/chatbot/Chatbot.vue'
import { ref } from 'vue'

const isMenuOpen = ref(false)
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

.menu-container {
  position: relative;
}

.menu-icon {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: #2980b9;
  padding: 0.5rem;
  transition: transform 0.3s ease;
}

.menu-icon:hover {
  transform: scale(1.1);
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  width: 200px;
  transform: translateY(-20px);
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
}

.dropdown-menu.open {
  transform: translateY(0);
  opacity: 1;
  visibility: visible;
}

.dropdown-menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.dropdown-menu li {
  padding: 1rem;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.dropdown-menu li:hover {
  background-color: #f5f5f5;
}
</style>