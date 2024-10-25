import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

// Importación de vistas
import Home from '../views/Home.vue'
import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import Checkout from '../views/Checkout.vue'
import Success from '../views/Success.vue'

// Definición de rutas
const routes = [
  {
    path: '/', // Ruta principal
    name: 'Home', // Nombre de la ruta
    component: Home // Componente asociado
  },
  {
    path: '/about', // Ruta de "Acerca de"
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue') // Carga diferida
  },
  {
    path: '/sign-up', // Ruta de registro
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in', // Ruta de inicio de sesión
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/my-account', // Ruta de cuenta del usuario
    name: 'MyAccount',
    component: MyAccount,
    meta: { // Requiere inicio de sesión
        requireLogin: true
    }
  },
  {
    path: '/search', // Ruta de búsqueda
    name: 'Search',
    component: Search
  },
  {
    path: '/cart', // Ruta del carrito
    name: 'Cart',
    component: Cart
  },
  {
    path: '/cart/success', // Ruta de éxito de la compra
    name: 'Success',
    component: Success
  },
  {
    path: '/cart/checkout', // Ruta de pago
    name: 'Checkout',
    component: Checkout,
    meta: { // Requiere inicio de sesión
        requireLogin: true
    }
  },
  {
    path: '/:category_slug/:product_slug', // Ruta de producto dinámico
    name: 'Product',
    component: Product
  },
  {
    path: '/:category_slug', // Ruta de categoría dinámica
    name: 'Category',
    component: Category
  }
]

// Creación del router
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL), // Historial web
  routes // Rutas definidas
})

// Guardia de navegación
router.beforeEach((to, from, next) => {
  // Verifica si se requiere inicio de sesión
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } }); // Redirige a inicio de sesión
  } else {
    next() // Continúa a la siguiente ruta
  }
})

export default router // Exporta el router
