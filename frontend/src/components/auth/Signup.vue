<template>
  <div class="modal fade" id="exampleModalToggle2" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabindex="-1">
        <div class="modal-dialog" role="document">
            <div class="modal-content rounded-4 shadow">
            <div class="modal-header p-5 pb-4 border-bottom-0">
                <h1 class="fw-bold mb-0 fs-2"  id="exampleModalToggleLabel2">Sign Up</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body p-5 pt-0">
                <form @submit.prevent="SignUp" class="">
                <div class="form-floating mb-3">
                    <input v-model="input.username" type="text" class="form-control rounded-3" id="floatingInput" placeholder="username">
                    <label for="floatingInput">Username</label>
                </div>
                <div class="form-floating mb-3">
                    <input v-model="input.password" type="password" class="form-control rounded-3" id="floatingPassword" placeholder="Password">
                    <label for="floatingPassword">Password</label>
                </div>
                <button class="w-100 mb-2 btn btn-lg rounded-3 btn-primary" type="submit">Sign Up</button>
                <small class="text-body-secondary">Already an account? <a href="#aeihf" data-bs-target="#loginModalToggle" data-bs-toggle="modal">Log In</a></small>
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
import Backend from "../../js/Backend";

const input = { username: '', password: '' }

// TODO: clear form if successful
const SignUp = async () => {
    try {
        await Backend.post('/api/users', input)
    } catch (err) {
        console.log('create: error: ', err.message)
        // TODO: add popup
    }
}

</script>

<style>

</style>