<script setup>
import { useI18n } from 'vue-i18n';
import { ref } from 'vue';
import PlayerGameAuth from '../components/auth/PlayerGameAuth.vue';
import { globalUser } from '../main';

const auth = ref(null);

</script>

<template>
  <h1>Onsite game</h1>
  <h1>Play on the same keyboard</h1>
    <button type="button" class="btn btn-outline-dark" @click="auth.openModal()">Authenticate second player</button>
    <PlayerGameAuth
      ref="auth"
      :player1="globalUser"
    />
</template>

<style>
</style>
