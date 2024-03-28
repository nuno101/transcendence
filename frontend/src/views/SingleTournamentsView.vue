<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { computed, ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle';
import ModalSettings from '../components/tournaments/ModalSettings.vue';
import GameSelection from '../components/tournaments/GameSelection.vue';
import WinnerRanking from '../components/tournaments/WinnerRanking.vue';

const tournament = ref(null);
const tournamentId = ref(null);
const title = ref(null); // try to use tournament.X instead of creating a ref for all
const description = ref(null);
const status = ref(null);
const created_at = ref(null);
const updated_at = ref(null);
const username = ref(null);
const creator = ref(null);
const players = ref([]);
const isCreator = ref(false);
const isJoined = ref(false);
const currentUser = ref(false);
const editingDescription = ref(false);
const games = ref(null);
const updatedGames = ref(null);
const alerts = ref({ title: '', message: '' })

const route = useRoute();
const router = useRouter();

watch(route, (newRoute) => {
  bootstrap.Modal.getInstance("#successModal")?.hide()
})

const fetchData = async () => {
  try {
    tournament.value = await Backend.get(`/api/tournaments/${tournamentId.value}`);
	currentUser.value = await Backend.get('/api/users/me');
	games.value = await Backend.get(`/api/tournaments/${tournamentId.value}/games`);
    username.value = currentUser.value.username;
	const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
	isJoined.value = localStorage.getItem(userTournamentKey) === 'true';
	initValues(tournament.value);
	return tournament.value;
  } catch (err) {
    console.error(err.message);
  }
};

const initValues = (data) => {
	title.value = data.title
	description.value = data.description
	status.value = data.status
	created_at.value = data.created_at
	updated_at.value = data.updated_at
	creator.value = data.creator.nickname
	players.value = data.players;
	if (data.creator.username === username.value) {
    	isCreator.value = true;
	}
};

watch(games, (newGames, oldGames) => {
  updatedGames.value = newGames;
});

const handleUpdateTesT = (newValue) => {
    games.value = newValue;
}

const joinTournament = async (msg) => {
	try {
		const join = await Backend.post(`/api/tournaments/${tournamentId.value}/play`, { "play": "join" });
		players.value = join.players;
		const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
		isJoined.value = true;
		localStorage.setItem(userTournamentKey, JSON.stringify(true));
		await Backend.patch(`/api/users/me`, { "tournament_id": `${tournamentId.value}` });
		setModal("Success", msg);
	} catch (error) {
		console.error(error.message);
		setModal("Error", error.message);
	}
};

const unjoinTournament = async (msg) => {
	try {
		const unjoin = await Backend.post(`/api/tournaments/${tournamentId.value}/play`, { "play": "unjoin" });
		players.value = unjoin.players;
		const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
		isJoined.value = false;
		localStorage.setItem(userTournamentKey, JSON.stringify(false));
		await Backend.patch(`/api/users/me`, { "tournament_id": `${tournamentId.value}` });
		setModal("Success", msg);
	} catch (error) {
        console.error(error.message);
		setModal("Error", error.message);
    }	
};

const changeState = async (msg) => {
	try {
		const response = await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "status": "next"});
		status.value = response.status;
		setModal("Success", msg);
	} catch (error) {
        console.error(error.message);
		setModal("Error", error.message);
    }
};

const cancelTournament = async (msg) => {
  try {
    const response = await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "status": "cancel"});
	status.value = response.status;
	setModal("Success", msg);
  } catch (err) {
    console.error(err.message);
	setModal("Error", err.message);
  }
};

const deleteTournament = async (msg) => {
  try {
    await Backend.delete(`/api/tournaments/${tournamentId.value}`);
	setModal("Success", msg);
	router.go(-1);
  } catch (err) {
    console.error(err.message);
  }
};

const startTournament = async (msg) => {
  try {
    games.value = await Backend.get(`/api/tournaments/${tournamentId.value}/games`);
	changeState(msg);
	console.log("games.value: ", games.value);
  } catch (err) {
    console.error(err.message);
  }
};

const startEditing = () => {
    editingDescription.value = true;
};

/*const updateDescription = async () => {
    try {
        await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "description": description.value });
		editingDescription.value = false;
    } catch (error) {
        console.error('Error updating description:', error.message);
    }
};*/

const { t } = useI18n();

const translatedStrings = computed(() => ({
    registrationIsNowOpen: t('singletournamentsview.registrationisnowopen'),
	tournamentIsNowDeleted: t('singletournamentsview.tournamentisnowdeleted'),
	registrationIsNowClosed: t('singletournamentsview.registrationisnowclosed'),
	theTournamentHasBeenCancelled: t('singletournamentsview.thetournamenthasbeencancelled'),
	successfullUnjoinTournament: t('singletournamentsview.successfullunjointournament'),
	successfullJoinTournament: t('singletournamentsview.successfulljointournament'),
	unjoinTheTournament: t('singletournamentsview.unjointhetournament'),
	joinTheTournament: t('singletournamentsview.jointhetournament'),
	tournamentWillStartGetReady: t('singletournamentsview.tournamentwillstartgetready')
    
}));

const setModal = async (title, msg) => {
    alerts.value = {
        title: title,
        message: msg,
    };
};

onMounted(() => {
	const route = useRoute();
  	tournamentId.value = route.params.id;
	fetchData();
})
</script>

