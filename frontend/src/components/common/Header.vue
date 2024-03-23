<template>
	<section>
		<header class="p-3 text-bg-dark">
			<div class="container">
				<div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
					<ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
						<div v-for="r in navRoutes" >
							<li v-if="Array.isArray(r.name)" class="nav-item dropdown">
								<a class="nav-link dropdown-toggle px-2 text-white" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">{{useI18n().t(r.button)}}</a>
								<ul class="dropdown-menu dropdown-menu-dark">
									<li v-for="subr in r.name">
										<router-link :to="{ name: subr.name }" :class="[ subr.name === route.name ? activeView : inactiveView, { 'dropdown-item': true }]">{{useI18n().t(subr.button)}}</router-link>
									</li>
								</ul>
							</li>
							<li v-else>
								<router-link :to="{ name: r.name }" :class="[route.name === r.name ? activeView : inactiveView]">{{useI18n().t(r.button)}}</router-link>
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
						<button @click="LogOut" type="button" class="btn btn-secondary">{{useI18n().t('login.logout')}}</button>
					</div>
					<div v-else class="text-end">
						<button type="button" class="btn btn-outline-light me-2" data-bs-target="#loginModalToggle" data-bs-toggle="modal">{{useI18n().t('login.login')}}</button>
						<button type="button" class="btn btn-secondary" data-bs-target="#signupModalToggle" data-bs-toggle="modal">{{useI18n().t('login.signUp')}}</button>
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
import { useI18n } from 'vue-i18n'
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
	'text-white': true,
}
const activeView = {
	'nav-link': true,
	'px-2': true,
	'text-secondary': true,
}
const route = useRoute()
const router = useRouter()
const navRoutes = [
	{ name: 'home', button: 'header.home' },
	{ name: 'friends', button: 'header.friends' },
	{ name: 'users', button: 'header.users' },
	{ name: 'chat', button: 'header.chat' },
	{ name: 'settings', button: 'header.settings' },
	{ name: 'tournaments', button: 'header.tournaments' },
	{ name: [
		{ name: 'game/online', button: 'header.online'},
		{ name: 'game/onsite', button: 'header.onsite' },
		{ name: 'demo', button: 'header.demo'},
	], button: 'header.game'}
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
