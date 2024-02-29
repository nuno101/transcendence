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
const errors = ref(null);
const success = ref(null);
const editingDescription = ref(false);
const newDescription = ref('');
const gamesInfo = ref(null);
const isTournamentStarted = ref(false);

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

// use username instead of nickname 
// use the same rror messg from back-end in the front-end 
// implement new join/unjoin logic

const joinTournament = async () => {
	console.log("Join")
    await Backend.post(`/api/tournaments/${tournamentId.value}/play`, { "play": "join" });
	console.log(players.value);
	const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
	isJoined.value = true;
	localStorage.setItem(userTournamentKey, JSON.stringify(true)); // Check this syntax
	await Backend.patch(`/api/users/me`, { "tournament_id": `${tournamentId.value}` });
	success.value = "You've successfully joined the tournament!"; // msg from vue-i18n
};

const unjoinTournament = async () => {
	console.log("Unjoin")
    await Backend.post(`/api/tournaments/${tournamentId.value}/play`, { "play": "unjoin" });
	console.log(players.value);
	const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
	isJoined.value = false;
	localStorage.setItem(userTournamentKey, JSON.stringify(false)); // Check this syntax
	await Backend.patch(`/api/users/me`, { "tournament_id": `${tournamentId.value}` });
	success.value = "You've successfully unjoined the tournament! "; // msg from vue-i18n
};

/* const getMinClosingTime = () => {
     // Get the current date and time
	 const now = new Date();
    // Get the current time as HH:MM format
    const currentTime = `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}`;
    // Format the current date and time to match the input type
    const minTime = `${now.getFullYear()}-${(now.getMonth() + 1).toString().padStart(2, '0')}-${now.getDate().toString().padStart(2, '0')}T${currentTime}`;
    return minTime;
}; */

const changeState = async () => {
	try {
		const response = await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "status": "next"});
		console.log(response);
		status.value = response.data.status;
	} catch (error) {
        console.error('Error:', error);
		errors.value = error.message; // should be translatable 
		const modal = bootstrap.Modal.getInstance("#errorModal");
		modal.show();
    }	
};

/*  const startInterval = async () => {
	setInterval(() => {
        if (selectedOption.value === 'option2' && closingTime.value) {
            const currentTime = new Date();
            const closingTimeDate = new Date(closingTime.value);
            if (currentTime >= closingTimeDate) {
				console.log("closing Time : ", closingTime.value);
				console.log("closingTimeDate : ", closingTimeDate.value);
                console.log("TEST");
            }
        }
    }, 1000);
}; */


const openRegSettings = async () => {
    try {
        // Store closingTime and selectedOption locally for this tournament
        localStorage.setItem(`tournament_${tournamentId.value}_selectedOption`, selectedOption.value);
		console.log(selectedOption.value);
		changeState();

		/* 
        if (selectedOption.value === 'option2') {
			localStorage.setItem(`tournament_${tournamentId.value}_closingTime`, closingTime.value);
			startInterval();
        } */

		const modal = bootstrap.Modal.getInstance("#RegistrationSetting");
		modal.hide();
    } catch (error) {
        console.error('Error:', error);
    }
};

const cancelTournament = async () => {
  try {
    const response = await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "status": "cancel"});
	success.value = "Tournament has been cancelled"; // msg from vue-i18n
  } catch (err) {
    console.error(err.message);
  }
};

const deleteTournament = async () => {
  try {
    await Backend.delete(`/api/tournaments/${tournamentId.value}`);
	success.value = "Tournament has been deleted"; // msg from vue-i18n
  } catch (err) {
    console.error(err.message);
  }
};

const startEditing = () => {
    editingDescription.value = true;
};

const updateDescription = async () => {
    try {
        // Make the PATCH request to update the description
        await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "description": description.value });

        // Optionally, display a success message or perform other actions
        console.log('Description updated successfully! : ', description.value);
		editingDescription.value = false;
    } catch (error) {
        console.error('Error updating description:', error);
    }
};

