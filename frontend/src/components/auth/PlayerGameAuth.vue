<template>
    <div class="modal fade" id="playerAuthToggle" aria-hidden="true" aria-labelledby="playerAuthToggleLabel" tabindex="-1">
        <div class="modal-dialog" role="document">
            <div class="modal-content rounded-4 shadow">
            <div class="modal-header p-5 pb-4 border-bottom-0">
                <h1 class="fw-bold mb-0 fs-2"  id="playerAuthToggleLabel">Authentication</h1>
                <button @click="closeModal" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div v-for="(player, index) in authPlayers" :key="index" :class="['modal-body', 'p-5', 'pt-0', { 'py-0': player.isAuthenticated }]">
                <div v-for="alert in player.alerts" :class="alert.type">
                  <div>{{ alert.message }}</div>
                  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
                <form @submit.prevent="authenticate(player)" v-if="!player.isAuthenticated">
                  <div class="form-floating mb-3">
                     <input v-if="player.isGiven" type="text" class="form-control rounded-3" :id="'AuthUsername' + index" placeholder="player.username" disabled required>
                     <input v-else v-model="player.username" type="text" class="form-control rounded-3" :id="'AuthUsername' + index" placeholder="Enter Username" required>
                      <label :for="'AuthUsername' + index">{{player.isGiven ? player.username : "Enter username"}}</label>
					  <p>PLAYER USERNAME: {{ player.username }}</p>
                  </div>
                  <div class="form-floating mb-3">
                      <input v-model="player.password" type="password" class="form-control rounded-3" :id="'AuthPassword' + index" placeholder="Password" required>
                      <label :for="'AuthPassword' + index">Password</label>
                  </div>
                  <SubmitButton :loading="loading">Authenticate</SubmitButton>
                </form>
                <div v-if="player.isAuthenticated" class="alert alert-success py-1" role="alert">
                  <i class="bi bi-person-fill-check"></i>
                  {{player.username}} with nickname <strong>{{player.nickname}}</strong> successfully authenticated
                </div>
              </div>
              <div class="mx-auto mb-2 text-center pb-5" v-if="areAllPlayersAuthenticated && authPlayers.length === 2">
                <InstructionInfo :firstplayer="authPlayers[0].nickname" :secondplayer="authPlayers[1].nickname"/>
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

const props = defineProps({
  game_id: {
    default: null
  },
  player1: {
    default: null
  },
  player2: {
    default: null
  }
});

const authPlayers = ref([]);
const loading = ref(false)

onMounted(() => {
  console.log("yo:", props);
  console.log("props player1 : ", props.player1);
  console.log("props player2 : ", props.player2);
  authPlayers.value.push({ username: props.player1,  isGiven: props.player1 !== null, isAuthenticated: props.player1 === globalUser.value.username, alerts: [] });
  authPlayers.value.push({ username: props.player2, isGiven: props.player2 !== null, isAuthenticated: props.player2 === globalUser.value.username, alerts: [] });
  console.log("authPlayers : ", authPlayers.value);
})

const openModal = () => {
  if(!bootstrap.Modal.getInstance("#playerAuthToggle"))
    new bootstrap.Modal('#playerAuthToggle', { keyboard: true })
	bootstrap.Modal.getInstance("#playerAuthToggle").show();
	console.log("open modal props player1 : ", props.player1);
    console.log("open modal props player2 : ", props.player2);
};

const closeModal = () => {
	bootstrap.Modal.getInstance("#playerAuthToggle").hide();
};

// CREATE GAME IF NO GAME_ID EXISTS (SINGLE GAME)
const startGame = async() => {
  let gameId;
  if(!props.game_id)
    gameId = await createSingleGame(authPlayers.value[0].userId, authPlayers.value[1].userId);
  else
    gameId = props.game_id;
  closeModal();
  router.push({ name: 'ponggame', params: { id: `${gameId}`} });
};

const createSingleGame = async(playerId1, playerId2) => {
  const response = ref(null);
  try{
    response.value = await Backend.post('/api/games', {  player1_id: `${playerId1}`, player2_id: `${playerId2}` });
  } catch (err) {
    console.log(err);
    alert(err);
  }
  return(response.value.id);
}

const authenticate = async (player) => {
  try {
    player.alerts = []

    // CHECK DUPLICATED PLAYERS FOR SINGLE GAMES
    const duplicatePlayer = authPlayers.value.find(p => p !== player && p.username === player.username);
    if(duplicatePlayer) {
      player.alerts.push({
        message: "Username " + `${player.username} already taken`,
        type: { 'alert': true, 'alert-danger': true, 'alert-dismissible': true }
      });
    } else {
      const response = await Backend.post('/api/authenticate', { username: `${player.username}`, password: `${player.password}`});
      player.userId = response.id;
      player.nickname = response.nickname;
      player.isAuthenticated = true;
    } 
  } catch (err) {
    console.log(err);
    player.alerts.push({
      message: err.message,
      type: { 'alert': true, 'alert-danger': true, 'alert-dismissible': true }
    })
    player.password = '';
    if(!player.isGiven)
      player.username = '';
  }
}

const areAllPlayersAuthenticated = computed(() => {
  return authPlayers.value.every(player => player.isAuthenticated);
});

defineExpose({
  openModal,
});
</script>
