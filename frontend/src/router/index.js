import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { globalUser } from '../main'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'

const Header = () => import ('../components/common/Header.vue')

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		// AUTH
		{
			path: '/',
			name: 'home',
			components: {
				default: HomeView,
				Header,
			}
		},
		{
			path: '/loading',
			name: 'getuser',
			components: {
				default: () => import('../views/GetUserView.vue'),
				Header,
			}
		},
		{
			path: '/login',
			name: 'login',
			component: () => import('../views/LoginView.vue')
		},
		{
			path: '/signup',
			name: 'signup',
			component: () => import('../views/SignupView.vue')
		},
		{
			path: '/logout',
			name: 'logout',
			components: {
				default: () => import('../views/Logout.vue'),
				Header,
			}
		},
		{
			path: '/settings',
			name: 'settings',
			components: {
				default: () => import('../views/SettingsView.vue'),
				Header,
			}
		},
		{
			path: '/users',
			name: 'users',
			components: {
				default: () => import('../views/UsersView.vue'),
				Header,
			}
		},
		{
			path: '/friends',
			name: 'friends',
			components: {
				default: () => import('../views/FriendsView.vue'),
				Header,
			}
		},
		{
			path: '/users/:id',
			name: 'user stats',
			components: {
				default: () => import('../views/UserStatsView.vue'),  
				Header,
			},
			props: { default: true, Header: false }
		},
		// TOURNAMENTS
		{
			path: '/tournaments',
			name: 'tournaments',
			components: {
				default: () => import('../views/TournamentsView.vue'),
				Header,
			}
		},
		{
			path: '/tournaments/:id', 
			name: 'tournaments/id',
			components: {
				default: () => import('../views/SingleTournamentsView.vue'),
				Header,
			}
		},
		// GAME
		{
			path: '/game/online',
			name: 'game/online',
			components: {
				default: () => import('../views/OnlineGameView.vue'),
				Header,
			}
		},   
		{
			path: '/game/onsite',
			name: 'game/onsite',
			components: {
				default: () => import('../views/OnsiteGameView.vue'),
				Header,
			}
		},   
		{
			path: '/ponggame/:id',
			name: 'ponggame',
			components: {
				default: () => import('../views/PongGameView.vue'),
				Header,
			},
			props: { default: true, Header: false }
		},
		// Chat
		{
			path: '/chat/:id?',
			name: 'chat',
			components: {
				default: () => import('../views/ChatView.vue'),
				Header,
			}
		},
		// FALLBACK
		{
			path: '/:pathMatch(.*)*',
			name: 'pathnotfound',
			components: {
				default: () => import('../views/PageNotFoundView.vue'),
				Header,
			}
		}
	]
})

const restrictedRoutes = ['users', 'friends', 'settings', 'chat', 'tournaments', 'user stats', 'game/onsite' , 'game/online', 'ponggame']

router.beforeEach((to) => {
	document.querySelectorAll('.modal.fade').forEach(modal => bootstrap.Modal.getInstance(modal)?.hide())
	
	if (globalUser.value === undefined && to.name !== 'getuser') {
		router.replace({ name: 'getuser', query: { continue: encodeURIComponent(to.fullPath) } })
	} else if (restrictedRoutes.includes(to.name) && globalUser.value === null) {
		router.push({ name: 'login', query: { continue: encodeURIComponent(to.fullPath) } })
	}
})

export default router

// route level code-splitting
// this generates a separate chunk (About.[hash].js) for this route
// which is lazy-loaded when the route is visited.
// component: () => import('../views/LoginView.vue')
// instead of component: LoginView
