<template>
	<div ref="loginModal" class="modal fade" id="loginModalToggle" aria-hidden="true" aria-labelledby="loginModalToggleLabel" tabindex="-1">
		<div class="modal-dialog" role="document">
			<div class="modal-content rounded-4 shadow">
				<div class="modal-header p-5 pb-4 border-bottom-0">
					<h1 class="fw-bold mb-0 fs-2" id="loginModalToggleLabel">{{ i18n.t('login.login') }}</h1>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body p-5 pt-0">
					<div v-for="alert in alerts" :class="alert.type">
						<div>{{ i18n.te(`err.${alert.message}`) ? i18n.t(`err.${alert.message}`) :  alert.message }}</div>
						<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
					</div>
					<form @submit.prevent="LogIn" class="">
						<div class="form-floating mb-3">
							<input v-model="input.username" type="text" class="form-control rounded-3" id="floatingLoginUsername" :placeholder="i18n.t('username')">
							<label for="floatingLoginUsername">{{ i18n.t('username') }}</label>
						</div>
						<div class="form-floating mb-3">
							<input v-model="input.password" type="password" class="form-control rounded-3" id="floatingLoginPassword" :placeholder="i18n.t('password')">
							<label for="floatingLoginPassword">{{ i18n.t('password') }}</label>
						</div>
						<div class="form-check my-3">
							<input v-model="remember" class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
							<label class="form-check-label" for="flexCheckChecked">{{ i18n.t('login.rememberMe') }}</label>
						</div>
						<SubmitButton :loading="loading">{{ i18n.t('login.login') }}</SubmitButton>
						<small class="text-body-secondary">
							{{ i18n.t('login.new?') }} <a href="#signupModalToggle" data-bs-target="#signupModalToggle" data-bs-toggle="modal">{{ i18n.t('login.signUp') }}</a>
						</small>
					</form>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { onMounted, ref, watch } from 'vue'
import Backend from '../../js/Backend'
import SubmitButton from '../common/SubmitButton.vue'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'
import { globalUser, globalWS } from '../../main.js'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const signedup = defineModel('signedup')
const input = ref({ username: '', password: '' })
const remember = ref(true)
const loginModal = ref(null)
const alerts = ref([])
const loading = ref(false)
const i18n = useI18n()

watch(signedup, (newValue) => {
	if (!newValue) return
	alerts.value.push({
		message: i18n.t('login.successfullySignedUp'),
		type: {'alert': true, 'alert-success': true, 'alert-dismissible': true }
	})
	signedup.value = false
})

onMounted(() => {
	loginModal.value.addEventListener('hidden.bs.modal', () => {
		Object.keys(input.value).forEach(k => input.value[k] = '')
		alerts.value = []
	})
})

const LogIn = async () => {
	try {
		alerts.value = []
		loading.value = true
		globalUser.value = await Backend.post('/api/login?remember=' + remember.value, input.value)
		loading.value = false
		bootstrap.Modal.getInstance(loginModal.value).hide()
		globalWS.reload()
		if (route.name === 'logout') {
			router.replace({ name: 'home'})
		}
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
