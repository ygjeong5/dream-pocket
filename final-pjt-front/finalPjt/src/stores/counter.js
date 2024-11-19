import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }
  
  const API_URL = ref('http://127.0.0.1:8000/')


  return { count, doubleCount, increment, API_URL}
})
