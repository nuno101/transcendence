<template>
  <section>
    <header class="p-3 text-bg-dark">
      <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
            <li v-for="e in navRoutes" :key="e.route">
              <router-link :to="'/' + e.route" :class="[route.name === e.route ? activeView : inactiveView]">{{ e.button }}</router-link>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" :class="[gameRoutes.includes(route.name) ? activeView : inactiveView]" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Game</a>
              <ul class="dropdown-menu">
                <li><router-link to="/game/online" class="dropdown-item">online</router-link></li>
                <li><router-link to="/game/onsite" class="dropdown-item">onsite</router-link></li>
              </ul>
            </li>
          </ul>
          
          <div v-if="!logged.loaded" class="text-end">
            <button type="button" class="btn btn-outline-light btn-empty disabled placeholder me-2" data-bs-target="#loginModalToggle" data-bs-toggle="modal"></button>
            <button type="button" class="btn btn-secondary btn-empty disabled placeholder" data-bs-target="#signupModalToggle" data-bs-toggle="modal"></button>
          </div>
          <div v-else-if="logged.status">
            <button type="button" class="btn btn-outline-light me-2">
              <router-link to="/profile" class="nav-link px-2 text-white">Profile</router-link>
            </button>
            <button @click="LogOut" type="button" class="btn btn-secondary">Logout</button>
          </div>
          <div v-else class="text-end">
            <button type="button" class="btn btn-outline-light me-2" data-bs-target="#loginModalToggle" data-bs-toggle="modal">Login</button>
            <button type="button" class="btn btn-secondary" data-bs-target="#signupModalToggle" data-bs-toggle="modal">Signup</button>
          </div>
        </div>
      </div>
    </header>
    <Login
      :logged="logged"
      :signedup="signedup"
      :forcelogin="forcelogin" />
    <Signup
      :signedup="signedup"
      :forcelogin="forcelogin"/>
  </section>
</template>

<script setup>
import Backend from "../../js/Backend"
import { ref } from 'vue'
import router from '../../router'
import Login from '../auth/Login.vue'
import Signup from '../auth/Signup.vue'
import { useRoute } from 'vue-router'
import { watch } from "vue"
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'

const logged = ref({ loaded: false, status: false })
const signedup = ref(false) 

const inactiveView = {
  'nav-link': true,
  'px-2': true,
  'text-white': true
}

const activeView = {
  'nav-link': true,
  'px-2': true,
  'text-secondary': true
}

const route = useRoute()
const navRoutes = [
  { route: 'dashboard', button: 'Dashboard' },
  { route: 'friends', button: 'Friends' },
  { route: 'settings', button: 'Settings' },
  { route: 'tournaments', button: 'Tournaments' },
]
const logoutRoute = { name: 'home' }
const gameRoutes = ['game/online', 'game/onsite', 'ponggame']
const restrictedRoutes = ['tournaments']
const forcelogin = ref(false)

watch(route, (newRoute) => {
  if (!logged.value.status && restrictedRoutes.includes(newRoute.name))
    router.push('/login?continue=' + encodeURIComponent(route.name))
  if (newRoute.name === 'login') {
    let LoginModel = document.getElementById('loginModalToggle')
    let bsLoginModal = new bootstrap.Modal(LoginModel)
    bsLoginModal.show()
    forcelogin.value = true
  } else {
    forcelogin.value = false
  }
})

const AlreadyLoggedin = async () => {
  try {
    await Backend.get('/api/users/me')
    logged.value.status = true;
  } catch {}
  logged.value.loaded = true;
}
AlreadyLoggedin()

const LogOut = async () => {
  try {
    await Backend.post('/api/logout')
    logged.value.status = false
    router.push(logoutRoute)
  } catch (err) {
    console.log('post(/api/logout): error: ' + err.message)
  }
}
</script>

<style>
  .btn-empty {
    width: 5rem;
  }
</style>
