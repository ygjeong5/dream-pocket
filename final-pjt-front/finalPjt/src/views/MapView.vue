<template>
  <div class="mainpage">
    <div class="container">
      <div>
        <label>검색하고 싶은 은행:</label>
        <select id="bankSelector" v-model="selectedBank">
          <option value="" disabled selected>은행을 선택하세요</option>
          <option value="은행">전체검색</option>
          <option value="KB국민은행">KB국민은행</option>
          <option value="신한은행">신한은행</option>
          <option value="하나은행">하나은행</option>
          <option value="우리은행">우리은행</option>
          <option value="NH농협은행">NH농협은행</option>
        </select>
        <button onclick="confirmBank()">확인</button>
      </div>

      <div>
        <label>장소 검색:</label>
        <input type="text" v-model="placeKeyword" placeholder="장소를 입력하세요" />
        <button @click="searchPlace">검색</button>
      </div>
    </div>

    <!-- 카카오 지도 -->
    <KakaoMap width=98% :height="1000" :lat="centerLat" :lng="centerLng" @onLoadKakaoMap="onLoadKakaoMap">
      <KakaoMapMarker
        v-for="(marker, index) in markerList"
        :key="marker.key === undefined ? index : marker.key"
        :lat="marker.lat"
        :lng="marker.lng"
        :infoWindow="marker.infoWindow"
        :clickable="true"
        @mouseOverKakaoMapMarker="mouseOverKakaoMapMarker(marker)"
        @mouseOutKakaoMapMarker="mouseOutKakaoMapMarker(marker)"
      />
    </KakaoMap>
  </div>
</template>


<script setup lang="ts">
import { KakaoMap, KakaoMapMarker, type KakaoMapMarkerListItem } from 'vue3-kakao-maps';
import { ref, watch } from 'vue';



// 지도와 마커 관련 상태
const map = ref<kakao.maps.Map>();
const markerList = ref<KakaoMapMarkerListItem[]>([]);

// 중심 좌표와 검색 키워드 상태
const centerLat = ref(37.566826); // 기본값: 서울 중심
const centerLng = ref(126.9786567); // 기본값: 서울 중심
const placeKeyword = ref(''); // 사용자가 입력한 장소 검색 키워드
const selectedBank = ref("은행")


const searchPlace = () => {
  if (!placeKeyword.value) {
    alert('검색할 장소를 입력해주세요.');
    return;
  }

  const ps = new kakao.maps.services.Places();
  ps.keywordSearch(placeKeyword.value, (data, status) => {
    if (status === kakao.maps.services.Status.OK) {
      const firstResult = data[0];
      if (firstResult) {
        // 중심 좌표를 첫 번째 결과로 업데이트
        const next_lat = parseFloat(firstResult.y);
        const next_lng = parseFloat(firstResult.x);
        const backUpMarkList = markerList.value 

        // 은행 검색 실행
        searchBanks(next_lat, next_lng).then((hasResults) => {
          if (hasResults) {
            centerLat.value = next_lat;
            centerLng.value = next_lng;
            map.value?.setCenter(new kakao.maps.LatLng(centerLat.value, centerLng.value));
          } else {
            alert('해당 지역에서 검색된 은행이 없습니다.');
            markerList.value = backUpMarkList
          }
        });
      } else {
        alert('해당 장소를 찾을 수 없습니다.');
      }
    } else {
      alert('검색에 실패했습니다.');
    }
  });
  placeKeyword.value = ''
};

// 은행 검색
const searchBanks = (lat: number, lng: number): Promise<boolean> => {
  return new Promise((resolve) => {
    const ps = new kakao.maps.services.Places();
    ps.keywordSearch(
      selectedBank.value,
      (data, status) => {
        if (status === kakao.maps.services.Status.OK) {
          const bounds = new kakao.maps.LatLngBounds();
          markerList.value = []; // 기존 마커 초기화

          for (let marker of data) {
            const markerItem: KakaoMapMarkerListItem = {
              lat: marker.y,
              lng: marker.x,
              infoWindow: {
                content: marker.place_name,
                visible: false,
              },
            };
            markerList.value.push(markerItem);
            bounds.extend(new kakao.maps.LatLng(Number(marker.y), Number(marker.x)));
          }
          // 지도 범위 재설정
          map.value?.setBounds(bounds);
          map.value.setLevel(3);

          resolve(true);
        } else {
          markerList.value = []; // 검색 결과가 없을 때 마커 리스트 초기화
          resolve(false);
        }
      },
      {
        category_group_code: 'BK9',
        location: new kakao.maps.LatLng(lat, lng),
        radius: 500,
      }
    )
  })
};

