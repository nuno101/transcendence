<script setup>
import { useI18n } from 'vue-i18n';
import UpcomingGames from '../components/game/UpcomingGames.vue';
import { globalUser } from '../main'

const profileLinks = [
	{ link: 'https://github.com/Anoukmch', name: 'amechain' },
	{ link: 'https://github.com/jharrach', name: 'jharrach' },
	{ link: 'https://github.com/jmatheis00', name: 'jmatheis' },
	{ link: 'https://github.com/nuno101', name: 'nlouro' },
	{ link: 'https://github.com/PythonGermany', name: 'rburgsta' }
]
</script>

<template>
	<UpcomingGames/>
	<h1 v-if="!globalUser" style="margin-top: 24vh; z-index: 0" class="text-white text-center align-middle">FT_TRANSCENDENCE</h1>
	<footer class="container-fluid p-3 text-center text-white" style="z-index: 1; background-color: rgba(0, 0, 0, 0.5);">
		<h6 class="text-uppercase fw-bold pb-1">{{useI18n().t('home.connectOnGithub')}}</h6>
		<div class="d-flex flex-wrap justify-content-center">
			<p class="mx-md-4 mx-2" v-for="(link, index) in profileLinks" :key="index">
				<i class="bi bi-github"></i> <a class="link-opacity-50-hover text-white" :href="link.link">{{ link.name }}</a>
			</p>
		</div>
		<div>
			<i class="bi bi-github"></i> <a class="link-opacity-50-hover text-white" href="https://github.com/nuno101/transcendence">{{useI18n().t('home.ourTranscendenceProject')}}</a>
		</div>
	</footer>
</template>

<style>

footer {
	position: absolute; bottom: 0; width: 100%;
}
</style>