<template>
<div class="container mt-5">
        <h1 class="display-4 mb-4">{{ title }}</h1>
        <div class="row">
            <div class="col-lg-8">
                <p class="lead mb-4">{{useI18n().t('tournamentsview.status')}}: <span class="text-muted" v-if="status">{{ useI18n().t(`singletournamentsview.${status}`)}}</span></p>
				<div class="mb-3">
					<label for="description" class="form-label">{{useI18n().t('tournamentsview.description')}}:</label>
					<div class="description-container">
						<span v-if="!editingDescription && isCreator && (status === 'created' || status === 'registration_open')" @click="startEditing">{{ description }}</span>
						<textarea class="form-control" id="description" v-model="description" v-if="editingDescription && isCreator && (status === 'created' || status === 'registration_open')" rows="5"></textarea>
						<button v-if="editingDescription && isCreator && (status === 'created' || status === 'registration_open')" class="btn btn-primary mt-3" @click="updateDescription">Update</button>
						<span v-if="!isCreator">{{ description }}</span>
					</div>
				</div>

                <div class="row mt-5">
                    <div class="col-md-6">
                        <p class="text-muted">{{useI18n().t('tournamentsview.created_at')}}: {{ created_at ? created_at.slice(0, 10) : 'N/A' }}</p>
                    </div>
                    <div class="col-md-6">
						<p class="text-muted">{{useI18n().t('tournamentsview.last_update')}}: {{ updated_at ? updated_at.slice(0, 10) : 'N/A' }}</p>
                    </div>
                </div>

				<div v-if="status === 'created'">
					<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#successModal" v-if="isCreator" @click="changeState(translatedStrings.registrationIsNowOpen)" >{{ t('singletournamentsview.openregistration') }}</button>
					<span v-if="isCreator">&nbsp;&nbsp;</span>
					<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#successModal" v-if="isCreator" @click="deleteTournament(translatedStrings.tournamentIsNowDeleted)">{{useI18n().t('singletournamentsview.deletetournament')}}</button>

					<div class="alert alert-danger" v-else>{{useI18n().t('singletournamentsview.registrationforthistournamentisnotyetopen')}} <b>{{ creator }}</b> {{useI18n().t('singletournamentsview.formoreinfo')}}</div>
				</div>

				<div v-if="status === 'registration_open'">
					<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#successModal" v-if="isCreator" @click="changeState(translatedStrings.registrationIsNowClosed)" >{{useI18n().t('singletournamentsview.closeregistration')}}</button>
					<span v-if="isCreator">&nbsp;&nbsp;</span>
					<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#successModal" v-if="isCreator" @click="cancelTournament(translatedStrings.theTournamentHasBeenCancelled)">{{useI18n().t('singletournamentsview.canceltournament')}}</button>
        			<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#successModal" v-else @click="isJoined ? unjoinTournament(translatedStrings.successfullUnjoinTournament) : joinTournament(translatedStrings.successfullJoinTournament)">{{ isJoined ? useI18n().t('singletournamentsview.unjointhetournament') : useI18n().t('singletournamentsview.jointhetournament') }}</button>		
				</div>

				<div v-if="status === 'registration_closed'">
					<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#successModal" v-if="isCreator" @click="startTournament(translatedStrings.tournamentWillStartGetReady)">{{useI18n().t('singletournamentsview.starttournament')}}</button>
					<span v-if="isCreator">&nbsp;&nbsp;</span>
					<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#successModal" v-if="isCreator" @click="cancelTournament(translatedStrings.theTournamentHasBeenCancelled)">{{useI18n().t('singletournamentsview.canceltournament')}}</button>
					<div class="alert alert-success" v-else>{{useI18n().t('singletournamentsview.tournamentwillstartgetready')}}</div>
				</div>

				<div v-if="status === 'ongoing'">
					<div class="tcontainer">
						<div class="tournament-bracket__round">
							<GameSelection title="Select a game" :is_Creator="isCreator" :tournament_Id="tournamentId" :games.sync="games" @update:games="handleUpdateTesT"></GameSelection>								
						</div>
					</div>
				</div>
            </div>

			<div v-if="status === 'done'">
				<div class="tcontainer">
					<div class="tournament-bracket__round">
						<WinnerRanking :games="games"></WinnerRanking>
					</div>
				</div>
            </div>

			<ModalSettings
			  :title_child="alerts.title"
			  :message_child="alerts.message"
			/>

            <div class="col-lg-4">
                <h3 class="mb-3">{{useI18n().t('tournamentsview.creator')}}</h3>
				<b><p>{{ creator }}
				<span v-if="isCreator">{{useI18n().t('tournamentsview.(you)')}}</span></p></b>
                <h3 class="mb-3 mt-4">{{useI18n().t('tournamentsview.players')}}</h3>
                <table class="table">
                    <thead>
                        <tr><th>{{useI18n().t('singletournamentsview.tournamentnickname')}}</th></tr>
                    </thead>
                    <tbody>
                        <tr v-for="(player, index) in players" :key="index">
							<td>
								<b v-if="player.username === username">{{ player.nickname }} {{useI18n().t('tournamentsview.(you)')}}</b>
        						<template v-else>{{ player.nickname }}</template>
							</td>
                        </tr>
                    </tbody>
                </table>
				<GameSelection v-if="status === 'ongoing'" title="Completed games" :is_Creator="isCreator" :tournament_Id="tournamentId" :games="games" @update:games="handleUpdateTesT"/>
            </div>
        </div>
    </div>
</template> 


<style>

/*!
 * Responsive Tournament Bracket
 * Copyright 2016 Jakub Hájek
 * Licensed under MIT (https://opensource.org/licenses/MIT)
 */

.tcontainer {
  width: 90%;
  min-width: 18em;
  padding-top:2em;
  margin: 4px;
}

.tournament-bracket__round {
  display: block;
  margin-left: -3px;
  flex: 1;
}

</style>
