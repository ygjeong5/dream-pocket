<template>
  <div class="chat-container">
    <div class="chat-area" ref="chatContainer">
      <div v-for="(chat, index) in chats" 
           :key="index" 
           :class="['chat', `${chat.type}-chat`]">
        {{ chat.content }}
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
  display: flex;
  flex-direction: column;
  height: 100%;
  background: white;
  border-radius: 0 0 10px 10px;
}

.chat-area {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
  background: #f8f9fa;
}

.chat {
  margin: 0.5rem 0;
  padding: 0.5rem 1rem;
  border-radius: 1rem;
  max-width: 80%;
}

.send-chat {
  background-color: #007bff;
  color: white;
  margin-left: auto;
}

.receive-chat {
  background-color: #f1f1f1;
  margin-right: auto;
}

.chat-input-container {
  display: flex;
  padding: 1rem;
  gap: 0.5rem;
  border-top: 1px solid #ddd;
}

.chat-input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>