const startTournament = async () => {
    try {
        gamesInfo.value = await Backend.get(`/api/tournaments/${tournamentId.value}/games`);
        console.log('Response : ', gamesInfo.value);
		isTournamentStarted.value = true;
    } catch (error) {
        console.error(error.message);
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
				<template v-if="status === 'created'">
				<!-- Button to trigger modal -->
				<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#RegistrationSetting" v-if="isCreator">Open registration</button>
				<span>&nbsp;&nbsp;</span>
				<button type="button" class="btn btn-primary" @click=deleteTournament() v-if="isCreator" data-bs-toggle="modal" data-bs-target="#successModal">Delete tournament</button>
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
								<form @submit.prevent="openRegSettings"> <!-- Add form element with submit.prevent -->
								<!-- Option 1: Close registration manually -->
								<div class="form-check">
									<input class="form-check-input" type="radio" id="option1" name="registrationOption" value="option1" v-model="selectedOption">
									<label class="form-check-label" for="option1">Close registration manually</label>
								</div>

								<div class="form-check">
									<input class="form-check-input" type="radio" id="option2" name="registrationOption" value="option2" v-model="selectedOption">
									<label class="form-check-label" for="option2">Set a closing time for registrations</label>
								</div>

								<div v-if="selectedOption === 'option2'">
									<label for="closingTime">Closing Time:</label>
									<input type="datetime-local" id="closingTime" v-model="closingTime" :min="getMinClosingTime()" required>
									<!-- Add the required attribute to the input field -->
								</div>
								<!-- Confirm and Cancel buttons -->
								<div class="mt-3">
									<p>{{ selectedOption }}</p>
									<button type="submit" class="btn btn-primary">Confirm</button> <!-- Change type to submit -->
									<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
								</div>	
							</form>
							</div>
						</div>
					</div>
				</div>	
				</template>
				
				<template v-else-if="status === 'registration_open'">
					<button type="button" class="btn btn-primary" v-if="isCreator" @click=changeState() >Close registration</button>
					<!-- Modal for displaying error message 
					Should this modal only be for creator ?  -->
					<div class="modal fade" id="errorModal" tabindex="-1" aria-labelledby="errorModalLabel" aria-hidden="true">
						<div class="modal-dialog">
							<div class="modal-content">
								<div class="modal-header">
									<h5 class="modal-title" id="errorModalLabel">Error</h5>
									<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
								</div>
								<div class="modal-body">
									<p>{{ errors }}</p>
								</div>
								<div class="modal-footer">
									<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
								</div>
							</div>
						</div>
					</div>
					<span>&nbsp;&nbsp;</span>
					<button type="button" class="btn btn-primary" v-if="isCreator" @click=cancelTournament() data-bs-toggle="modal" data-bs-target="#successModal" >Cancel tournament</button>

        			<button type="button" class="btn btn-primary" v-else @click="isJoined ? unjoinTournament() : joinTournament()" data-bs-toggle="modal" data-bs-target="#successModal" >{{ isJoined ? 'Unjoin' : 'Join' }}</button>
				
				</template>

				<template v-else-if="status === 'registration_closed'">
				<button type="button" class="btn btn-primary" v-if="isCreator" @click="startTournament()">Start tournament</button>
				<span>&nbsp;&nbsp;</span>
				<button type="button" class="btn btn-primary" v-if="isCreator" @click="cancelTournament" data-bs-toggle="modal" data-bs-target="#successModal">Cancel tournament</button>
				<!-- Overlay and message box for the creator -->
				<h1 class="display-4 mb-4">{{ isTournamentStarted }}</h1>
				<div class="overlay" v-if="isTournamentStarted && isCreator">
					<div class="message-box">
					<p v-if="gamesInfo && gamesInfo.length > 0">Tournament Bracket:</p>
					<ul v-if="gamesInfo && gamesInfo.length > 0" class="tournament-bracket">
						<!-- Iterate over gamesInfo array to display game information -->
						<li class="bracket-column" v-for="(game, index) in gamesInfo" :key="index">
							<p>Round {{ Math.ceil(index / 2) }}:</p>
							<ul class="game">
								<li>
									<p>{{ game.player1.nickname }}</p>
								</li>
								<li>
									<p>{{ game.player2.nickname }}</p>
								</li>
							</ul>
						</li>
					</ul>
					<p v-else>No games information available.</p>
				</div>

				</div>
				<div class="overlay" v-else-if="!isCreator">
					<div class="message-box">
						<!-- Message for non-creator users -->
						<p>Time to join <b>{{ creator }}</b>. Please gather round at their computer.</p>
					</div>
				</div>
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

	<!-- Modal for success message -->
	<div class="modal fade" id="successModal" tabindex="-1" aria-labelledby="successModalLabel" aria-hidden="true">
						<div class="modal-dialog">
							<div class="modal-content">
								<div class="modal-header">
									<h5 class="modal-title" id="successModalLabel">Success</h5>
									<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
								</div>
								<div class="modal-body">
                					<p>{{ success }}</p>
            					</div>
								<div class="modal-footer">
									<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
								</div>
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
    width: 80%; /* Set width to 80% of the screen */
    max-width: 800px; /* Set a maximum width to ensure it doesn't exceed a certain size */
    margin: 0 auto; /* Center the message box horizontally */
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
    text-align: center; 
}

.tournament-bracket {
    list-style-type: none;
    padding: 0;
}

.game {
    display: flex;
    justify-content: space-between;
	list-style-type: none;
    padding: 10px 0;
    flex-direction: column;
}

.game li {
    flex: 1;
    text-align: center;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    margin: 0 5px;
}

.game p {
    margin: 0;
}

.bracket-column {
    width: 25%; /* Each bracket column takes up 25% of the message box width */
}


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