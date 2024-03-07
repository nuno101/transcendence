<template>
    <div class="modal fade" id="playerAuthToggle" aria-hidden="true" aria-labelledby="playerAuthToggleLabel" tabindex="-1">
        <div class="modal-dialog" role="document">
            <div class="modal-content rounded-4 shadow">
            <div class="modal-header p-5 pb-4 border-bottom-0">
                <h1 class="fw-bold mb-0 fs-2"  id="playerAuthToggleLabel">Authentication</h1>
                <button @click="closeModal" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div v-for="player in authPlayers" :class="['modal-body', 'p-5', 'pt-0', { 'py-0': player.isAuthenticated }]">
                <div v-for="alert in player.alerts" :class="alert.type">
                  <div>{{ alert.message }}</div>
                  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
                <form @submit.prevent="authenticate(player)" v-if="!player.isAuthenticated">
                  <div class="form-floating mb-3">
                     <input type="text" class="form-control rounded-3" :id="'AuthUsername' + player.id" placeholder="player.username" disabled required>
                      <label :for="'AuthUsername' + player.id">{{player.username}}</label>
                  </div>
                  <div class="form-floating mb-3">
                      <input v-model="player.password" type="password" class="form-control rounded-3" :id="'AuthPassword' + player.id" placeholder="Password" required>
                      <label :for="'AuthPassword' + player.id">Password</label>
                  </div>
                  <SubmitButton :loading="loading">Authenticate</SubmitButton>
                </form>
                <div v-if="player.isAuthenticated" class="alert alert-success py-1" role="alert">
                  <i class="bi bi-person-fill-check"></i>
                  {{player.username}} successfully authenticated
                </div>
              </div>
              <div class="mx-auto mb-2 text-center pb-5" v-if="areAllPlayersAuthenticated && authPlayers.length === 2">
                <InstructionInfo :firstplayer="authPlayers[0].username" :secondplayer="authPlayers[1].username"/>
                <button type="button" class="btn btn-success" @click="startGame">Start Game</button>
              </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed, defineProps } from 'vue';
import Backend from '../../js/Backend'
import SubmitButton from '../common/SubmitButton.vue';
import InstructionInfo from '../game/InstructionInfo.vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle';
import router from '../../router';
import { globalUser } from '../../main';


const props = defineProps(['game_id', 'player1', 'player2']);

const authPlayers = ref([]);
const loading = ref(false)

onMounted(() => {
  authPlayers.value.push({ id: 1, username: props.player1, isAuthenticated: props.player1 === globalUser.value.username, alerts: [] });
  authPlayers.value.push({ id: 2, username: props.player2, isAuthenticated: props.player2 === globalUser.value.username, alerts: [] });
})

const openModal = () => {
  if(!bootstrap.Modal.getInstance("#playerAuthToggle"))
    new bootstrap.Modal('#playerAuthToggle', { keyboard: true })
	bootstrap.Modal.getInstance("#playerAuthToggle").show();
};

const closeModal = () => {
	bootstrap.Modal.getInstance("#playerAuthToggle").hide();
};

const startGame = () => {
  closeModal();
  router.push('/ponggame');
  // props.game.value.id
  // add gameid here
};

const authenticate = async (player) => {
  try {
    player.alerts = []
    await Backend.post('/api/authenticate', { username: `${player.username}`, password: `${player.password}`});
    player.isAuthenticated = true;
  } catch (err) {
    console.log(err);
    player.alerts.push({
      message: err.message,
      type: { 'alert': true, 'alert-danger': true, 'alert-dismissible': true }
    })
    player.password = '';
  }
}

const areAllPlayersAuthenticated = computed(() => {
  return authPlayers.value.every(player => player.isAuthenticated);
});

defineExpose({
  openModal,
});
</script>
