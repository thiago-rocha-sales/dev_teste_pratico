import Vue from 'vue'
import VueRouter from 'vue-router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import App from './App.vue'

Vue.use(Buefy)
Vue.use(VueRouter)

import Plataformas from './Plataformas'
import Jogos from './Jogos' 

const routes = [
  { path: '/plataformas', component: Plataformas },
  { path: '/jogos', component: Jogos }
]

const router = new VueRouter({
  routes 
})

// const app = new Vue({
//   router,
//   el: '#app',
//   render: h => h(App)
// }).$mount('#app')

const app = new Vue({
  router,
  el: '#app',
  components: { App },
  template: '<App/>'
}).$mount('#app')
