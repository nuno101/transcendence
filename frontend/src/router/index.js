import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // AUTH
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/logout',
      name: 'logout',
      component: () => import('../views/Logout.vue')
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import('../views/SettingsView.vue')
    },
    {
      path: '/users',
      name: 'users',
      component: () => import('../views/UsersView.vue')
    },
    {
      path: '/friends',
      name: 'friends',
      component: () => import('../views/FriendsView.vue')
    },
    {
      path: '/users/:id',
      name: 'user stats',
      component: () => import('../views/UserStatsView.vue'),
      props: true
    },
    // TOURNAMENTS
    {
      path: '/tournaments',
      name: 'tournaments',
      component: () => import('../views/TournamentsView.vue')
    },
	{
		path: '/tournaments/:id', 
		name: 'tournaments/id',
		component: () => import('../views/SingleTournamentsView.vue')
	  },
    // GAME
    {
      path: '/game/online',
      name: 'game/online',
      component: () => import('../views/OnlineGameView.vue')
    },   
    {
      path: '/game/onsite',
      name: 'game/onsite',
      component: () => import('../views/OnsiteGameView.vue')
    },   
    {
      path: '/ponggame/:id',
      name: 'ponggame',
      component: () => import('../views/PongGameView.vue'),
      props: true
    },
    // Chat
    {
      path: '/chat/:id?',
      name: 'chat',
      component: () => import('../views/ChatView.vue')
    },
    // FALLBACK
    {
      path: '/:pathMatch(.*)*',
      name: 'pathnotfound',
      component: () => import('../views/PageNotFoundView.vue')
    }
  ]
})

export default router


// route level code-splitting
// this generates a separate chunk (About.[hash].js) for this route
// which is lazy-loaded when the route is visited.
// component: () => import('../views/LoginView.vue')
// instead of component: LoginView