<script setup>
import { useI18n } from 'vue-i18n';
import { ref, onMounted } from 'vue';
import SecondPlayerAuth from '../components/auth/SecondPlayerAuth.vue';
import { useRouter } from 'vue-router';
import Backend from '../js/Backend';
import InstructionInfo from '../components/game/InstructionInfo.vue';
import { globalUser } from '../main';

const router = useRouter();
const input = ref({ nickname: '', id: ''});
const isAuthenticated = ref(false);
const shouldOpenModal = ref(false);

const startGame = () => {
  router.push('/ponggame');
};
</script>

<template>
  <h1>Onsite game</h1>
  <h1>Play on the same keyboard</h1>
    <button v-if="!isAuthenticated" type="button" class="btn btn-outline-dark" @click="shouldOpenModal = true">Authenticate second player</button>
    <SecondPlayerAuth
      v-if="shouldOpenModal"
      v-model:input="input"
      v-model:isAuthenticated="isAuthenticated"
      v-model:shouldOpenModal="shouldOpenModal"
    />
    <div v-if="isAuthenticated">
      <div class="alert alert-success py-1" role="alert">
        <i class="bi bi-person-fill-check"></i>
        Second player successfully authenticated
      </div>
      <InstructionInfo :firstplayer="input.nickname" :secondplayer="globalUser?.nickname"/>
      <button type="button" class="btn btn-outline-success" @click="startGame">Start Game</button>
    </div>
</template>

<style>
</style>
