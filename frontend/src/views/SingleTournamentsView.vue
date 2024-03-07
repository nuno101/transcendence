<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { computed, ref, onMounted } from 'vue';
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
const isClicked = ref(false);
const completedGames = ref(false);

const fetchData = async () => {
  try {
    tournament.value = await Backend.get(`/api/tournaments/${tournamentId.value}`);
	currentUser.value = await Backend.get('/api/users/me');
    nickname.value = currentUser.value.nickname;
	gamesInfo.value = await Backend.get(`/api/tournaments/${tournamentId.value}/games`);	
	completedGames.value = gamesInfo.value.filter(game => game.status === 'done' || game.status === 'cancel');
	gamesInfo.value = gamesInfo.value.filter(game => !completedGames.value.some(pt => pt.id === game.id));
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
		console.log('Response : ', response);
		status.value = response.value.status;
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
        await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "description": description.value });

        console.log('Description updated successfully! : ', description.value);
		editingDescription.value = false;
    } catch (error) {
        console.error('Error updating description:', error);
    }
};

const startTournament = async () => {
    try {
		changeState();
    } catch (error) {
        console.error(error.message);
    }
};

const handleGameClick = (index) => {
	console.log("TEST", index);
    isClicked.value = index;
};

const startGame = () => {
    console.log('Start the game:', gamesInfo.value[isClicked.value]);
};

document.body.addEventListener('click', (event) => {
    if (!event.target.closest('.tournament-bracket__match')) {
        isClicked.value = 0;
    }
});

