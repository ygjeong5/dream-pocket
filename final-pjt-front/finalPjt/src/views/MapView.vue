<template>
  <div>
    <div class="container">
    <label style="padding-right: 20px;">검색하고 싶은 은행:</label>
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
    {{  selectedBank }}
  </div>
    

    <!-- 장소 검색 입력 폼 -->
    <div>
      <label>
        장소 검색:
        <input type="text" v-model="placeKeyword" placeholder="장소를 입력하세요" />
      </label>
      <button @click="searchPlace">검색</button>
    </div>

  

    <!-- 카카오 지도 -->
    <KakaoMap :lat="centerLat" :lng="centerLng" @onLoadKakaoMap="onLoadKakaoMap">
      <KakaoMapMarker
        v-for="(marker, index) in markerList"
        :key="marker.key === undefined ? index : marker.key"
        :lat="marker.lat"
        :lng="marker.lng"
        :infoWindow= marker.infoWindow
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

