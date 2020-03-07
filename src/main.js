import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import axios from 'axios';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
Vue.prototype.$axios = axios;

Vue.config.productionTip = false

new Vue({
  el:'#app',
  vuetify,
  router,
  render: h => h(App)
})
