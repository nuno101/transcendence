<script setup>
import { useI18n } from 'vue-i18n';
import { ref, onMounted } from 'vue';
import SecondPlayerAuth from '../components/auth/SecondPlayerAuth.vue';
import { useRouter } from 'vue-router';
import Backend from '../js/Backend';
import InstructionInfo from '../components/game/InstructionInfo.vue';
import { globalUser } from '../main';

const shouldOpenModal = ref(false);

const gameid = ref(23);

</script>

<template>
  <h1>Onsite game</h1>
  <h1>Play on the same keyboard</h1>
    <button type="button" class="btn btn-outline-dark" @click="shouldOpenModal = true">Authenticate second player</button>
    <SecondPlayerAuth v-if="shouldOpenModal"
      :game_id="gameid"
    />
</template>

<style>
</style>
