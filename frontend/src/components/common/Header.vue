<template>
	<section>
		<header class="p-3 text-bg-dark">
			<div class="container">
				<div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
					<ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
						<div v-for="r in navRoutes" >
							<li v-if="Array.isArray(r.name)" class="nav-item dropdown">
								<a class="nav-link dropdown-toggle" :class="[r.name.some(e => e.name.includes(route.name)) ? activeView : inactiveView]" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">{{ r.button }}</a>
								<ul class="dropdown-menu">
									<li v-for="subr in r.name">
										<router-link :to="{ name: subr.name }" class="dropdown-item">{{ subr.button }}</router-link>
									</li>
								</ul>
							</li>
							<li v-else>
								<router-link :to="{ name: r.name }" :class="[route.name === r.name ? activeView : inactiveView]">{{ r.button }}</router-link>
							</li>
						</div>
					</ul>
					<div v-if="globalUser === undefined" class="text-end">
						<button type="button" class="btn btn-outline-light btn-empty disabled placeholder me-2" data-bs-target="#loginModalToggle" data-bs-toggle="modal"></button>
						<button type="button" class="btn btn-secondary btn-empty disabled placeholder" data-bs-target="#signupModalToggle" data-bs-toggle="modal"></button>
					</div>
					<div v-else-if="globalUser">
						<button type="button" class="btn btn-outline-info me-2 btn-empty">
							<router-link :to="`/users/${globalUser.id}`" class="nav-link">{{ globalUser.nickname }}</router-link>
						</button>
						<button @click="LogOut" type="button" class="btn btn-secondary">Logout</button>
					</div>
					<div v-else class="text-end">
						<button type="button" class="btn btn-outline-light me-2" data-bs-target="#loginModalToggle" data-bs-toggle="modal">Login</button>
						<button type="button" class="btn btn-secondary" data-bs-target="#signupModalToggle" data-bs-toggle="modal">Signup</button>
					</div>
					<div v-if="globalUser" class="position-relative ms-3">
						<Notifications />
					</div>
				</div>
			</div>
		</header>
		<Login v-model:signedup="signedup" />
		<Signup v-model:signedup="signedup" />
	</section>
</template>

<script setup>
import Backend from '../../js/Backend'
import { ref } from 'vue'
import Login from '../auth/Login.vue'
import Signup from '../auth/Signup.vue'
import Notifications from '../common/Notifications.vue'
import { useRoute, useRouter } from 'vue-router'
import { globalUser } from '../../main'

const signedup = ref(false) 
const inactiveView = {
	'nav-link': true,
	'px-2': true,
	'text-white': true
}
const activeView = {
	'nav-link': true,
	'px-2': true,
	'text-secondary': true
}
const route = useRoute()
const router = useRouter()
const navRoutes = [
	{ name: 'home', button: 'Home' },
	{ name: 'friends', button: 'Friends' },
	{ name: 'chat', button: 'Chat' },
	{ name: 'settings', button: 'Settings' },
	{ name: 'tournaments', button: 'Tournaments' },
	{ name: [
		{ name: 'game/online', button: 'online'},
		{ name: 'game/onsite', button: 'onsite' }
	], button: 'Game'}
]
const logoutRoute = { name: 'logout' }

const LogOut = async () => {
	try {
		await Backend.post('/api/logout', {})
		globalUser.value = null;
		router.push(logoutRoute)
	} catch (err) {
		console.error(err.message)
	}
}
</script>

<style scoped>
	header button {
		min-width: 5rem;
	}
</style>
