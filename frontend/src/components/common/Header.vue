<template>
  <section>
    <header class="p-3 text-bg-dark">
      <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
            <div v-for="r in navRoutes" >
              <li v-if="Array.isArray(r.name)" class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" :class="[r.name.some(e => e.name.includes(route.name)) ? activeView : inactiveView]" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">{{useI18n().t(r.button)}}</a>
                <ul class="dropdown-menu">
                  <li v-for="subr in r.name">
                    <router-link :to="{ name: subr.name }" class="dropdown-item">{{useI18n().t(subr.button)}}</router-link>
                  </li>
                </ul>
              </li>
              <li v-else>
                <router-link :to="{ name: r.name }" :class="[route.name === r.name ? activeView : inactiveView]">{{useI18n().t(r.button)}}</router-link>
              </li>
            </div>
          </ul>
          <div v-if="!loaded" class="text-end">
            <button type="button" class="btn btn-outline-light btn-empty disabled placeholder me-2" data-bs-target="#loginModalToggle" data-bs-toggle="modal"></button>
            <button type="button" class="btn btn-secondary btn-empty disabled placeholder" data-bs-target="#signupModalToggle" data-bs-toggle="modal"></button>
          </div>
          <div v-else-if="status">
            <button type="button" class="btn btn-outline-info me-2 btn-empty">
              <router-link :to="`/users/${globalUser.id}`" class="nav-link">{{ globalUser.nickname }}</router-link>
            </button>
            <button @click="LogOut" type="button" class="btn btn-secondary">{{useI18n().t('login.logout')}}</button>
          </div>
          <div v-else class="text-end">
            <button type="button" class="btn btn-outline-light me-2" data-bs-target="#loginModalToggle" data-bs-toggle="modal">{{useI18n().t('login.login')}}</button>
            <button type="button" class="btn btn-secondary" data-bs-target="#signupModalToggle" data-bs-toggle="modal">{{useI18n().t('login.signUp')}}</button>
          </div>
          <div v-if="status" class="position-relative ms-3">
            <Notifications />
          </div>
        </div>
      </div>
    </header>
    <Login
      v-model:status="status"
      v-model:signedup="signedup"
      :forcelogin="forcelogin" />
    <Signup
      v-model:signedup="signedup"
      :forcelogin="forcelogin"/>
  </section>
</template>

<script setup>
import { useI18n } from 'vue-i18n';
import Backend from "../../js/Backend"
import { ref, onMounted } from 'vue'
import router from '../../router'
import Login from '../auth/Login.vue'
import Signup from '../auth/Signup.vue'
import Notifications from '../common/Notifications.vue'
import { useRoute } from 'vue-router'
import { watch } from "vue"
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'
import { globalUser } from "../../main"

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
  { name: 'home', button: 'header.home'},
  { name: 'friends', button: 'header.friends'},
  { name: 'users', button: 'header.users'},
  { name: 'chat', button: 'header.chat'},
  { name: 'settings', button: 'header.settings'},
  { name: 'tournaments', button: 'header.tournaments'},
  { name: [
    { name: 'game/online', button: 'header.online'},
    { name: 'game/onsite', button: 'header.onsite'}
  ], button: 'header.game'}
]
const logoutRoute = { name: 'logout' }
const restrictedRoutes = ['users', 'friends', 'settings', 'game/onsite', 'game/online', 'ponggame']
const forcelogin = ref(false)
const loaded = ref(false);
const status = ref(false);

onMounted(() => {
  console.log(navRoutes);
})

watch(route, (newRoute) => {
  bootstrap.Modal.getInstance("#loginModalToggle")?.hide()
  bootstrap.Modal.getInstance("#signupModalToggle")?.hide()
  if (loaded.value && !status.value && restrictedRoutes.includes(newRoute.name))
    router.replace({ name: 'login', query: { continue: encodeURIComponent(route.fullPath) }})
  forcelogin.value = newRoute.name === 'login'
  if (forcelogin.value) {
    new bootstrap.Modal('#signupModalToggle', { keyboard: false, backdrop: 'static' })
    new bootstrap.Modal('#loginModalToggle', { keyboard: false, backdrop: 'static' }).show()
  } else {
    new bootstrap.Modal('#loginModalToggle', { keyboard: true })
    new bootstrap.Modal('#signupModalToggle', { keyboard: true })
  }
})

const AlreadyLoggedin = async() => {
  try {
    globalUser.value = await Backend.get('/api/users/me');
    status.value = true;
  } catch {
    globalUser.value = null;
    if (restrictedRoutes.includes(route.name))
      router.push({ name: 'login', query: { continue: encodeURIComponent(route.fullPath) }})
  }
  loaded.value = true;
}
AlreadyLoggedin()

const LogOut = async () => {
  try {
    await Backend.post('/api/logout', {})
    localStorage.removeItem('globalUser');
    globalUser.value = null;
    status.value = false;
    router.push(logoutRoute)
  } catch (err) {
    console.log('post(/api/logout): error: ' + err.message)
  }
}
</script>

<style scoped>
  header button {
    min-width: 5rem;
  }
</style>
