<template>
  <div ref="signupModal" class="modal fade" id="signupModalToggle" aria-hidden="true" aria-labelledby="signupModalToggleLabel" tabindex="-1">
        <div class="modal-dialog" role="document">
            <div class="modal-content rounded-4 shadow">
            <div class="modal-header p-5 pb-4 border-bottom-0">
                <h1 class="fw-bold mb-0 fs-2"  id="signupModalToggleLabel">Sign Up</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body p-5 pt-0">
                <div v-for="alert in alerts" :class="alert.type">
                  <div>{{ alert.message }}</div>
                  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
                <form @submit.prevent="SignUp" class="">
                <div class="form-floating mb-3">
                    <input v-model="input.username" type="text" class="form-control rounded-3" id="floatingInput" placeholder="username">
                    <label for="floatingInput">Username</label>
                </div>
                <div class="form-floating mb-3">
                    <input v-model="input.password" type="password" class="form-control rounded-3" id="floatingPassword" placeholder="Password">
                    <label for="floatingPassword">Password</label>
                </div>
                <SubmitButton :loading="loading">Sign Up</SubmitButton>
                <small class="text-body-secondary">Already an account? <a href="#loginModalToggle" data-bs-target="#loginModalToggle" data-bs-toggle="modal">Log In</a></small>
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
import { onMounted, ref } from "vue";
import Backend from "../../js/Backend";
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'
import SubmitButton from "../common/SubmitButton.vue";

const signedup = defineModel('signedup')
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
        let LoginModel = document.getElementById('loginModalToggle')
        let bsLoginModal = new bootstrap.Modal(LoginModel)
        bootstrap.Modal.getInstance('#signupModalToggle').hide()
        bsLoginModal.show()
        signedup.value = true
    } catch (err) {
        loading.value = false
        alerts.value.push({
            message: err.message,
            type: { 'alert': true, 'alert-danger': true, 'alert-dismissible': true }
        })
        console.log('signup: error: ', err.message)
    }
}

</script>
