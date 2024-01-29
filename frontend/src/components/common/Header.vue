<template>
  <section>
    <header class="p-3 text-bg-dark">
      <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
            <svg class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap"><use xlink:href="#bootstrap"></use></svg>
          </a>

          <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
            <li><a href="#" class="nav-link px-2 text-secondary">Home</a></li>
            <li><a href="#" class="nav-link px-2 text-white">Features</a></li>
            <li><a href="#" class="nav-link px-2 text-white">Pricing</a></li>
            <li><a href="#" class="nav-link px-2 text-white">FAQs</a></li>
            <li><a href="#" class="nav-link px-2 text-white">About</a></li>
          </ul>

          <div v-if="logged">
            <button type="button" class="btn btn-outline-light me-2"><router-link to="/profile">Profile</router-link></button>
            <button @click="LogOut" type="button" class="btn btn-secondary">Logout</button>
          </div>

          <div v-else class="text-end">
            <button type="button" class="btn btn-outline-light me-2" data-bs-target="#loginModalToggle" data-bs-toggle="modal">Login</button>
            <button type="button" class="btn btn-secondary" data-bs-target="#signupModalToggle" data-bs-toggle="modal">Signup</button>
          </div>
        </div>
      </div>
    </header>
    <Login v-model:logged="logged" />
    <Signup />
  </section>
</template>

<script setup>
import Backend from "../../js/Backend"
import { ref } from 'vue'
import router from '../../router'
import Login from '../auth/Login.vue'
import Signup from '../auth/Signup.vue'

let logged = ref(false)

const LogOut = async () => {
  try {
    await Backend.post('/api/logout')
    logged.value = false
    router.push('/')
  } catch (err) {
    console.log('post(/api/logout): error: ' + err.message)
  }
}
</script>

<style scoped>
  a {
   text-decoration: none;
   color: unset;
  }
</style>