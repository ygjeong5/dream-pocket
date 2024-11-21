<template>
  <div>
    <!-- 댓글 작성 폼 -->
    <h3>댓글</h3>
    <div class="comment-form">
      <textarea 
        v-model="newComment" 
        placeholder="댓글을 입력하세요"
      ></textarea>
      <button @click="createComment">작성</button>
    </div>

    <!-- 댓글 목록 -->
    <div class="comments-list">
      <!-- 댓글이 있을 경우 -->
      <div v-if="comments && comments.length > 0">
        <div 
          v-for="comment in comments" 
          :key="comment.id"
          class="comment-item"
        >
          <div class="comment-content">
            <p>{{ comment.user.username }}</p>
            <textarea
              v-if="editingCommentId === comment.id"
              v-model="editContent"
            ></textarea>
            <p v-else>{{ comment.content }}</p>
            <p>{{ formatDate(comment.created_at) }}</p>
          </div>
          
          <!-- 댓글 작성자인 경우에만 수정/삭제 버튼 표시 -->
          <div v-if="isCommentAuthor(comment)">
            <template v-if="editingCommentId === comment.id">
              <button @click="updateComment(comment.id)">저장</button>
              <button @click="cancelEdit">취소</button>
            </template>
            <template v-else>
              <button @click="startEdit(comment)">수정</button>
              <button @click="deleteComment(comment.id)">삭제</button>
            </template>
          </div>
        </div>
      </div>
      <!-- 댓글이 없을 경우 -->
      <p v-else>아직 댓글이 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useEggStore } from '@/stores/egg'

const props = defineProps({
  article: Object,
  comments: Array
})

const emit = defineEmits(['comment-added'])
const store = useEggStore()
const newComment = ref('')           // 새 댓글 내용
const editingCommentId = ref(null)   // 현재 수정 중인 댓글 ID
const editContent = ref('')          // 수정 중인 댓글 내용
const currentUsername = ref(null)    // 현재 로그인한 사용자 이름

// 컴포넌트 마운트 시 현재 사용자 정보 가져오기
onMounted(async () => {
  try {
    const response = await axios({
      method: 'get',
      url: `${store.API_URL}accounts/user/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    currentUsername.value = response.data.username
    console.log('현재 사용자:', currentUsername.value)
  } catch (error) {
    console.error('사용자 정보 가져오기 실패:', error)
  }
})

// 새 댓글 작성
const createComment = async () => {
  if (!newComment.value.trim()) return

  try {
    await axios({
      method: 'post',
      url: `${store.API_URL}articles/${props.article.id}/comments/`,
      data: { content: newComment.value.trim() },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    
    newComment.value = ''
    emit('comment-added')
    
  } catch (error) {
    console.error('댓글 작성 실패:', error)
  }
}

// 댓글 수정 모드 시작
const startEdit = (comment) => {
  editingCommentId.value = comment.id
  editContent.value = comment.content
}

// 댓글 수정 취소
const cancelEdit = () => {
  editingCommentId.value = null
  editContent.value = ''
}

// 댓글 수정 저장
const updateComment = async (commentId) => {
  if (!editContent.value.trim()) return

  try {
    await axios({
      method: 'put',
      url: `${store.API_URL}articles/${props.article.id}/comments/${commentId}/`,
      data: { content: editContent.value.trim() },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    
    editingCommentId.value = null
    editContent.value = ''
    emit('comment-added')  // 부모 컴포넌트에 댓글 수정 알림
    
  } catch (error) {
    console.error('댓글 수정 실패:', error)
  }
}

// 댓글 삭제
const deleteComment = async (commentId) => {
  if (!confirm('정말로 이 댓글을 삭제하시겠습니까?')) return

  try {
    await axios({
      method: 'delete',
      url: `${store.API_URL}articles/${props.article.id}/comments/${commentId}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    
    emit('comment-added')  // 부모 컴포넌트에 댓글 삭제 알림
    
  } catch (error) {
    console.error('댓글 삭제 실패:', error)
  }
}

// 댓글 작성자 확인
const isCommentAuthor = (comment) => {
  return comment.user.username === currentUsername.value
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('ko-KR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>

<style scoped>
/* 댓글 작성 폼 스타일 */
.comment-form {
  margin: 20px 0;
}

/* 댓글 작성 텍스트영역 스타일 */
.comment-form textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  resize: vertical;
}

/* 댓글 아이템 스타일 */
.comment-item {
  padding: 10px;
  border-bottom: 1px solid #eee;
  display: flex;
  justify-content: space-between;
  align-items: start;
}
</style>
