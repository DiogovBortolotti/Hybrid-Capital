import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import AboutView from '../views/AboutView.vue'
import PainelView from '../views/Painel.vue'

const routes = [
    {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/painel',
    name: 'painel',
    component: PainelView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
