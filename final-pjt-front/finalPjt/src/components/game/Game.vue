<template>
    <p>
        <button @click="close">
            닫기
        </button>
    </p>
    <div class="game-container">
      <iframe :src="gameUrl" width="1500" height="1500" frameborder="0" allowfullscreen></iframe>
    </div>
  </template>

<script setup>
defineProps({
    gameUrl:String
})

const emit = defineEmits(["close"])

const close = () => {
  emit("close")
}

</script>

<style scoped>

</style>