<template>
	<div ref="signupModal" class="modal fade" id="signupModalToggle" aria-hidden="true" aria-labelledby="signupModalToggleLabel" tabindex="-1">
		<div class="modal-dialog" role="document">
			<div class="modal-content rounded-4 shadow">
				<div class="modal-header p-5 pb-4 border-bottom-0">
					<h1 class="fw-bold mb-0 fs-2"  id="signupModalToggleLabel">{{useI18n().t('login.signUp')}}</h1>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body p-5 pt-0">
					<div v-for="alert in alerts" :class="alert.type">
						<div>{{ alert.message }}</div>
						<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
					</div>
					<form @submit.prevent="SignUp" class="">
						<div class="form-floating mb-3">
							<input v-model="input.username" type="text" class="form-control rounded-3" id="floatingSignupUsername" :placeholder="useI18n().t('username')">
							<label for="floatingSignupUsername">{{useI18n().t('username')}}</label>
						</div>
						<div class="form-floating mb-3">
							<input v-model="input.password" type="password" class="form-control rounded-3" id="floatingSignupPassword" :placeholder="useI18n().t('password')">
							<label for="floatingSignupPassword">{{useI18n().t('password')}}</label>
						</div>
						<SubmitButton :loading="loading">{{useI18n().t('login.signUp')}}</SubmitButton>
						<small class="text-body-secondary">
							{{useI18n().t('login.alreadyHaveAnAccount')}} <a href="#loginModalToggle" data-bs-target="#loginModalToggle" data-bs-toggle="modal">Log In</a>
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
import Backend from '../../js/Backend'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'
import SubmitButton from '../common/SubmitButton.vue'

const signedup = defineModel('signedup')
const props = defineProps({ forcelogin: Boolean })
const input = ref({ username: '', password: '' })
const signupModal = ref(null)
const loading = ref(false)
const alerts = ref([])

onMounted(() => {
	signupModal.value.addEventListener('hidden.bs.modal', () => {
		Object.keys(input.value).forEach(k => input.value[k] = '')
		alerts.value = []
	})
})

const SignUp = async () => {
	try {
		alerts.value = []
		loading.value = true
		await Backend.post('/api/users', input.value)
		loading.value = false
		signedup.value = true
		bootstrap.Modal.getInstance(signupModal.value).hide()
		new bootstrap.Modal(document.getElementById('loginModalToggle')).show()
	} catch (err) {
		loading.value = false
		alerts.value.push({
			message: err.message,
			type: { 'alert': true, 'alert-danger': true, 'alert-dismissible': true }
		})
		console.error(err.message)
	}
}
</script>
