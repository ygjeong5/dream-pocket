<template>
  <div class="chat-container">
    <div class="chat-header">
      <div class="card-icon">🤖</div>
      <h3>AI 금융 상담사</h3>
    </div>
    
    <div class="chat-area" ref="chatContainer">
      <div v-for="(chat, index) in chats" 
           :key="index" 
           :class="['chat-item', `${chat.type}-chat`]">
        <div class="chat-content">
          {{ chat.content }}
        </div>
      </div>
    </div>
    
    <div class="chat-input-container">
      <input 
        v-model="userInput"
        @keyup.enter="chatSubmit"
        class="chat-input"
        placeholder="메시지를 입력하세요..."
        id="chat-input"
        name="chat-input"
        autocomplete="off"
      >
      <button 
        @click="chatSubmit"
        class="card-button"
        id="chat-submit"
        name="chat-submit"
      >
        전송
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'
import { useEggStore } from '@/stores/egg'

const store = useEggStore()
const API_URL = store.API_URL

const chatContainer = ref(null)
const userInput = ref('')
const chats = ref([])
const oldMsg = ref('')

// 채팅창 자동 스크롤
watch(chats, () => {
  setTimeout(() => {
    if (chatContainer.value) {
      chatContainer.value.scrollTop = chatContainer.value.scrollHeight
    }
  }, 0)
}, { deep: true })

const addChat = (type, content) => {
  chats.value.push({
    type,
    content
  })
}

const chatReceive = async (userMsg) => {
  try {
    const response = await axios({
      method: 'post',
      url: `${API_URL}chatbot/chat_message/`,
      headers: {
        'Authorization': `Token ${store.token}`,
        'Content-Type': 'application/json'
      },
      data: {
        message: userMsg
      }
    })

    // 응답 메시지 처리
    const assistantMessage = response.data.response
    addChat('receive', assistantMessage)
    oldMsg.value = assistantMessage

  } catch (error) {
    console.error('Error details:', error.response?.data || error)
    addChat('receive', '죄송합니다. 오류가 발생했습니다.')
  }
}

const chatSubmit = () => {
  const message = userInput.value.trim()
  if (!message) return

  addChat('send', message)
  chatReceive(message)
  userInput.value = ''
}
</script>

<style scoped>
.chat-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  background: white;
  border-radius: 20px;
  padding: 1.5rem;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.chat-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.card-icon {
  font-size: 2.5rem;
  width: 70px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(145deg, #e8f1f8, #d4e6f1);
  border-radius: 50%;
}

.chat-header h3 {
  font-size: 1.5rem;
  color: #2c3e50;
  margin: 0;
  font-family: 'DNFBitBitv2';
}

.chat-area {
  flex: 1;
  min-height: 300px;
  max-height: 400px;
  overflow-y: auto;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  background: linear-gradient(145deg, #f8f9fa, #e8f1f8);
  border-radius: 15px;
}

.chat-item {
  max-width: 80%;
  padding: 1rem;
  border-radius: 15px;
  animation: fadeIn 0.3s ease;
}

.send-chat {
  align-self: flex-end;
  background: linear-gradient(145deg, #3498db, #2980b9);
  color: white;
  border-bottom-right-radius: 5px;
}

.receive-chat {
  align-self: flex-start;
  background: white;
  color: #2c3e50;
  border-bottom-left-radius: 5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.chat-content {
  font-family: 'DNFBitBitv2';
  font-size: 1rem;
  line-height: 1.5;
  word-break: break-word;
}

.chat-input-container {
  display: flex;
  gap: 1rem;
  padding: 0.8rem;
  background: white;
  border-radius: 15px;
  border: 3px solid #88C9F2;
  box-shadow: 0 4px 0 #a5c6e1;
}

.chat-input {
  flex: 1;
  padding: 0.8rem;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  font-size: 1rem;
  font-family: 'DNFBitBitv2';
  color: #2c3e50;
  outline: none;
  transition: all 0.3s ease;
}

.chat-input:focus {
  border-color: #88C9F2;
  box-shadow: 0 0 0 2px rgba(136, 201, 242, 0.1);
}

.chat-submit-btn {
  padding: 0.8rem 1.5rem;
  background: white;
  border: 2px solid #3b82f6;
  color: #3b82f6;
  border-radius: 10px;
  font-family: 'DNFBitBitv2';
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.chat-submit-btn:hover {
  background: linear-gradient(145deg, #3b82f6, #2563eb);
  color: white;
  transform: translateY(2px);
}

.chat-submit-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent,
    rgba(59, 130, 246, 0.2),
    transparent
  );
  transition: 0.5s;
}

.chat-submit-btn:hover::before {
  left: 100%;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 스크롤바 스타일링 */
.chat-area::-webkit-scrollbar {
  width: 8px;
}

.chat-area::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.chat-area::-webkit-scrollbar-thumb {
  background: #88C9F2;
  border-radius: 4px;
}

.chat-area::-webkit-scrollbar-thumb:hover {
  background: #7fb3d5;
}
</style>