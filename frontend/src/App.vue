<script setup>
import { RouterView } from 'vue-router';
import LanguageSelection from './components/common/LanguageSelection.vue';
import Header from './components/common/Header.vue'
import Notifications from '../src/js/Notifications'
//import './colors.css' - TODO: remove file?

</script>

<template>
  <!-- add things here that should be visible on ALL sites -->
  <LanguageSelection />
  <Header />
  <div v-if="Notifications.reloadrequired.value" class="alert alert-danger py-1 text-center" role="alert">
    Please reload the page, the page is not up-to-date
    <button class="btn" data-bs-dismiss="alert" aria-label="Close">X</button>
  </div>
  <div class="container py-4 px-3 mx-auto">
    <RouterView />
  </div>
</template>

<style scoped>
	background-color: #ffffff;
</style>
