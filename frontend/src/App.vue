<script setup>
import LanguageSelection from './components/common/LanguageSelection.vue'
import Notifications from '../src/js/Notifications'
//import './colors.css' - TODO: remove file?
</script>

<!-- add things here that should be visible on ALL sites -->
<template>
	<LanguageSelection />
	<RouterView name="Header" />
	<div class="container py-4 px-3 mx-auto">
		<div v-if="Notifications.reloadrequired.value" class="alert alert-danger alert-dismissible" role="alert">
			<div class="text-center">Please reload the page, the page is not up-to-date</div>
			<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
		</div>
		<RouterView />
	</div>
</template>
