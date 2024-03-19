<template>
	<div class="modal modal-sheet position-static d-block p-4 py-md-5" tabindex="-1" role="dialog" id="modalSignin">
		<div class="modal-dialog" role="document">
			<div class="modal-content rounded-4 shadow">
				<div class="modal-header p-5 pb-4 border-bottom-0">
					<h1 class="fw-bold mb-0 fs-2">{{useI18n().t('login.signUp')}}</h1>
					<button @click="router.back()" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
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
							{{useI18n().t('login.alreadyHaveAnAccount')}} <router-link :to="{ name: 'login', query: { continue: route.query.continue } }" replace>{{useI18n().t('login.login')}}</router-link>
						</small>
					</form>
				</div>
			</div>
		</div>
	</div>
</template>
	
<script setup>
import { useI18n } from 'vue-i18n'
import SubmitButton from '../components/common/SubmitButton.vue'
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Backend from '../js/Backend'

const route = useRoute()
const router = useRouter()
const input = ref({ username: '', password: '' })
const alerts = ref([])
const loading = ref(false)

const SignUp = async () => {
	try {
		alerts.value = []
		loading.value = true
		await Backend.post('/api/users', input.value)
		loading.value = false
		router.replace({ name: 'login', query: { continue: route.query.continue, signup: 'true' } })
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
