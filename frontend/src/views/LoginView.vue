<template>
	<div class="modal modal-sheet position-static d-block p-4 py-md-5" tabindex="-1" role="dialog" id="modalSignin">
		<div class="modal-dialog" role="document">
			<div class="modal-content rounded-4 shadow">
				<div class="modal-header p-5 pb-4 border-bottom-0">
					<h1 class="fw-bold mb-0 fs-2" id="loginModalToggleLabel">{{useI18n().t('login.login')}}</h1>
					<button @click="router.back()" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body p-5 pt-0">
					<div v-for="alert in alerts" :class="alert.type">
						<div>{{ useI18n().t(`err.${alert.message}`)}}</div>
						<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
					</div>
					<form @submit.prevent="LogIn" class="">
						<div class="form-floating mb-3">
							<input v-model="input.username" type="text" class="form-control rounded-3" id="floatingLoginUsername" :placeholder="useI18n().t('username')">
							<label for="floatingLoginUsername">{{useI18n().t('username')}}</label>
						</div>
						<div class="form-floating mb-3">
							<input v-model="input.password" type="password" class="form-control rounded-3" id="floatingLoginPassword" :placeholder="useI18n().t('password')">
							<label for="floatingLoginPassword">{{useI18n().t('password')}}</label>
						</div>
						<div class="form-check my-3">
							<input v-model="remember" class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
							<label class="form-check-label" for="flexCheckChecked">{{useI18n().t('login.rememberMe')}}</label>
						</div>
						<SubmitButton :loading="loading">{{useI18n().t('login.login')}}</SubmitButton>
						<small class="text-body-secondary">
							{{useI18n().t('login.new?')}} <router-link :to="{ name: 'signup', query: { continue: route.query.continue } }" replace>{{useI18n().t('login.signUp')}}</router-link>
						</small>
					</form>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Backend from '../js/Backend'
import SubmitButton from '../components/common/SubmitButton.vue'
import { globalUser, globalWS } from '../main'

const route = useRoute()
const router = useRouter()
const input = ref({ username: '', password: '' })
const remember = ref(true)
const alerts = ref([])
const loading = ref(false)

onMounted(() => {
	if (route.query.signup) {
		alerts.value.push({
			message: 'Successfuly signed up',
			type: {'alert': true, 'alert-success': true, 'alert-dismissible': true }
		})
	}
})

const LogIn = async () => {
	try {
		alerts.value = []
		loading.value = true
		globalUser.value = await Backend.post('/api/login?remember=' + remember.value, input.value)
		loading.value = false
		if (route.query.continue) {
			router.replace(decodeURIComponent(route.query.continue))
		} else if (route.name === 'logout') {
			router.replace({ name: 'home'})
		}
		globalWS.reload()
	} catch (err) {
		globalUser.value = null;
		loading.value = false
		alerts.value.push({
			message: err.message,
			type: { 'alert': true, 'alert-danger': true, 'alert-dismissible': true }
		})
		console.error(err.message)
	}
}
</script>
