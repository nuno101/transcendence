import { createRouter, createWebHistory } from 'vue-router';
// IMPORT NEW VIEWS/PAGES HERE
import HomeView from '../views/HomeView.vue';
import LoginView from '../views/LoginView.vue';
import RegistrationView from '../views/RegistrationView.vue';
import CreateProfileView from '../views/CreateProfileView.vue';
import DashboardView from '../views/DashboardView.vue';
import ProfileView from '../views/ProfileView.vue';
import SettingsView from '../views/SettingsView.vue';
import FriendsView from '../views/FriendsView.vue';
import FriendStatsView from '../views/FriendStatsView.vue';
import TournamentsView from '../views/TournamentsView.vue';
import GameModesView from '../views/GameModesView.vue';
import OnlineGameView from '../views/OnlineGameView.vue';
import OnsiteGameView from '../views/OnsiteGameView.vue';

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
      component: () => import('../views/CreateProfileView.vue')
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
    }
  ]
})

export default router


// route level code-splitting
// this generates a separate chunk (About.[hash].js) for this route
// which is lazy-loaded when the route is visited.
// component: () => import('../views/LoginView.vue')
// instead of component: LoginView