<template>
  <section>
    <header class="p-3 text-bg-dark">
      <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
            <li v-for="e in navRoutes" :key="e.route">
              <router-link :to="'/' + e.route" :class="[routeName === e.route ? activeView : inactiveView]">{{ e.button }}</router-link>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" :class="[gameRoutes.includes(routeName) ? activeView : inactiveView]" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Game</a>
              <ul class="dropdown-menu">
                <li><router-link to="/game/online" class="dropdown-item">online</router-link></li>
                <li><router-link to="/game/onsite" class="dropdown-item">onsite</router-link></li>
              </ul>
            </li>
          </ul>
          
          <div v-if="logged">
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
    <Login v-model:logged="logged" v-model:signedup="signedup" />
    <Signup v-model:signedup="signedup"/>
  </section>
</template>

<script setup>
import Backend from "../../js/Backend"
import { ref, watch } from 'vue'
import router from '../../router'
import Login from '../auth/Login.vue'
import Signup from '../auth/Signup.vue'
import { useRoute } from 'vue-router'

const logged = ref(false)
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
let routeName = ref(null)
const navRoutes = [
  { route: 'dashboard', button: 'Dashboard' },
  { route: 'friends', button: 'Friends' },
  { route: 'settings', button: 'Settings' },
  { route: 'tournaments', button: 'Tournaments' },
]
const gameRoutes = ['game/online', 'game/onsite', 'ponggame']

watch(route, async (newroute) => routeName.value = newroute.name)

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
