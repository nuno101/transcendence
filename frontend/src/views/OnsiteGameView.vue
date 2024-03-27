<script setup>
import { useI18n } from 'vue-i18n';
import { ref } from 'vue';
import PlayerGameAuth from '../components/auth/PlayerGameAuth.vue';
import { globalUser } from '../main';

const auth = ref(null);

</script>

<template>
    <button type="button" class="btn btn-outline-dark" @click="auth.openModal()">{{useI18n().t('onsite.authenticateSecondPlayer')}}</button>
    <PlayerGameAuth
      ref="auth"
      :player1="globalUser"
    />
</template>

<style>
</style>
