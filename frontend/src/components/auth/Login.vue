<template>
    <div ref="loginModal" class="modal fade" id="loginModalToggle" aria-hidden="true" aria-labelledby="loginModalToggleLabel" tabindex="-1">
        <div class="modal-dialog" role="document">
            <div class="modal-content rounded-4 shadow">
            <div class="modal-header p-5 pb-4 border-bottom-0">
                <h1 class="fw-bold mb-0 fs-2"  id="loginModalToggleLabel">{{useI18n().t('login.login')}}</h1>
                <button @click="CloseModal" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body p-5 pt-0">
                <div v-for="alert in alerts" :class="alert.type">
                  <div>{{ alert.message }}</div>
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
                    <input v-model="remember" class="form-check-input" type="checkbox" value="" id="flexCheckChecked" checked>
                    <label class="form-check-label" for="flexCheckChecked">
                        {{useI18n().t('login.rememberMe')}}
                    </label>
                </div>
                <SubmitButton :loading="loading">{{useI18n().t('login.login')}}</SubmitButton>
                <small class="text-body-secondary">{{useI18n().t('login.new?')}} <a href="#signupModalToggle" data-bs-target="#signupModalToggle" data-bs-toggle="modal">{{useI18n().t('login.signUp')}}</a></small>
                <!-- FIXME: <hr class="my-4">
                <h2 class="fs-5 fw-bold mb-3">Or use a third-party</h2>
                <button class="w-100 py-2 mb-2 btn btn-outline-secondary rounded-3" type="submit">
                    <svg class="bi me-1" width="16" height="16"><use xlink:href="#twitter"></use></svg>
                    Sign up with Google
                </button> -->
                </form>
            </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n';
import { onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router'
import Backend from '../../js/Backend'
import SubmitButton from '../common/SubmitButton.vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'
import router from '../../router';
import { globalUser, globalWS } from '../../main.js';

const props = defineProps({ forcelogin: Boolean })
const signedup = defineModel('signedup')
const status = defineModel('status')
const input = { username: '', password: '' }
const loginModal = ref(null)
const alerts = ref([])
const loading = ref(false)
const route = useRoute()
let   remember = true

watch(signedup, (newValue) => {
  if (!newValue) return
  alerts.value.push({
    message: 'Successfuly signed up',
    type: {'alert': true, 'alert-success': true, 'alert-dismissible': true }
  })
  signedup.value = false
})

const CloseModal = () => {
  if (props.forcelogin) {
    router.push({ name: 'home' })
  }
}

onMounted(() => {
  loginModal.value.addEventListener('hidden.bs.modal', () => {
    Object.keys(input).forEach(k => input[k] = '')
    alerts.value = []
  })
})

const LogIn = async () => {
  try {
    alerts.value = []
    loading.value = true
    globalUser.value = await Backend.post('/api/login?remember=' + remember, input)
    loading.value = false
    status.value = true
    localStorage.setItem('globalUser', JSON.stringify(globalUser.value));
    let bsLoginModal = bootstrap.Modal.getInstance("#loginModalToggle")
    bsLoginModal.hide()
    if (props.forcelogin) {
      const urlParams = new URLSearchParams(document.location.search)
      router.replace(decodeURIComponent(urlParams.get('continue')))
    } else if (route.name === 'logout') {
      router.replace({ name: 'home' })
    }
    globalWS.reload()
  } catch (err) {
    globalUser.value = null;
    loading.value = false
    alerts.value.push({
      message: err.message,
      type: { 'alert': true, 'alert-danger': true, 'alert-dismissible': true }
    })

    console.log('login: error: ', err.message)
  }
}
</script>
