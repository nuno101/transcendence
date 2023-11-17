import { createRouter, createWebHistory } from 'vue-router';
// IMPORT NEW VIEWS/PAGES HERE
import HomeView from '../views/HomeView.vue';
import HomePage from '../views/HomePage.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/homepage',
      name: 'homepage',
      component: () => import('../views/HomePage.vue')
    }
  ]
})

export default router
