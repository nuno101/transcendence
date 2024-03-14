<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { computed, ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
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
const nickname = ref(null);
const creator = ref(null);
const players = ref([]);
const isCreator = ref(false);
const isJoined = ref(false);
const currentUser = ref(false);
const message = ref(null);
const editingDescription = ref(false);
const newDescription = ref('');

const route = useRoute();

watch(route, (newRoute) => {
  bootstrap.Modal.getInstance("#successModal")?.hide()
})

const fetchData = async () => {
  try {
    tournament.value = await Backend.get(`/api/tournaments/${tournamentId.value}`);
	currentUser.value = await Backend.get('/api/users/me');
    nickname.value = currentUser.value.nickname;
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
	if (creator.value === nickname.value) {
    	isCreator.value = true;
	}
};

const joinTournament = async () => {
    await Backend.post(`/api/tournaments/${tournamentId.value}/play`, { "play": "join" });
	console.log(players.value);
	const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
	isJoined.value = true;
	localStorage.setItem(userTournamentKey, JSON.stringify(true)); // Check this syntax
	await Backend.patch(`/api/users/me`, { "tournament_id": `${tournamentId.value}` });
	message.value = "You've successfully joined the tournament!"; // msg from vue-i18n
};

const unjoinTournament = async () => {
    await Backend.post(`/api/tournaments/${tournamentId.value}/play`, { "play": "unjoin" });
	console.log(players.value);
	const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
	isJoined.value = false;
	localStorage.setItem(userTournamentKey, JSON.stringify(false)); // Check this syntax
	await Backend.patch(`/api/users/me`, { "tournament_id": `${tournamentId.value}` });
	message.value = "You've successfully unjoined the tournament! "; // msg from vue-i18n
};

const changeState = async () => {
	try {
		const response = await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "status": "next"});
		console.log('Response : ', response);
		status.value = response.value.status;
	} catch (error) {
        console.error('Error:', error);
		message.value = error.message; // Should be translatable 
		const modal = bootstrap.Modal.getInstance("#successModal");
		modal.show();
    }	
};

const cancelTournament = async () => {
  try {
    const response = await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "status": "cancel"});
	message.value = "Tournament has been cancelled"; // msg from vue-i18n
  } catch (err) {
    console.error(err.message);
  }
};

const deleteTournament = async () => {
  try {
    await Backend.delete(`/api/tournaments/${tournamentId.value}`);
	message.value = "Tournament has been deleted"; // msg from vue-i18n
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

        console.log('Description updated successfully! : ', description.value);
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
					<button type="button" class="btn btn-primary" @click=changeState() v-if="isCreator">Open registration</button>
					<span>&nbsp;&nbsp;</span>
					<button type="button" class="btn btn-primary" @click=deleteTournament() v-if="isCreator" data-bs-toggle="modal" data-bs-target="#successModal">Delete tournament</button> <!-- is the modal opening? -->

					<div class="alert alert-danger" v-else>Registration for this tournament is not yet open (contact <b>{{ creator }}</b> for more info)</div>
				</div>
				
				<div v-if="status === 'registration_open'">
					<button type="button" class="btn btn-primary" v-if="isCreator" @click=changeState() >Close registration</button>
					<span>&nbsp;&nbsp;</span>
					<button type="button" class="btn btn-primary" v-if="isCreator" @click=cancelTournament() data-bs-toggle="modal" data-bs-target="#successModal" >Cancel tournament</button>
        			<button type="button" class="btn btn-primary" v-else @click="isJoined ? unjoinTournament() : joinTournament()" data-bs-toggle="modal" data-bs-target="#successModal" >{{ isJoined ? 'Unjoin' : 'Join' }}</button>
					<ModalSettings
					  :message_child="message"
					  type_child="Success"
					/>				
				</div>

				<div v-if="status === 'registration_closed'">
					<button type="button" class="btn btn-primary" v-if="isCreator" @click="changeState()">Start tournament</button>
					<span>&nbsp;&nbsp;</span>
					<button type="button" class="btn btn-primary" v-if="isCreator" @click="cancelTournament()" data-bs-toggle="modal" data-bs-target="#successModal">Cancel tournament</button>
					<div class="alert alert-success" v-else>The tournament will start soon</div>
				</div>

				<div v-if="status === 'ongoing'">
					<div class="overlay">
						<div class="message-box">
							<p>Tournament Progress:</p>
							<div class="tcontainer">
								<div class="tournament-bracket__round">
									<GameSelection title="Select a game" :is_Creator="isCreator" :tournament_Id="tournamentId"/>										
									<GameSelection title="Finished games" :is_Creator="isCreator" :tournament_Id="tournamentId"/>	
								</div>
							</div>
						</div>
					</div>
				</div>
            </div>

            <div class="col-lg-4">
                <h3 class="mb-3">Created by</h3>
				<b><p>{{ creator }}
				<span v-if="isCreator">(You)</span></p></b>
                <h3 class="mb-3 mt-4">Players</h3>
                <table class="table">
                    <thead>
                        <tr><th>Nickname</th></tr>
                    </thead>
                    <tbody>
                        <tr v-for="(player, index) in players" :key="index">
							<td>
								<b v-if="player === nickname">{{ player }} (You)</b>
        						<template v-else>{{ player }}</template>
							</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template> 


<style>
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 999;
}

.message-box {
	height: 85%;
    width: 60%; /* Set width to 80% of the screen */
    max-width: 2000px; /* Set a maximum width to ensure it doesn't exceed a certain size */
    margin: 0 auto; /* Center the message box horizontally */
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
    text-align: center;
	overflow: auto;
	padding-top: 30px;
}

@media (max-width: 768px) {
    .message-box {
        max-width: 100%; /* Allow the message box to occupy the full width of the screen */
        padding: 10px; /* Reduce padding on smaller screens */
		width: 90%;
		overflow: auto;
		padding-top: 30px;
    }
}

/*!
 * Responsive Tournament Bracket
 * Copyright 2016 Jakub Hájek
 * Licensed under MIT (https://opensource.org/licenses/MIT)
 */

.tcontainer {
  width: 90%;
  min-width: 18em;
  margin: 20px auto;
}

.tournament-bracket__round {
  display: block;
  margin-left: -3px;
  flex: 1;
}

</style>
