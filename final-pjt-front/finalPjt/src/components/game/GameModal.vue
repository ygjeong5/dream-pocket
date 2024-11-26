<template>
    <div class="modal-overlay">
        <div class="game-modal">
            <div class="game-frame">
                <iframe 
                    :src="gameUrl" 
                    frameborder="0" 
                    allowfullscreen
                ></iframe>
            </div>
            <button @click="$emit('close')" class="close-btn">
                게임 종료
            </button>
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
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.game-modal {
    background: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 0 50px rgba(0,0,0,0.3);
    border: 4px solid #88C9F2;
    position: relative;
    width: 95%;
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.game-frame {
    width: 100%;
    height: calc(85vh - 100px);
    overflow: hidden;
    border-radius: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
}

iframe {
    width: 100%;
    height: 100%;
    border: none;
    max-width: 1200px;
    max-height: 800px;
}

.close-btn {
    position: relative;
    margin-top: 1.5rem;
    background: linear-gradient(145deg, #F25E86, #F29F05);
    color: white;
    border: none;
    padding: 0.8rem 1.8rem;
    border-radius: 12px;
    font-family: 'DNFBitBitv2';
    font-size: 1.1rem;
    cursor: pointer;
    border: 3px solid #F2B705;
    box-shadow: 0 4px 0 #F25E86;
    transition: all 0.3s ease;
    z-index: 1001;
    white-space: nowrap;
}

.close-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 0 #F25E86;
}

.close-btn::before {
    content: '';
    position: absolute;
    top: -3px;
    left: -3px;
    right: -3px;
    bottom: -3px;
    border-radius: 15px;
    background: linear-gradient(145deg, #F25E86, #F29F05);
    z-index: -1;
    opacity: 0.5;
}

@media (max-width: 1280px) {
    .game-frame {
        height: calc(80vh - 100px);
    }
}

@media (max-width: 768px) {
    .game-modal {
        width: 98%;
        padding: 1rem;
    }

    .game-frame {
        height: calc(70vh - 80px);
    }

    .close-btn {
        margin-top: 1rem;
        padding: 0.8rem 1.5rem;
        font-size: 1rem;
    }
}
</style>