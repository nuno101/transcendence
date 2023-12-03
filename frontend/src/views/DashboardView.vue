<script setup>
// import { useI18n } from 'vue-i18n';
import HomeSelection from '../components/dashboard/DashboardChoice.vue';
</script>

<template>
  <div class="row home">
      <home-selection />
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .home {
    min-height: 20vh;
    display: flex;
    align-items: center;
  }
}
</style>