// 키워드 검색 완료 시 호출되는 콜백 함수
const placesSearchCB = (data: kakao.maps.services.PlacesSearchResult, status: kakao.maps.services.Status): void => {
  if (status === kakao.maps.services.Status.OK) {
    const bounds = new kakao.maps.LatLngBounds();
    markerList.value = []; // 기존 마커 초기화
    for (let marker of data) {
      const markerItem: KakaoMapMarkerListItem = {
        lat: marker.y,
        lng: marker.x,
        infoWindow: {
          content: marker.place_name,
          visible: false
        }
      };
      markerList.value.push(markerItem);
      bounds.extend(new kakao.maps.LatLng(Number(marker.y), Number(marker.x)));
    }

      // 지도 범위 재설정
      map.value?.setBounds(bounds);
      map.value.setLevel(3) 
  } else {
    alert('검색결과가 없습니다.')
    
  }
};


// 지도 로드 시 실행되는 함수
const onLoadKakaoMap = (mapRef: kakao.maps.Map) => {
  map.value = mapRef;

  // 초기 은행 검색 실행
  searchBanks(centerLat.value, centerLng.value);

  kakao.maps.event.addListener(map.value, 'click', function (mouseEvent: kakao.maps.event.MouseEvent){
    const latlng = mouseEvent.latLng
    centerLat.value = latlng.getLat()
    centerLng.value = latlng.getLng()
    searchBanks(centerLat.value, centerLng.value)
    
  })

};

// 마커 클릭 시 인포윈도우의 visible 값을 반전시킵니다

const mouseOverKakaoMapMarker = (markerList: KakaoMapMarkerListItem): void => {
  markerList.infoWindow.visible = true
}

const mouseOutKakaoMapMarker = (markerList: KakaoMapMarkerListItem): void => {
  markerList.infoWindow.visible = false
}

watch(selectedBank, (newValue, oldValue) => {
  searchBanks(centerLat.value, centerLng.value).then((hasResults) => {
          if (hasResults) {
            console.log('gg')
          } else {
            alert('해당 지역에서 검색된 은행이 없습니다.');
            selectedBank.value = '은행'
          }
        })
      })





</script>


<style scoped>
.mainpage{
  padding: 10px;
  padding-top: 20px;
  display: flex;
  align-content: center;
  margin: 10px;
}


.container {
  position: absolute;
  top: 20px;
  right: 40px;
  z-index: 10;
  width: 350px;
  background: linear-gradient(145deg, #e8f1f8, #d4e6f1);
  padding: 20px;
  border-radius: 15px;
  border: 3px solid #2980b9;
  box-shadow: 0 4px 0 #85929e;
  display: flex;
  flex-direction: column;
  gap: 15px;
  
}

.container > div {
  display: flex;
  flex-direction: column;
  gap: 10px;
}



label {
  font-family: 'DNFBitBitv2';
  font-size: 1.1rem;
  background: linear-gradient(to left top, #2980b9, #3498db);
  -webkit-background-clip: text;
  -webkit-text-stroke: 1px rgba(39, 54, 154, 0.5);
  color: transparent;
}

select {
  width: 100%;
  padding: 8px 12px;
  border: 2px solid #7fb3d5;
  border-radius: 8px;
  margin: 5px 0;
  font-family: 'Pretendard-Regular';
  box-shadow: 0 2px 0 #85929e;
}

button {
  width: 100%;
  padding: 8px 12px;
  background: white;
  border: 2px solid #7fb3d5;
  border-radius: 8px;
  color: #2980b9;
  font-family: 'DNFBitBitv2';
  cursor: pointer;
  transition: all 0.2s ease;
}

button:hover {
  background: linear-gradient(145deg, #2980b9, #3498db);
  color: white;
}

input[type="text"] {
  width: 100%;
  padding: 8px 12px;
  border: 2px solid #7fb3d5;
  border-radius: 8px;
  margin: 5px 0;
  font-family: 'Pretendard-Regular';
  box-shadow: 0 2px 0 #85929e;
}

@media (max-width: 768px) {
  .container {
    position: relative;
    top: 0;
    right: 0;
    width: 100%;
    margin-bottom: 10px;
  }
}


/* 지도 컨테이너 스타일 추가 */
:deep(.kakao-map-container) {
  width: 100% !important;  /* 지도 너비 조정 */
  height: 80vh !important;  /* 지도 높이 조정 */
  margin: 40px auto !important;  /* 상하 여백과 가운데 정렬 */
  border-radius: 15px;
  border: 3px solid #2980b9;
  box-shadow: 0 6px 0 #85929e;
}

@media (max-width: 768px) {
  :deep(.kakao-map-container) {
    width: 95% !important;
    height: 70vh !important;
  }
}
</style>

