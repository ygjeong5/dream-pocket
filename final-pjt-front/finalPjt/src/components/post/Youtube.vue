<template>
  <div class="youtube-view">
    <div class="video-list">
      <div 
        v-for="video in videos" 
        :key="video.id" 
        class="video-item"
      >
        <a :href="video.url" target="_blank" rel="noopener noreferrer" class="video-link">
          <div class="video-card">
            <img :src="video.thumbnail" :alt="video.title" class="video-thumbnail" />
            <div class="video-overlay">
              <div class="video-title">{{ video.title }}</div>
            </div>
          </div>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
const videos = [
  { id: "video_id_1", title: "[부자되는 재테크] 은행원도 알려주지 않는 예금과 적금 활용법!! - 1억을 모으는 방법 #.13", url: 'https://youtu.be/aZxYnGO_7wo?si=yhlR5X_A_k8cmnxC', thumbnail: "thumbnail/thumbnail1.jpg" },
  { id: "video_id_2", title: "재테크, 지금도 늦었다.", url: 'https://youtu.be/SpWz5Q4OS1A?si=eGkVJKJBXKmyajtt', thumbnail: "thumbnail/thumbnail2.jpg" },
  { id: "video_id_3", title: '슈카쌤 "설마 이걸 모르지는 않겠지"', url: 'https://youtu.be/X1L5w_pBRhY?si=5kH_OPKp4AZkfG2n', thumbnail: "thumbnail/thumbnail3.jpg" },
  { id: "video_id_4", title: "[경제가 군금해?!] EP 02. 투자성향이 군금해?!", url: 'https://www.youtube.com/watch?v=FGUUw2Jw_qs', thumbnail: "thumbnail/thumbnail4.jpg" },
  { id: "video_id_5", title: "기초편3(금리). 금리가 당신의 삶에 미치는 영향", url: 'https://www.youtube.com/watch?v=fI_u8STJtAc', thumbnail: "thumbnail/thumbnail5.jpg" },
  { id: "video_id_6", title: "[Full] 나의 두 번째 교과서 - 경제 3강 금리와 환율, 밀고 당기는 돈의 역학", url: 'https://www.youtube.com/watch?v=1Onp3C6jYYE', thumbnail: "thumbnail/thumbnail6.jpg" },
  { id: "video_id_7", title: "혹시 청년이세요? 🙋‍ 2024 달라진 청년 지원 정책 종합 선물 풀어보기! 🎁 S3 Ep.3 | 기획재정부", url: 'https://www.youtube.com/watch?v=CEU2_xjoguY', thumbnail: "thumbnail/thumbnail7.jpg" },
  { id: "video_id_8", title: "[재테크의 정석] 파킹통장이 뭐지?? (예적금을 이븐하게 곁들인..)", url: 'https://www.youtube.com/watch?v=bJjN2vrp-Oc', thumbnail: "thumbnail/thumbnail8.jpg" },
  { id: "video_id_9", title: "재테크, 지금도 안늦었다.", url: 'https://www.youtube.com/watch?v=7VDvW1zCZ8c', thumbnail: "thumbnail/thumbnail9.jpg" },
  { id: "video_id_10", title: "[주식] 드디어 배운 '재무제표' 읽는법(홍진경,슈카) [공부왕찐천재]", url: 'https://www.youtube.com/watch?v=bE1iSUYA0KI', thumbnail: "thumbnail/thumbnail10.jpg" },
  { id: "video_id_11", title: "[경제가 군금해?!] EP 03. 신용이 군금해?!", url: 'https://www.youtube.com/watch?v=_khYfd7zDSk', thumbnail: "thumbnail/thumbnail11.jpg" },
  { id: "video_id_12", title: "주식 초보라면 꼭 알아둬야 할 차트 보는 방법", url: 'https://www.youtube.com/watch?v=hI3pzjLbOzY', thumbnail: "thumbnail/thumbnail12.jpg" },
  { id: "video_id_13", title: "[2024 미국 대선-반도체산업] 美 대선 이후 반도체 산업 영향과 그에 따른 대응방안에 대해 알아봤습니다🧐", url: 'https://www.youtube.com/watch?v=ZZ-weu_Ck7A', thumbnail: "thumbnail/thumbnail13.jpg" },
  { id: "video_id_14", title: "가장 기본적인 투자방법", url: 'https://www.youtube.com/watch?v=5lHHAxyXI_g', thumbnail: "thumbnail/thumbnail14.jpg" }
];
</script>

<style scoped>
.youtube-view {
  padding: 20px;
  background-color: #f7f9fc;
}

.page-title {
  text-align: center;
  font-size: 28px;
  margin-bottom: 30px;
  color: #2c3e50;
  font-family: 'Pretendard', sans-serif;
}

.video-list {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 한 줄에 4개 */
  gap: 20px;
  justify-items: center;
}

.video-item {
  width: 100%;
  text-align: center;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  background: #fff;
  overflow: hidden;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.video-item:hover {
  transform: scale(1.05);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.2);
}

.video-link {
  display: block;
  text-decoration: none;
  color: inherit;
}

.video-card {
  position: relative;
}

.video-thumbnail {
  width: 100%;
  height: 250px; /* 카드의 높이를 크게 조정 */
  object-fit: cover;
  border-radius: 8px;
}

.video-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  border-radius: 8px;
}

.video-card:hover .video-overlay {
  opacity: 1;
}

.video-title {
  font-size: 18px;
  font-weight: bold;
  color: #fff;
  text-align: center;
  margin-top: 10px;
  padding: 10px;
}
</style>
