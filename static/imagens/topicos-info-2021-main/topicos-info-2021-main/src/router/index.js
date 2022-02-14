import Vue from 'vue'
import VueRouter from 'vue-router'
import Contador from '../views/Contador.vue'
import Produtos from '../views/Produtos.vue'
import Noticias from '../views/Noticias.vue'
import Sobre from '../views/Sobre.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/contador',
    name: 'Contador',
    component: Contador
  },
  {
    path: '/produtos',
    name: 'Produtos',
    component: Produtos
  },
  {
    path: '/noticias',
    name: 'Notícias Interno',
    component: Noticias
  },
  {
    path: '/sobre',
    name: 'Sobre',
    component: Sobre
  },
]

const router = new VueRouter({
  routes
})

export default router