const cancelGame = async () => {
  try {
    // Cancel a game 
  } catch (err) {
    console.error(err.message);
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

				<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#RegistrationSetting" v-if="isCreator">Open registration</button>
				<span>&nbsp;&nbsp;</span>
				<button type="button" class="btn btn-primary" @click=deleteTournament() v-if="isCreator" data-bs-toggle="modal" data-bs-target="#successModal">Delete tournament</button>

				<div class="alert alert-danger" v-else>Registration for this tournament is not yet open (contact <b>{{ creator }}</b> for more info)</div>

				<div class="modal fade" id="RegistrationSetting" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="RegistrationSettingModal" aria-hidden="true">
					<div class="modal-dialog">
						<div class="modal-content">
							<div class="modal-header">
								<h1 class="modal-title fs-5" id="RegistrationSettingModal">Choose the registration settings</h1>
								<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
							</div>
							<div class="modal-body">
								<form @submit.prevent="openRegSettings"> 

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

								</div>

								<div class="mt-3">
									<p>{{ selectedOption }}</p>
									<button type="submit" class="btn btn-primary">Confirm</button>
									<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
								</div>	
							</form>
							</div>
						</div>
					</div>
				</div>	
				</div>
				
				<div v-if="status === 'registration_open'">
					<button type="button" class="btn btn-primary" v-if="isCreator" @click=changeState() >Close registration</button>

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
				
				</div>

				<div v-if="status === 'registration_closed'">
					<button type="button" class="btn btn-primary" v-if="isCreator" @click="startTournament()">Start tournament</button>
					<span>&nbsp;&nbsp;</span>
					<button type="button" class="btn btn-primary" v-if="isCreator" @click="cancelTournament" data-bs-toggle="modal" data-bs-target="#successModal">Cancel tournament</button>

					<div class="alert alert-success" v-else>The tournament will start soon</div>
				</div>

				<div v-if="status === 'ongoing'">
					<div class="overlay">
						<div class="message-box">
							<p v-if="gamesInfo && gamesInfo.length > 0">Tournament Progress:</p>

							<div class="container">
								<div class="tournament-bracket tournament-bracket--rounded">                                                     
									<div class="tournament-bracket__round">
									<h3 class="tournament-bracket__round-title">Select a game</h3> <!-- NOT IF ALL GAMES ARE DONE -->
									<ul v-if="gamesInfo" class="tournament-bracket__list">
										<li v-for="(game, index) in gamesInfo" :key="index" class="tournament-bracket__item">
											<div class="tournament-bracket__match" :class="{ 'user-not-player': currentUser.nickname !== game.player1.nickname && currentUser.nickname !== game.player2.nickname }" tabindex="0" @click="handleGameClick(index + 1)">						
												<table class="tournament-bracket__table">
													<tbody class="tournament-bracket__content">
														<tr class="tournament-bracket__team">
															<td class="tournament-bracket__country">
																<abbr class="tournament-bracket__code">{{ game.player1.nickname }}</abbr>
															</td>
															<td class="tournament-bracket__score">
																<span class="tournament-bracket__number">_</span>
															</td>
														</tr>
														<tr class="tournament-bracket__team">
															<td class="tournament-bracket__country">
																<abbr class="tournament-bracket__code">{{ game.player2.nickname }}</abbr>
															</td>
															<td class="tournament-bracket__score">
																<span class="tournament-bracket__number">_</span>
															</td>
														</tr>
													</tbody>
													<div style="margin-top: 10px;"></div>
													<h3 class="tournament-bracket__round-title">{{ game.status }}</h3>
												</table>
											</div>
											<div v-if="isClicked === (index + 1)">
												<button v-if="isCreator" class="btn btn-danger" @click="cancelGame(isClicked)">Cancel Game</button>
												<button class="btn btn-success start-game-button" @click="startGame">Start Game</button>
											</div>					
										</li>	
									</ul>
									<p v-else>No games information available.</p>

									<h3 class="tournament-bracket__round-title">Finished games</h3>
									<ul v-if="completedGames" class="tournament-bracket__list">
										<li v-for="(game, index) in completedGames" :key="index" class="tournament-bracket__item">
											<div class="tournament-bracket__match done"  tabindex="0">						
												<table class="tournament-bracket__table">
												<tbody class="tournament-bracket__content">
													<tr class="tournament-bracket__team" :class="{ 'tournament-bracket__team--winner': game.player1_score >= game.player2_score }">
														<td class="tournament-bracket__country">
															<abbr class="tournament-bracket__code">{{ game.player1.nickname }}</abbr>
														</td>
														<td class="tournament-bracket__score">
															<span class="tournament-bracket__number">
																{{ game.player1_score !== undefined && game.player1_score !== '' ? game.player1_score : '_' }} <!-- OR CANCELLED -->
															</span>
														</td>
													</tr>
													<tr class="tournament-bracket__team" :class="{ 'tournament-bracket__team--winner': game.player2_score >= game.player1_score }">
														<td class="tournament-bracket__country">
															<abbr class="tournament-bracket__code">{{ game.player2.nickname }}</abbr>
														</td>
														<td class="tournament-bracket__score">
															<span class="tournament-bracket__number">
																{{ game.player2_score !== undefined && game.player2_score !== '' ? game.player2_score : '_' }}
															</span>
														</td>
													</tr>
												</tbody>
												<div style="margin-top: 10px;"></div>
												<h3 class="tournament-bracket__round-title">{{ game.status }}</h3>
												</table>
											</div>
										</li>
									</ul>
									</div>
								</div>
							</div>
							<!-- <Game View component> Do I insert Game component or do I use the router to change View? --> 
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
	height: 90%;
    width: 50%; /* Set width to 80% of the screen */
    max-width: 800px; /* Set a maximum width to ensure it doesn't exceed a certain size */
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

.start-game-button {
    width: auto; /* Set width to auto to make the button less wide */
    margin-top: 1px; /* Adjust the top margin as needed */
	margin-left: 5px;

}



/*!
 * Responsive Tournament Bracket
 * Copyright 2016 Jakub Hájek
 * Licensed under MIT (https://opensource.org/licenses/MIT)
 */

.container {
  width: 90%;
  min-width: 18em;
  margin: 20px auto;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  border: 0;
}

.tournament-bracket {
  display: flex;
  flex-direction: row;
  
  @media (min-width: @breakpoint-sm) {
    flex-direction: row;
  }
}

.tournament-bracket__round {
  display: block;
  margin-left: -3px;
  flex: 1;
}

.tournament-bracket__round-title {
  color: #9e9e9e;
  font-size: 0.95rem;
  font-weight: 400;
  text-align: center;
  font-style: italic;
}

.tournament-bracket__list {
  flex-direction: column;
  flex-flow: column wrap;
  justify-content: center;
  height: 60%;
  min-height: 60%;
  border-bottom: 1px dashed #e5e5e5;
  transition: padding 0.2s ease-in-out, margin 0.2s ease-in-out;
  
  @media (max-width: @breakpoint-xs) {
    padding-bottom: 1em;
    margin-bottom: 1em;
  }
  
  @media (min-width: @breakpoint-sm) {
    margin-bottom: 0;
    padding-bottom: 0;
    border-right: 1px dashed #e5e5e5;
    border-bottom: 0;
  }
  
  .tournament-bracket__round:last-child & {
    border: 0;
  }
}

.tournament-bracket__item {
  display: flex;
  flex: 0 1 auto;
  justify-content: center;
  flex-direction: column;
  align-items: flex-start;
  position: relative;
  padding: 2% 0;
  width: 48%;
  transition: padding 0.2s linear;
  
  &:nth-child(odd) {
    margin-right: 2%;
  }
  
  &:nth-child(even) {
    margin-left: 2%;
  }
  
  &::after {
    transition: width 0.2s linear;
  }
  
  @media (max-width: @breakpoint-xs) {
    width: 100%;
    
    &:nth-child(odd),
    &:nth-child(even) {
      margin-left: 0;
      margin-right: 0;
    }
  }
  
  @media (min-width: @breakpoint-sm) {
    padding: 0.5em 1em;
    width: 100%;
    
    &:nth-child(odd),
    &:nth-child(even) {
      margin: 0;
    }
    
    &::after {
      position: absolute;
      right: 0;
      content: '';
      display: block;
      width: 1em;
      height: 45%;
      border-right: 2px solid #9e9e9e;
    }

    &:nth-child(odd)::after {
      top: 50%;
      border-top: 2px solid #9e9e9e;
      transform: translateY(-1px);
      
      .tournament-bracket--rounded & {
        border-top-right-radius: 0.6em;
      }
    }
    
    &:nth-child(even)::after {
      bottom: 50%;
      border-bottom: 2px solid #9e9e9e;
      transform: translateY(1px);
      
      .tournament-bracket--rounded & {
        border-bottom-right-radius: 0.6em;
      }
    }
    .tournament-bracket__round:first-child & {
       padding-left: 0;
    }
    .tournament-bracket__round:last-child & {
       padding-right: 0;

       &::after {
         display: none;
       }
    }

    .tournament-bracket__round:nth-last-child(2) & {
      &::after {
        border-radius: 0;
        border-right: 0;
      }
    }  
  }
  
  @media (min-width: @breakpoint-lg) {
    padding: 0.5em 1.5em;
    
    &::after {
      width: 1.5em;
    }
  }
}


.tournament-bracket__match {
  display: flex;
  width: 200%;
  background-color: #ffffff;
  padding: 1.5em;
  padding-bottom: 0.5em;
  border: 1px solid transparent;
  border-radius: 0.2em;
  box-shadow: 0 2px 0 0 #e5e5e5;
  outline: none; 
  cursor: pointer;
  transition: padding 0.2s ease-in-out, border 0.2s linear, background-color 0.2s ease-in-out;

  &:focus {
	background-color: #2196F3;
    border-color: #2196F3;
  }
  
  &::before,
  &::after {
    transition: all 0.2s linear;
  }
  
  @media (max-width: @breakpoint-xs) {
    padding: 0.75em 0.5em;
  }
  
  @media (min-width: @breakpoint-sm) {
    &::before,
    &::after {
      position: absolute;
      left: 0;
      z-index: 1;
      content: '';
      display: block;
      width: 1em;
      height: 10%;
      border-left: 2px solid #9e9e9e;
    }

    &::before  {
      bottom: 50%;
      border-bottom: 2px solid #9e9e9e;
      transform: translate(0, 1px);
      
      .tournament-bracket--rounded & {
        border-bottom-left-radius: 0.6em;
      }
    }

    &::after  {
      top: 50%;
      border-top: 2px solid #9e9e9e;
      transform: translate(0, -1px);
      
      .tournament-bracket--rounded & {
        border-top-left-radius: 0.6em;
      }
    }
  }
  
  @media (min-width: @breakpoint-lg) {
    &::before,
    &::after {
      width: 1.5em;
    }
    
    &::before {
      transform: translate(0, 1px);
    }
    
    &::after {
      transform: translate(0, -1px);
    }
  }
}

.user-not-player {
  background-color: #00000009;;
  cursor: not-allowed;
  pointer-events: none;
}


.done {
  background-color: #00000009;;
  cursor: not-allowed;
  pointer-events: none;
}

.tournament-bracket__round:last-child .tournament-bracket__match {
  &::before,
  &::after {
    border-left: 0;
  }
  
  &::before  {
    border-bottom-left-radius: 0;
  }
  
  &::after  {
    display: none;
  }
}

.tournament-bracket__round:first-child .tournament-bracket__match {
  &::before,
  &::after {
    display: none;
  }
}

.tournament-bracket__content {
  display: flex;
  
  &::after {
    content: ':';
    width: 1em;
    text-align: center;
    padding: 0.2em 0.1em;
    
    @media (min-width: @breakpoint-sm) {
       order: 1;
    }
  }
  
  & .tournament-bracket__team:first-child {
    width: 50%;
    order: 0;
    text-align: right;
    
    @media (min-width: @breakpoint-sm) and (max-width: @breakpoint-md) {
      align-items: flex-end;
    }
    
    & .tournament-bracket__country {
      order: 2;
      justify-content: flex-end;
      
      @media (min-width: @breakpoint-xs) {
        order: 0;
      } 
      
      @media (min-width: @breakpoint-sm) and (max-width: @breakpoint-md) {
        flex-direction: column-reverse;
        align-items: flex-end;
      }
    }
    
    & .tournament-bracket__score {
      order: 0;
      
      @media (min-width: @breakpoint-xs) {
         order: 2;
      }
    }
  }
  
  & .tournament-bracket__team:last-child {
    width: 50%;
    order: 2;
    text-align: left;
    
    @media (min-width: @breakpoint-sm) and (max-width: @breakpoint-md) {
      align-items: flex-start;
    }
    
    & .tournament-bracket__country {
      @media (min-width: @breakpoint-sm) {
        justify-content: flex-start;
      }
      
      @media (min-width: @breakpoint-sm) and (max-width: @breakpoint-md) {
        align-items: flex-start;
      }
    }
    
    .tournament-bracket__code {
      order: 1;
    }
  }
}


.tournament-bracket__table {
  width: 100%;
}

.tournament-bracket__caption {
  font-size: 0.8rem;
  color: #BDBDBD;
  font-weight: 300;
  padding-bottom: 0.75em;
}

.tournament-bracket__team {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-between;
  
  @media (min-width: @breakpoint-xs) {
    flex-direction: column-reverse;
  }
  
  @media (min-width: @breakpoint-sm) {
    flex-direction: column-reverse;
  }
}

.tournament-bracket__country {
  font-size: 0.95rem;
  display: flex;
  margin-top: 0.5em;
  align-items: center;
  
  @media (max-width: @breakpoint-xs) {
    margin-top: 0;
  }
  
  @media (min-width: @breakpoint-sm) and (max-width: @breakpoint-md) {
    display: flex;
    flex-direction: column;
    
    .tournament-bracket__code {
      margin-top: 0.2em;
    }
  }
}

.tournament-bracket__code {
  padding: 0 0.5em;
  color: #212121;
  font-weight: 600;
  text-transform: uppercase;
  border: 0;
  text-decoration: none;
  transition: padding 0.2s ease-in-out;
  
  @media (max-width: @breakpoint-xs) {
    padding: 0 0.25em;
  }
  
  @media (min-width: @breakpoint-sm) and (max-width: @breakpoint-md) {
    padding: 0;
  }
}

.tournament-bracket__score {
  display: flex;
  align-items: center;
  
  .tournament-bracket__team:first-child & {
    flex-direction: row-reverse;
    padding-left: 0.75em;
  }
  
  .tournament-bracket__team:last-child & {
    padding-right: 0.75em;
  }
}

.tournament-bracket__number {
  display: inline-block;
  padding: 0.2em 0.4em 0.2em;
  border-bottom: 0.075em solid transparent;
  font-size: 0.95rem;
  background-color: #00000021;
  border-color: spin(shade(#00000021, 10%), -10);
  
  .tournament-bracket__team--winner & {
    background-color: #ffee58;
    border-color: spin(shade(#ffee58, 2%), -10);
  }
}

.tournament-bracket__medal {
  padding: 0 0.5em;
}

.tournament-bracket__medal--gold {
  color: #FFD700;
}

.tournament-bracket__medal--silver {
  color: #C0C0C0;
}

.tournament-bracket__medal--bronze {
  color: #CD7F32;
}

</style>
