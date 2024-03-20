<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { computed, ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle';
import ModalSettings from '../components/tournaments/ModalSettings.vue';
import GameSelection from '../components/tournaments/GameSelection.vue';

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
const message = ref(null);
const editingDescription = ref(false);
const games = ref(null);
const updatedGames = ref(null);

const route = useRoute();
const router = useRouter();

watch(route, (newRoute) => {
  bootstrap.Modal.getInstance("#successModal")?.hide()
})

watch(games, (newGames, oldGames) => {
  updatedGames.value = newGames;
});

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

const handleUpdateTesT = (newValue) => {
    games.value = newValue;
}

const initValues = (data) => {
	title.value = data.title
	description.value = data.description
	status.value = data.status
	created_at.value = data.created_at
	updated_at.value = data.updated_at
	creator.value = data.creator.username
	players.value = data.players;
	if (creator.value === username.value) {
    	isCreator.value = true;
	}
};

const joinTournament = async (msg) => {
    const join = await Backend.post(`/api/tournaments/${tournamentId.value}/play`, { "play": "join" });
	players.value = join.players;
	const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
	isJoined.value = true;
	localStorage.setItem(userTournamentKey, JSON.stringify(true));
	await Backend.patch(`/api/users/me`, { "tournament_id": `${tournamentId.value}` });
	message.value = msg;
};

const unjoinTournament = async (msg) => {
    const unjoin = await Backend.post(`/api/tournaments/${tournamentId.value}/play`, { "play": "unjoin" });
	players.value = unjoin.players;
	const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
	isJoined.value = false;
	localStorage.setItem(userTournamentKey, JSON.stringify(false));
	await Backend.patch(`/api/users/me`, { "tournament_id": `${tournamentId.value}` });
	message.value = msg;
};

const changeState = async (msg) => {
	try {
		const response = await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "status": "next"});
		status.value = response.status;
		message.value = msg;
	} catch (error) {
        console.error(error.message);
		message.value = error.message; // Should be translatable 
		const modal = bootstrap.Modal.getInstance("#successModal"); // Should be error modal 
		modal.show();
    }	
};

const cancelTournament = async (msg) => {
  try {
    const response = await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "status": "cancel"});
	status.value = response.status;
	message.value = msg;
  } catch (err) {
    console.error(err.message);
  }
};

const deleteTournament = async (msg) => {
  try {
    const response = await Backend.delete(`/api/tournaments/${tournamentId.value}`);
	message.value = msg;
	router.go(-1);
  } catch (err) {
    console.error(err.message);
  }
};

const startEditing = () => {
    editingDescription.value = true;
};

const updateDescription = async () => {
    try {
        await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "description": description.value });
		editingDescription.value = false;
    } catch (error) {
        console.error('Error updating description:', error);
    }
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
                <p class="lead mb-4">Status: <span class="text-muted">{{ status }}</span></p>
				<div class="mb-3">
					<label for="description" class="form-label">Description:</label>
					<div class="description-container">
						<span v-if="!editingDescription && isCreator && (status === 'created' || status === 'registration_open')" @click="startEditing">{{ description }}</span>
						<textarea class="form-control" id="description" v-model="description" v-if="editingDescription && isCreator && (status === 'created' || status === 'registration_open')" rows="5"></textarea>
						<button v-if="editingDescription && isCreator && (status === 'created' || status === 'registration_open')" class="btn btn-primary mt-3" @click="updateDescription">Update</button>
						<span v-if="!isCreator">{{ description }}</span>
					</div>
				</div>

                <div class="row mt-5">
                    <div class="col-md-6">
                        <p class="text-muted">Created at: {{ created_at ? created_at.slice(0, 10) : 'N/A' }}</p>
                    </div>
                    <div class="col-md-6">
						<p class="text-muted">Last updated: {{ updated_at ? updated_at.slice(0, 10) : 'N/A' }}</p>
                    </div>
                </div>

				<div v-if="status === 'created'">
					<button type="button" class="btn btn-primary" v-if="isCreator" data-bs-toggle="modal" data-bs-target="#successModal" @click="changeState('Registrations are now open')" >Open registration</button>
					<span v-if="isCreator">&nbsp;&nbsp;</span>
					<button type="button" class="btn btn-primary" v-if="isCreator" data-bs-toggle="modal" data-bs-target="#successModal" @click="deleteTournament('The tournament has been deleted')">Delete tournament</button> <!-- is the modal opening? -->

					<div class="alert alert-danger" v-else>Registration for this tournament is not yet open (contact <b>{{ creator }}</b> for more info)</div>
				</div>
				
				<div v-if="status === 'registration_open'">
					<button type="button" class="btn btn-primary" v-if="isCreator" data-bs-toggle="modal" data-bs-target="#successModal" @click="changeState('Registrations are now closed')" >Close registration</button>
					<span v-if="isCreator">&nbsp;&nbsp;</span>
					<button type="button" class="btn btn-primary" v-if="isCreator" data-bs-toggle="modal" data-bs-target="#successModal" @click="cancelTournament('The tournament has been cancelled')">Cancel tournament</button>
        			<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#successModal" v-else @click="isJoined ? unjoinTournament('You\'ve successfully unjoined the tournament!') : joinTournament('You\'ve successfully joined the tournament!')">{{ isJoined ? 'Unjoin' : 'Join' }}</button>			
				</div>

				<div v-if="status === 'registration_closed'">
					<button type="button" class="btn btn-primary" v-if="isCreator" data-bs-toggle="modal" data-bs-target="#successModal" @click="changeState('Registrations are now closed')">Start tournament</button>
					<span v-if="isCreator">&nbsp;&nbsp;</span>
					<button type="button" class="btn btn-primary" v-if="isCreator" data-bs-toggle="modal" data-bs-target="#successModal" @click="cancelTournament('The tournament has been cancelled')">Cancel tournament</button>
					<div class="alert alert-success" v-else>The tournament will start soon</div>
				</div>

				<div v-if="status === 'ongoing'">
					<div class="tcontainer">
						<div class="tournament-bracket__round">
							<GameSelection title="Select a game" :is_Creator="isCreator" :tournament_Id="tournamentId" :games.sync="games" @update:games="handleUpdateTesT"></GameSelection>								
						</div>
					</div>
				</div>
            </div>

			<ModalSettings
			  :message_child="message"
			  type_child="Success"
			/>	

            <div class="col-lg-4">
                <h3 class="mb-3">Created by</h3>
				<b><p>{{ creator }} <!-- tournament.creator.nickname -->
				<span v-if="isCreator">(You)</span></p></b>
                <h3 class="mb-3 mt-4">Players</h3>
                <table class="table">
                    <thead>
                        <tr><th>Nickname</th></tr>
                    </thead>
                    <tbody>
                        <tr v-for="(player, index) in players" :key="index">
							<td>
								<b v-if="player.username === username">{{ player.nickname }} (You)</b>
        						<template v-else>{{ player.nickname }}</template>
							</td>
                        </tr>
                    </tbody>
                </table>
				<GameSelection v-if="status === 'ongoing'" title="Finished games" :is_Creator="isCreator" :tournament_Id="tournamentId" :games="updatedGames" @update:games="handleUpdateTesT"/>
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
