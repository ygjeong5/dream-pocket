import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

// vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})

// font awesome
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { faPiggyBank } from '@fortawesome/free-solid-svg-icons'
import { faUser } from '@fortawesome/free-solid-svg-icons'
import { faS } from '@fortawesome/free-solid-svg-icons'

// bootstrap
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

// kakaomap
import { useKakao } from 'vue3-kakao-maps/@utils';

useKakao('5c601815580290a95eddff0a6a13f52c', ['clusterer', 'services', 'drawing']);


// import Swiper JS
import Swiper from 'swiper';
// import Swiper styles
import 'swiper/css';



library.add(faUserSecret, faPiggyBank, fas, faUser)

const app = createApp(App)


app.component('font-awesome-icon', FontAwesomeIcon)

app.use(router)
app.use(pinia)
app.use(vuetify).mount('#app')
