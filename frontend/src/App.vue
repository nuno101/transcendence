<script setup>
import LanguageSelection from './components/common/LanguageSelection.vue'
</script>

<!-- add things here that should be visible on ALL sites -->
<template>
	<div class="background-image">
    <LanguageSelection />
    <RouterView name="Header" />
      <div class="container py-4 px-3 mx-auto">
        <RouterView />
      </div>
	</div>
</template>

<style scoped>
.background-image {
  /* Adjust the URL to the path of your background image */
  background-image: url('./assets/backgroundWithoutFont.png');
  /* Set background size and other properties as needed */
  background-size: cover;
  background-position: center;
  width: 100vw;
  height: 100vh;
  position: relative;
  overflow: hidden;
  font-family: 'Courier New', monospace;
  /* color: white; */
}
</style>