import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import AboutView from '../views/AboutView.vue'
import PainelView from '../views/Painel.vue'
import Termos from '../views/Termos.vue'
import HomePainel from '../views/HomePainel.vue'

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
  },
    {
    path: '/termos-e-condicoes',
    name: 'termos',
    component: Termos
  },
    {
    path: '/home-painel',
    name: 'HomePainel',
    component: HomePainel
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
