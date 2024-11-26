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
    emit('comment-added')  // 부모 컴포넌트에 ���글 수정 알림
    
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
h3 {
  font-family: 'DNFBitBitv2';
  font-size: 1.5rem;
  background: linear-gradient(to left top, #2980b9, #3498db);
  -webkit-background-clip: text;
  -webkit-text-stroke: 1px rgba(39, 54, 154, 0.726);
  color: transparent;
  margin-bottom: 1rem;
}

/* 댓글 작성 폼 스타일 */
.comment-form {
  background: white;
  padding: 1rem;
  border: 2px solid #7fb3d5;
  border-radius: 12px;
  box-shadow: 0 3px 0 #85929e;
  margin-bottom: 1.5rem;
}

.comment-form textarea {
  width: 100%;
  padding: 0.8rem;
  border: 2px solid #7fb3d5;
  border-radius: 8px;
  font-size: 0.9rem;
  min-height: 80px;
  resize: vertical;
  margin-bottom: 0.8rem;
  transition: all 0.3s ease;
}

.comment-form textarea:focus {
  outline: none;
  border-color: #2980b9;
  box-shadow: 0 0 0 2px rgba(41, 128, 185, 0.1);
}

.comment-form button {
  padding: 0.5rem 1rem;
  border: 2px solid #7fb3d5;
  border-radius: 15px;
  font-family: 'DNFBitBitv2';
  font-size: 13px;
  cursor: pointer;
  background: linear-gradient(145deg, #2980b9, #3498db);
  color: white;
  box-shadow: 0 3px 0 #85929e;
  transition: all 0.2s ease;
}

.comment-form button:hover {
  transform: translateY(2px);
  box-shadow: 0 2px 0 #85929e;
}

/* 댓글 목록 스타일 */
.comments-list {
  background: white;
  padding: 1rem;
  border: 2px solid #7fb3d5;
  border-radius: 12px;
  box-shadow: 0 3px 0 #85929e;
}

.comment-item {
  padding: 0.8rem;
  border-bottom: 1px solid #e8f1f8;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  transition: all 0.3s ease;
}

.comment-item:last-child {
  border-bottom: none;
}

.comment-content {
  flex: 1;
  margin-right: 1rem;
}

.comment-content p:first-child {
  font-family: 'DNFBitBitv2';
  color: #2980b9;
  margin-bottom: 0.3rem;
}

.comment-content textarea {
  width: 100%;
  padding: 0.6rem;
  border: 2px solid #7fb3d5;
  border-radius: 8px;
  margin: 0.3rem 0;
  min-height: 60px;
  resize: vertical;
}

.comment-content p:last-child {
  color: #666;
  font-size: 0.8rem;
  margin-top: 0.3rem;
}

/* 댓글 버튼 스타일 */
.comment-item button {
  padding: 0.4rem 0.8rem;
  border: 2px solid #7fb3d5;
  border-radius: 12px;
  font-family: 'DNFBitBitv2';
  font-size: 12px;
  cursor: pointer;
  background: white;
  color: #2980b9;
  margin-left: 0.3rem;
  box-shadow: 0 2px 0 #85929e;
  transition: all 0.2s ease;
}

.comment-item button:hover {
  background: linear-gradient(145deg, #2980b9, #3498db);
  color: white;
  transform: translateY(2px);
  box-shadow: 0 1px 0 #85929e;
}

/* 빈 댓글 메시지 */
.comments-list > p {
  text-align: center;
  padding: 1.5rem;
  color: #666;
  font-family: 'DNFBitBitv2';
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.comment-item {
  animation: fadeIn 0.3s ease-out;
}
</style>
