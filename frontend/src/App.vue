<script setup>
import LanguageSelection from './components/common/LanguageSelection.vue'
//import './colors.css' - TODO: remove file?
</script>

<!-- add things here that should be visible on ALL sites -->
<template>
	<LanguageSelection />
	<RouterView name="Header" />
	<div class="container py-4 px-3 mx-auto">
		<RouterView />
	</div>
</template>
