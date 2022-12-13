import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Product from '../views/Product.vue'
import Product2 from '../views/Product2.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Recomendation from '../views/Recomendation.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
/*   {
    path:'/:category_slug/:product_slug/',
    name:'Product',
    component: Product
  }, */
  {
    path:'/product2',
    name:'Product',
    component: Product2
  },
  {
    path:'/:username/:id',
    name:'Product',
    component: Product
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/recomendation/:id',
    name: 'recomendation',
    component: Recomendation
  }


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
