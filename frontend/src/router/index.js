import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import AboutView from '../views/AboutView.vue'
import PainelView from '../views/Painel.vue'
import Termos from '../views/Termos.vue'
import HomePainel from '../views/HomePainel.vue'
import Lancamento from '../views/Lancamento.vue'
import FriendList from '../views/FriendList.vue'
import Pagamentos from '../views/Pagamentos.vue'
import Investimentos from '../views/Investimentos/Lancamento_Investimento'
import Dashboard_Investimento from '../views/Investimentos/Dashboard_Investimento'

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
    {
    path: '/lancamento',
    name: 'Lancamento',
    component: Lancamento
  },
  {
    path: '/friendList',
    name: 'FriendList',
    component: FriendList
  },
  {
    path: '/Pagamentos',
    name: 'Pagamentos',
    component: Pagamentos
  },
    {
    path: '/Investimentos',
    name: 'Investimentos',
    component: Investimentos
  },
    {
    path: '/Dashboard_Investimento',
    name: 'Dashboard_Investimento',
    component: Dashboard_Investimento
  },

  
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
