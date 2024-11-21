<template>
  <div>
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
        :infoWindow="marker.infoWindow"
        :clickable="true"
        @onClickKakaoMapMarker="onClickMapMarker(marker)"
      />
    </KakaoMap>
  </div>
</template>


<script setup lang="ts">
import { KakaoMap, KakaoMapMarker, type KakaoMapMarkerListItem } from 'vue3-kakao-maps';
import { ref } from 'vue';


// 지도와 마커 관련 상태
const map = ref<kakao.maps.Map>();
const markerList = ref<KakaoMapMarkerListItem[]>([]);

// 중심 좌표와 검색 키워드 상태
const centerLat = ref(37.566826); // 기본값: 서울 중심
const centerLng = ref(126.9786567); // 기본값: 서울 중심
const placeKeyword = ref(''); // 사용자가 입력한 장소 검색 키워드


// 은행 검색
const searchBanks = (lat: number, lng: number) => {
  const ps = new kakao.maps.services.Places();
  ps.keywordSearch(
    '국민은행',
    placesSearchCB,
    {
      location: new kakao.maps.LatLng(lat, lng),
      radius: 1000 // 반경 1000m
    }
  );
};

// 장소 검색 (사용자가 입력한 키워드 기준)
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
        centerLat.value = parseFloat(firstResult.y);
        centerLng.value = parseFloat(firstResult.x);

        // 은행 검색 실행
        searchBanks(centerLat.value, centerLng.value);

        // 지도 중심 이동
        map.value?.setCenter(new kakao.maps.LatLng(centerLat.value, centerLng.value));
      }
    } else {
      alert('해당 장소를 찾을 수 없습니다.');
    }
  });
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
  }
};

// 지도 로드 시 실행되는 함수
const onLoadKakaoMap = (mapRef: kakao.maps.Map) => {
  map.value = mapRef;

  // 초기 은행 검색 실행
  searchBanks(centerLat.value, centerLng.value);
};

// 마커 클릭 시 인포윈도우의 visible 값을 반전시킵니다
const onClickMapMarker = (markerItem: KakaoMapMarkerListItem): void => {
  if (markerItem.infoWindow?.visible !== null && markerItem.infoWindow?.visible !== undefined) {
    markerItem.infoWindow.visible = !markerItem.infoWindow.visible;
  } else {
    markerItem.infoWindow.visible = true;
  }
};
</script>

