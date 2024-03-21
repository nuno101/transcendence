<script setup>
import LanguageSelection from './components/common/LanguageSelection.vue'
import Notifications from '../src/js/Notifications'
import { useRouter } from 'vue-router';
import { ref } from 'vue';

//import './colors.css' - TODO: remove file?

// const bg = ref(null);
const router = useRouter();

// Navigation guard to handle background image change based on route
router.beforeEach((to, from, next) => {
  if (to.path === '/') {
    // Change the background image for the root route
    bg.value = './assets/background_root.png';
  } else {
    // Use the default background image for other routes
    bg.value = './assets/background.png';
  }
  next();
});

</script>

<!-- add things here that should be visible on ALL sites -->
<template>
	<div class="background-image">
	<LanguageSelection />
	<RouterView name="Header" />
	<div class="container py-4 px-3 mx-auto">
		<div v-if="Notifications.reloadrequired.value" class="alert alert-danger alert-dismissible" role="alert">
			<div class="text-center">Please reload the page, the page is not up-to-date</div>
			<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
		</div>
		<RouterView />
	</div>
	</div>
</template>

<style scoped>
.background-image {
  /* Adjust the URL to the path of your background image */
  background-image: url('./assets/background.png');
  /* Set background size and other properties as needed */
  background-size: cover;
  background-position: center;
  width: 100vw;
  height: 100vh;
  position: relative;
  overflow: hidden;
}
</style>