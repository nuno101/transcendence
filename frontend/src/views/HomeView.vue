<script setup>
import { useI18n } from 'vue-i18n';
import UpcomingGames from '../components/game/UpcomingGames.vue';
import FooterComp from '../components/common/Footer.vue';
import { globalUser } from '../main'

</script>

<template>
	<h1 v-if="!globalUser" style="margin-top: 24vh; z-index: 0" class="text-white text-center align-middle">FT_TRANSCENDENCE</h1>
	<UpcomingGames/>
	<FooterComp  class="footer"/>
</template>

<style>
</style>