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
      path: '/registration',
      name: 'registration',
      component: () => import('../views/RegistrationView.vue')
    },
    {
      path: '/createprofile',
      name: 'createprofile',
      component: () => import('../views/CreateProfileView.vue')
    },
    // DASHBOARD
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/DashboardView.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfileView.vue')
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import('../views/SettingsView.vue')
    },
    {
      path: '/friends',
      name: 'friends',
      component: () => import('../views/FriendsView.vue')
    },
    {
      path: '/friends/stats',
      name: 'friends/stats',
      component: () => import('../views/FriendStatsView.vue')
    },
    // TOURNAMENTS
    {
      path: '/tournaments',
      name: 'tournaments',
      component: () => import('../views/TournamentsView.vue')
    },
	{
		path: '/singletournament',
		name: 'singletournament',
		component: () => import('../views/SingleTournamentsView.vue')
	},  
    // GAME
    {
      path: '/game',
      name: 'game',
      component: () => import('../views/GameModesView.vue')
    },
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
      path: '/ponggame',
      name: 'ponggame',
      component: () => import('../views/PongGameView.vue')
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