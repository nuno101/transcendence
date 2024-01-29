<template>
    <div ref="loginModal" class="modal fade" id="loginModalToggle" aria-hidden="true" aria-labelledby="loginModalToggleLabel" tabindex="-1">
        <div class="modal-dialog" role="document">
            <div class="modal-content rounded-4 shadow">
            <div class="modal-header p-5 pb-4 border-bottom-0">
                <h1 class="fw-bold mb-0 fs-2"  id="loginModalToggleLabel">Log In</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body p-5 pt-0">
                <form @submit.prevent="LogIn" class="">
                <div class="form-floating mb-3">
                    <input v-model="input.username" type="text" class="form-control rounded-3" id="floatingInput" placeholder="username">
                    <label for="floatingInput">Username</label>
                </div>
                <div class="form-floating mb-3">
                    <input v-model="input.password" type="password" class="form-control rounded-3" id="floatingPassword" placeholder="Password">
                    <label for="floatingPassword">Password</label>
                </div>
                <div class="form-check my-3">
                    <input v-model="remember" class="form-check-input" type="checkbox" value="" id="flexCheckChecked" checked>
                    <label class="form-check-label" for="flexCheckChecked">
                        Remember me
                    </label>
                </div>
                <button class="w-100 mb-2 btn btn-lg rounded-3 btn-primary" type="submit">Log In</button>
                <small class="text-body-secondary">New? <a href="#signupModalToggle" data-bs-target="#signupModalToggle" data-bs-toggle="modal">Sign up</a></small>
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
import { onMounted, ref } from 'vue';
import Backend from '../../js/Backend'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'

const logged = defineModel('logged')
const input = ref({ username: '', password: '' })
const loginModal = ref(null)
let   remember = true

const AlreadyLoggedin = async () => {
  try {
    await Backend.get('/api/users/me')
    logged.value = true
  } catch {}
}
AlreadyLoggedin()

onMounted(() => {
  loginModal.value.addEventListener('hidden.bs.modal', () => {
    Object.keys(input.value).forEach(k => input.value[k] = '')
  })
})

const LogIn = async () => {
  try {
    await Backend.post('/api/login?remember=' + remember, input.value)
    let bsLoginModal = bootstrap.Modal.getInstance("#loginModalToggle")
    bsLoginModal.hide()
    logged.value = true
  } catch (err) {
    console.log(err.message)
    // TODO: add popup
  }
}
</script>

<style>

</style>