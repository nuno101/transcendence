<script setup>
import HomeSelection from '../components/HomeSelection.vue';
</script>

<template>
  <div class="home">
    <home-selection />
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .home {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
