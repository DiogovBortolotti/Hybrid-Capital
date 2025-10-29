import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '@/views/Home.vue'
import AboutView from '@/views/AboutView.vue'
import PainelView from '@/views/Painel.vue'
import TermosView from '@/views/Termos.vue'
import HomePainelView from '@/views/HomePainel.vue'
import LancamentoView from '@/views/Lancamento.vue'
import FriendListView from '@/views/FriendList.vue'
import PagamentosView from '@/views/Pagamentos.vue'

// Views de Investimentos
import LancamentoInvestimento from '../views/Investimentos/Lancamento_Investimento.vue';
import DashboardInvestimento from '../views/Investimentos/Dashboard_Investimento.vue';



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
    component: TermosView
  },
    {
    path: '/home-painel',
    name: 'HomePainel',
    component: HomePainelView
  },
    {
    path: '/lancamento',
    name: 'Lancamento',
    component: LancamentoView
  },
  {
    path: '/friendList',
    name: 'FriendList',
    component: FriendListView
  },
  {
    path: '/Pagamentos',
    name: 'Pagamentos',
    component: PagamentosView
  },
    {
    path: '/Investimentos',
    name: 'Investimentos',
    component: LancamentoInvestimento
  },
    {
    path: '/Dashboard_Investimento',
    name: 'Dashboard_Investimento',
    component: DashboardInvestimento
  },

  
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
