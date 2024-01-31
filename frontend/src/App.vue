<script setup>
import { RouterView } from 'vue-router';
import LanguageSelection from './components/common/LanguageSelection.vue';
import Header from './components/common/Header.vue'
import './colors.css'

</script>

<template>
  <!-- add things here that should be visible on ALL sites -->
  <LanguageSelection />
  <Header />
  <div class="container py-4 px-3 mx-auto">
    <RouterView />
  </div>
</template>

<style scoped>
</style>
