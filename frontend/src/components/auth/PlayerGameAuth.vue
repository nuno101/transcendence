<template>
	<div ref="authModal" class="modal fade" id="playerAuthToggle" aria-hidden="true" aria-labelledby="playerAuthToggleLabel" tabindex="-1">
		<div class="modal-dialog" role="document">
			<div class="modal-content rounded-4 shadow">
				<div class="modal-header p-5 pb-4 border-bottom-0">
					<h1 class="fw-bold mb-0 fs-2"  id="playerAuthToggleLabel">{{useI18n().t('auth.authentication')}}</h1>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div v-for="(player, index) in authPlayers" :key="index" :class="['modal-body', 'p-5', 'pt-0', { 'py-0': player.isAuthenticated }]">
					<div v-for="alert in player.alerts" :class="alert.type">
						<div>{{ useI18n().te(`err.${alert.message}`) ? useI18n().t(`err.${alert.message}`) :  alert.message}}</div>
						<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
					</div>
					<form @submit.prevent="authenticate(player)" v-if="!player.isAuthenticated">
						<div class="form-floating mb-3">
							<input v-if="player.isGiven" type="text" class="form-control rounded-3" :id="'AuthUsername' + index" placeholder="player.username" disabled required>
							<input v-else v-model="player.user.username" type="text" class="form-control rounded-3" :id="'AuthUsername' + index" :placeholder="useI18n().t('username')" required>
							<label :for="'AuthUsername' + index">{{player.isGiven ? player.user.username : useI18n().t('username')}}</label>
						</div>
						<div class="form-floating mb-3">
							<input v-model="player.password" type="password" class="form-control rounded-3" :id="'AuthPassword' + index" :placeholder="useI18n().t('password')" required>
							<label :for="'AuthPassword' + index">{{useI18n().t('password')}}</label>
						</div>
						<SubmitButton :loading="loading">{{useI18n().t('auth.authenticate')}}</SubmitButton>
					</form>
					<div v-if="player.isAuthenticated" class="alert alert-success py-1" role="alert">
						<i class="bi bi-person-fill-check"></i>
						{{player.user.username}} {{useI18n().t('auth.withNickname')}} <strong>{{player.user.nickname}}</strong> {{useI18n().t('auth.successfullyAuth')}}
					</div>
				</div>
				<div class="mx-auto mb-2 text-center px-5 pb-5" v-if="areAllPlayersAuthenticated && authPlayers.length === 2">
					<InstructionInfo :firstplayer="authPlayers[0].user.nickname" :secondplayer="authPlayers[1].user.nickname"/>
					<button type="button" class="btn btn-success" @click="startGame">{{useI18n().t('auth.startGame')}}</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { useI18n } from 'vue-i18n';
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
	player1: {},
	player2: {
		default: null
	}
});

const i18n = useI18n();
const authPlayers = ref([]);
const loading = ref(false)
const authModal = ref(null);

onMounted(() => {
	authModal.value.addEventListener('hidden.bs.modal', () => {
		authPlayers.value = [];
	})
})

const openModal = () => {
	if(!bootstrap.Modal.getInstance("#playerAuthToggle"))
		new bootstrap.Modal('#playerAuthToggle', { keyboard: true })
	bootstrap.Modal.getInstance("#playerAuthToggle").show();
	authPlayers.value.push({ 
		user: props.player1 ? props.player1 : { username: '' }, 
		isGiven: props.player1 !== null, 
		isAuthenticated: props.player1 ? props.player1.username === globalUser.value.username : false, 
		alerts: [] 
	});
	authPlayers.value.push({ 
		user: props.player2 ? props.player2 : { username: '' }, 
		isGiven: props.player2 !== null, 
		isAuthenticated: props.player2 !== null ? props.player2.username === globalUser.value.username : false, 
		alerts: [] 
	});
};

const closeModal = () => {
	bootstrap.Modal.getInstance("#playerAuthToggle").hide();
};

// CREATE GAME IF NO GAME_ID EXISTS (SINGLE GAME)
const startGame = async() => {
	let gameId;
	if(!props.game_id)
		gameId = await createSingleGame(authPlayers.value[0].user.id, authPlayers.value[1].user.id);
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
		console.error(err.message);
		alert(i18n.te(err.message) ? i18n.t(err.message) : err.message);
	}
	return(response.value.id);
}

const authenticate = async (player) => {
	try {
		player.alerts = []

		// CHECK DUPLICATED PLAYERS FOR SINGLE GAMES
		const duplicatePlayer = authPlayers.value.find(p => p !== player && p.user.username === player.user.username);
		if(duplicatePlayer) {
			player.alerts.push({
				message: `${i18n.t('username')} ${player.user.username} ${i18n.t('onsite.alreadyTaken')}`,
				type: { 'alert': true, 'alert-danger': true, 'alert-dismissible': true }
			});
		} else {
			const response = await Backend.post('/api/authenticate', { username: `${player.user.username}`, password: `${player.password}`});
			player.user.id = response.id;
			player.user.nickname = response.nickname;
			player.isAuthenticated = true;
		} 
	} catch (err) {
		console.error(err.message);
		player.alerts.push({
			message: err.message,
			type: { 'alert': true, 'alert-danger': true, 'alert-dismissible': true }
		})
		player.password = '';
		if(!player.isGiven)
			player.user.username = '';
  	}
}

const areAllPlayersAuthenticated = computed(() => {
  	return authPlayers.value.every(player => player.isAuthenticated);
});

defineExpose({
  	openModal,
});
</script>