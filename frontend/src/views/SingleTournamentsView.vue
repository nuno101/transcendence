<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import ModalSettings from '../components/tournaments/ModalSettings.vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle';


const tournament = ref(null);
const tournamentId = ref(null);
const title = ref(null);
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
const selectedOption = ref('option1');
const closingTime = ref(0);

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
	console.log("Join")
    await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "player": `${nickname.value}` });
	console.log(players.value);
	const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
	isJoined.value = true;
	localStorage.setItem(userTournamentKey, JSON.stringify(true)); // Check this syntax 
};

const unjoinTournament = async () => {
	console.log("Unjoin")
    await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "player": `${nickname.value}` });
	console.log(players.value);
	const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
	isJoined.value = false;
	localStorage.setItem(userTournamentKey, JSON.stringify(false)); // Check this syntax 
};

const getMinClosingTime = () => {
     // Get the current date and time
	 const now = new Date();
    // Get the current time as HH:MM format
    const currentTime = `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}`;
    // Format the current date and time to match the input type
    const minTime = `${now.getFullYear()}-${(now.getMonth() + 1).toString().padStart(2, '0')}-${now.getDate().toString().padStart(2, '0')}T${currentTime}`;
    return minTime;
};

const changeState = async () => {
	const response = await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "status": "next"});
	status.value = response.data.status;
};

const openRegSettings = async () => {
    try {
        // Store closingTime and selectedOption locally for this tournament
        localStorage.setItem(`tournament_${tournamentId.value}_selectedOption`, selectedOption.value);

        if (selectedOption.value === 'option1') {
			changeState();
        } else if (selectedOption.value === 'option2') {
			localStorage.setItem(`tournament_${tournamentId.value}_closingTime`, closingTime.value);
            console.log("TEST2")
        }
        // Close the modal after confirming settings
		const modal = bootstrap.Modal.getInstance("#RegistrationSetting");
		modal.hide();
    } catch (error) {
        console.error('Error:', error);
    }
};

const closeRegSettings = async () => {
    try {
		changeState();
    } catch (error) {
        console.error('Error:', error);
    }
};

const printPlayers = async () => {
	console.log(players.value);
};


onMounted(() => {
	const route = useRoute();
  	tournamentId.value = route.params.id;
	fetchData();

	setInterval(() => {
            if (selectedOption.value === 'option2' && closingTime.value) {
                const currentTime = new Date();
                const closingTimeDate = new Date(closingTime.value);
                if (currentTime >= closingTimeDate) {
                    changeState();
                }
            }
        }, 1000);
})
</script>


<template>
    <div class="container mt-5">
        <h1 class="display-4 mb-4">{{ title }}</h1>
        <div class="row">
            <div class="col-lg-8">
                <p class="lead mb-4">Status: <span class="text-muted">{{ status }}</span></p>
                <p>{{ description }}</p>
                <div class="row mt-5">
                    <div class="col-md-6">
                        <p class="text-muted">Created at: {{ created_at ? created_at.slice(0, 10) : 'N/A' }}</p>
                    </div>
                    <div class="col-md-6">
						<p class="text-muted">Last updated: {{ updated_at ? updated_at.slice(0, 10) : 'N/A' }}</p>
                    </div>
                </div>
				<p>{{ selectedOption }}</p>
				<template v-if="status === 'created'">
				<!-- Button to trigger modal -->
				<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#RegistrationSetting" v-if="isCreator">Open registration</button>
				<!-- Alert message for when registration is not open -->
				<div class="alert alert-danger" v-else>Registration for this tournament is not yet open (contact <b>{{ creator }}</b> for more info)</div>
				<!-- Modal component (conditionally rendered based on isCreator) -->
				<div class="modal fade" id="RegistrationSetting" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="RegistrationSettingModal" aria-hidden="true">
					<div class="modal-dialog">
						<div class="modal-content">
							<div class="modal-header">
								<h1 class="modal-title fs-5" id="RegistrationSettingModal">Choose the registration settings</h1>
								<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
							</div>
							<div class="modal-body">
								<!-- Option 1: Close registration manually -->
								<div class="form-check">
            						<input class="form-check-input" type="radio" id="option1" name="registrationOption" value="option1" v-model="selectedOption">
            						<label class="form-check-label" for="option1">Close registration manually</label>
        						</div>

								<div class="form-check">
									<input class="form-check-input" type="radio" id="option2" name="registrationOption" value="option2" v-model="selectedOption" @change="updateClosingTime">
									<label class="form-check-label" for="option2">Set a closing time for registrations</label>
								</div>

								<div v-if="selectedOption === 'option2'">
									<label for="closingTime">Closing Time:</label>
									<input type="datetime-local" id="closingTime" v-model="closingTime" :min="getMinClosingTime()">
								</div>

								<!-- Confirm and Cancel buttons -->
								<div class="mt-3">
									<button type="button" class="btn btn-primary" @click="openRegSettings">Confirm</button>
									<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
								</div>	
							</div>
						</div>
					</div>
				</div>	
				</template>
				
				<template v-else-if="status === 'registration_open'">
					<button type="button" class="btn btn-primary" v-if="isCreator && selectedOption === 'option1'" @click="closeRegSettings">Close registration</button>
        			<template v-else-if="selectedOption === 'option2'">
            			<p>{{ closingTime }}</p>
        			</template>
        			<button type="button" class="btn btn-primary" v-else @click="isJoined ? unjoinTournament() : joinTournament()">{{ isJoined ? 'Unjoin' : 'Join' }}</button>
				</template>

				<template v-else-if="status === 'registration_closed'">
				</template>

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
                        <tr v-for="(player, index) in players" :key="index"> <!-- Test it -->
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
</style>

<!--
path("users/<int:user_id>/stats"

VS 

await Backend.get(`/api/users/${users.id}/stats`);

VS

const tournamentId = route.params.id;
const endpoint = `/api/tournaments/${tournamentId}`;
const response = await Backend.get(endpoint);

How do I make the URL looks like:
http://localhost/tournaments/<id> 
with id being the actual id 

<h2>TEST 2 : {{ tournamentId.value }}</h2>

-->
-->