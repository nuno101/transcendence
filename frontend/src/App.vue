<script setup>
import { RouterLink, RouterView } from 'vue-router';
import LanguageSelection from './components/LanguageSelection.vue';
</script>

<template>
<!-- add things here that should be visible on ALL sites -->
    <LanguageSelection />
  <RouterView />
</template>

<style scoped>
</style>