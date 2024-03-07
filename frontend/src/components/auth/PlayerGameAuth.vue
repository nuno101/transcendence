<template>
    <div class="modal fade" id="playerAuthToggle" aria-hidden="true" aria-labelledby="playerAuthToggleLabel" tabindex="-1">
        <div class="modal-dialog" role="document">
            <div class="modal-content rounded-4 shadow">
            <div class="modal-header p-5 pb-4 border-bottom-0">
                <h1 class="fw-bold mb-0 fs-2"  id="playerAuthToggleLabel">Authentication</h1>
                <button @click="closeModal" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div v-for="player in authPlayers" :class="['modal-body', 'p-5', 'pt-0', { 'py-0': player.isAuthenticated }]">
                <div v-for="alert in alerts" :class="alert.type">
                  <div>{{ alert.message }}</div>
                  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" @click="closeModal"></button>
                </div>
                <form @submit.prevent="authenticate(player)" v-if="!player.isAuthenticated">
                  <div class="form-floating mb-3">
                     <input type="text" class="form-control rounded-3" :id="'AuthUsername' + player.id" placeholder="" disabled>
                      <label :for="'AuthUsername' + player.id">{{player.username}}</label>
                  </div>
                  <div class="form-floating mb-3">
                      <input v-model="player.password" type="password" class="form-control rounded-3" :id="'AuthPassword' + player.id" placeholder="Password">
                      <label :for="'AuthPassword' + player.id">Password</label>
                  </div>
                  <SubmitButton :loading="loading">Authenticate</SubmitButton>
                </form>
                <div v-if="player.isAuthenticated" class="alert alert-success py-1" role="alert">
                  <i class="bi bi-person-fill-check"></i>
                  {{player.username}} successfully authenticated
                </div>
              </div>
              <div class="mx-auto mb-2 text-center" v-if="areAllPlayersAuthenticated && authPlayers.length === 2">
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


const props = defineProps(['game_id']);

const authPlayers = ref([]);
const alerts = ref([])
const loading = ref(false)

const game = ref({});

onMounted(() => {
  fetchData();
})

const fetchData = async () => {
  try {
      game.value = await Backend.get(`/api/games/${props.game_id}`);
      authPlayers.value.push({ ...game.value.player1, isAuthenticated: game.value.player1.username === globalUser.value.username });
      authPlayers.value.push({ ...game.value.player2, isAuthenticated: game.value.player2.username === globalUser.value.username });
  } catch (err) {
    console.error('Error fetching upcoming games:', err);
  }
};

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
    alerts.value = []
    console.log(player.username);
    console.log(player.password);
    // USERNAME: player.username
    // PASSWORD: player.password
    // const response = await Backend.post('/api/login', { username: `${player.username}`, password: `${player.password}`});
    player.isAuthenticated = true;
  } catch (err) {
    console.log(err);
    alerts.value.push({
      message: err.message,
      type: { 'alert': true, 'alert-danger': true, 'alert-dismissible': true }
    })
  }
}

const areAllPlayersAuthenticated = computed(() => {
  return authPlayers.value.every(player => player.isAuthenticated);
});

defineExpose({
  openModal,
});
</script>
