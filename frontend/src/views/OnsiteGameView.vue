<script setup>
import { useI18n } from 'vue-i18n';
import { ref, onMounted } from 'vue';
import PlayerGameAuth from '../components/auth/PlayerGameAuth.vue';
import { globalUser } from '../main';

const auth = ref(null);

onMounted(() => {
	if(auth.value)
		auth.value.openModal();
})
</script>

<template>
	<div class="text-center" style="margin-top: 20vh">
		<button type="button"
			class="btn btn-outline-light"
			@click="auth.openModal()">{{useI18n().t('onsite.authenticateSecondPlayer')}}
		</button>
	</div>
	<PlayerGameAuth
		ref="auth"
		:player1="globalUser"
	/>
</template>

<style>
</style>
