<script setup>
import { useI18n } from 'vue-i18n';
import { ref } from 'vue';
import PlayerGameAuth from '../components/auth/PlayerGameAuth.vue';

const gameid = ref(35);
const p1 = ref("test11");
const p2 = ref("test3");
const auth = ref(null);

</script>

<template>
  <h1>Onsite game</h1>
  <h1>Play on the same keyboard</h1>
    <button type="button" class="btn btn-outline-dark" @click="auth.openModal()">Authenticate second player</button>
    <PlayerGameAuth
      ref="auth"
    />
      <!-- :game_id="gameid"
      :player1="p1"
      :player2="p2" -->
</template>

<style>
</style>
