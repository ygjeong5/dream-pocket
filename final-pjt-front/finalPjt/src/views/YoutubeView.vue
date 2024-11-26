<template>
  <div class="youtube-view">
    <h1>유튜브 동영상 목록</h1>
    <div class="video-list">
      <div 
        v-for="video in videos" 
        :key="video.id" 
        class="video-item"
      >
        <a :href="`${video.url}`" target="_blank" rel="noopener noreferrer">
          <img :src="video.thumbnail" :alt="video.title" class="video-thumbnail" />
          <p class="video-title">{{ video.title }}</p>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
const videos = [
  {
    id: "video_id_1",
    title: "[부자되는 재테크] 은행원도 알려주지 않는 예금과 적금 활용법!! - 1억을 모으는 방법 #.13",
    url: 'https://youtu.be/aZxYnGO_7wo?si=yhlR5X_A_k8cmnxC',
    thumbnail: "thumbnail/thumbnail1.jpg",
    },
  {
    id: "video_id_2",
    title: "재테크, 지금도 늦었다.",
    url: 'https://youtu.be/SpWz5Q4OS1A?si=eGkVJKJBXKmyajtt',
    thumbnail: "thumbnail/thumbnail2.jpg",
  },
  {
    id: "video_id_3",
    title: '슈카쌤 "설마 이걸 모르지는 않겠지"',
    url: 'https://youtu.be/X1L5w_pBRhY?si=5kH_OPKp4AZkfG2n',
    thumbnail: "thumbnail/thumbnail3.jpg",
  },
  {
    id: "video_id_4",
    title: "[경제가 군금해?!] EP 02. 투자성향이 군금해?!",
    url: 'https://www.youtube.com/watch?v=FGUUw2Jw_qs',
    thumbnail: "thumbnail/thumbnail4.jpg",
  },
  {
    id: "video_id_5",
    title: "기초편3(금리). 금리가 당신의 삶에 미치는 영향",
    url: 'https://www.youtube.com/watch?v=fI_u8STJtAc',
    thumbnail: "thumbnail/thumbnail5.jpg",
  },
  {
    id: "video_id_6",
    title: "[Full] 나의 두 번째 교과서 - 경제 3강 금리와 환율, 밀고 당기는 돈의 역학",
    url: 'https://www.youtube.com/watch?v=1Onp3C6jYYE',
    thumbnail: "thumbnail/thumbnail6.jpg",
  },
  {
    id: "video_id_7",
    title: "혹시 청년이세요? 🙋‍ 2024 달라진 청년 지원 정책 종합 선물 풀어보기! 🎁 S3 Ep.3 | 기획재정부",
    url: 'https://www.youtube.com/watch?v=CEU2_xjoguY',
    thumbnail: "thumbnail/thumbnail7.jpg",
  },
  {
    id: "video_id_8",
    title: "[재테크의 정석] 파킹통장이 뭐지?? (예적금을 이븐하게 곁들인..)",
    url: 'https://www.youtube.com/watch?v=bJjN2vrp-Oc',
    thumbnail: "thumbnail/thumbnail8.jpg",
  },
  {
    id: "video_id_9",
    title: "재테크, 지금도 안늦었다.",
    url: 'https://www.youtube.com/watch?v=7VDvW1zCZ8c',
    thumbnail: "thumbnail/thumbnail9.jpg",
  },
  {
    id: "video_id_10",
    title: "[주식] 드디어 배운 '재무제표' 읽는법(홍진경,슈카) [공부왕찐천재]",
    url: 'https://www.youtube.com/watch?v=bE1iSUYA0KI',
    thumbnail: "thumbnail/thumbnail10.jpg",
  },
  {
    id: "video_id_11",
    title: "[경제가 군금해?!] EP 03. 신용이 군금해?!",
    url: 'https://www.youtube.com/watch?v=_khYfd7zDSk',
    thumbnail: "thumbnail/thumbnail11.jpg",
  },
  {
    id: "video_id_12",
    title: "주식 초보라면 꼭 알아둬야 할 차트 보는 방법",
    url: 'https://www.youtube.com/watch?v=hI3pzjLbOzY',
    thumbnail: "thumbnail/thumbnail12.jpg",
  },
  {
    id: "video_id_13",
    title: "[2024 미국 대선-반도체산업] 美 대선 이후 반도체 산업 영향과 그에 따른 대응방안에 대해 알아봤습니다🧐",
    url: 'https://www.youtube.com/watch?v=ZZ-weu_Ck7A',
    thumbnail: "thumbnail/thumbnail13.jpg",
  },
  {
    id: "video_id_14",
    title: "가장 기본적인 투자방법",
    url: 'https://www.youtube.com/watch?v=5lHHAxyXI_g',
    thumbnail: "thumbnail/thumbnail14.jpg",
  },
];
</script>

<style scoped>
.youtube-view {
  padding: 20px;
}

.video-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.video-item {
  width: 200px;
  text-align: center;
}

.video-thumbnail {
  width: 100%;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.video-title {
  margin-top: 10px;
  font-size: 16px;
  font-weight: bold;
  color: #333;
}
</style>
