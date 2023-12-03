<script setup>
  import { RouterLink, RouterView } from 'vue-router';
  import LanguageSelection from './components/common/LanguageSelection.vue';
</script>

<template>
  <!-- add things here that should be visible on ALL sites -->
  <div class="container py-4 px-3 mx-auto">
    <LanguageSelection />
    <RouterView />
  </div>
</template>

<style scoped>
</style>
