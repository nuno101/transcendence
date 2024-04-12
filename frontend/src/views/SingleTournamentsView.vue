<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { computed, ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle';
import ModalSettings from '../components/tournaments/ModalSettings.vue';
import GameSelection from '../components/tournaments/GameSelection.vue';
import WinnerRanking from '../components/tournaments/WinnerRanking.vue';
import Loading from '../components/common/Loading.vue';

const { t } = useI18n();

const tournament = ref(null);
const tournamentId = ref(null);
const isCreator = ref(false);
const isJoined = ref(false);
const currentUser = ref(false);
const games = ref(null);
const alerts = ref({ title: '', message: '' })
const dataLoaded = ref(null);

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
	const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
	isJoined.value = localStorage.getItem(userTournamentKey) === 'true';
	if (tournament.value.creator.username === currentUser.value.username)
		isCreator.value = true;
	dataLoaded.value = true;
  } catch (err) {
    console.error(err.message);
  }
};

const handleUpdateTesT = (newValue) => {
    games.value = newValue;
}

const joinTournament = async (msg) => {
	try {
		const join = await Backend.post(`/api/tournaments/${tournamentId.value}/play`, { "play": "join" });
		tournament.value.players = join.players;
		const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
		isJoined.value = true;
		localStorage.setItem(userTournamentKey, JSON.stringify(true));
		await Backend.patch(`/api/users/me`, { "tournament_id": `${tournamentId.value}` });
		setModal(t(`singletournamentsview.success`), msg);
	} catch (error) {
		console.error(error.message);
		setModal(t(`singletournamentsview.errormodal`), t(`err.${error.message}`));
	}
};

const unjoinTournament = async (msg) => {
	try {
		const unjoin = await Backend.post(`/api/tournaments/${tournamentId.value}/play`, { "play": "unjoin" });
		tournament.value.players = unjoin.players;
		const userTournamentKey = `isJoined_${currentUser.value.id}_${tournamentId.value}`;
		isJoined.value = false;
		localStorage.setItem(userTournamentKey, JSON.stringify(false));
		await Backend.patch(`/api/users/me`, { "tournament_id": `${tournamentId.value}` });
		setModal(t(`singletournamentsview.success`), msg);
	} catch (error) {
        console.error(error.message);
		setModal(t(`singletournamentsview.errormodal`), t(`err.${error.message}`));
    }	
};

const changeState = async (msg) => {
	try {
		const response = await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "status": "next"});
		tournament.value.status = response.status;
		setModal(t(`singletournamentsview.success`), msg);
	} catch (error) {
        console.error(error.message);
		setModal(t(`singletournamentsview.errormodal`), t(`err.${error.message}`));
    }
};

const cancelTournament = async (msg) => {
  try {
    const response = await Backend.patch(`/api/tournaments/${tournamentId.value}`, { "status": "cancel"});
	tournament.value.status = response.status;
	setModal(t(`singletournamentsview.success`), msg);
  } catch (err) {
    console.error(err.message);
	setModal(t(`singletournamentsview.errormodal`), t(`err.${err.message}`));
  }
};

const deleteTournament = async (msg) => {
  try {
    await Backend.delete(`/api/tournaments/${tournamentId.value}`);
	setModal(t(`singletournamentsview.success`), msg);
	router.go(-1);
  } catch (err) {
    console.error(err.message);
  }
};

const startTournament = async (msg) => {
  try {
    games.value = await Backend.get(`/api/tournaments/${tournamentId.value}/games`);
	changeState(msg);
  } catch (err) {
    console.error(err.message);
  }
};

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
<div class="boxstyling">
	<div class="box rounded">
		<Loading v-if="!dataLoaded"/>
		<div v-else-if="dataLoaded" class="container mt-4">
        <h1 class="display-4 mb-4 text-color-custom">{{ tournament.title }}</h1>
        <div class="row">
            <div class="col-lg-8">
				<p class="lead mb-4">
  					<span class="status-label text-color-custom">{{useI18n().t('tournamentsview.status')}}:</span>
  					<span class="text-muted" v-if="tournament.status">{{ useI18n().t(`singletournamentsview.${tournament.status}`)}}</span>
				</p>

				<div class="mb-3">
					<label for="description" class="form-label text-color-custom">{{useI18n().t('tournamentsview.description')}}:</label>
					<div class="description-container">
					{{ tournament.description }}
					</div>
				</div>

                <div class="row mt-5">
                    <div class="col-md-6">
                        <p class="text-muted">{{useI18n().t('tournamentsview.created_at')}}: {{ tournament.created_at ? tournament.created_at.slice(0, 10) : 'N/A' }}</p>
                    </div>
                    <div class="col-md-6">
						<p class="text-muted">{{useI18n().t('tournamentsview.last_update')}}: {{ tournament.updated_at ? tournament.updated_at.slice(0, 10) : 'N/A' }}</p>
                    </div>
                </div>

				<div v-if="tournament.status === 'created'">
					<button type="button" class="btn btn-custom" data-bs-toggle="modal" data-bs-target="#successModal" v-if="isCreator" @click="changeState(translatedStrings.registrationIsNowOpen)" >{{ t('singletournamentsview.openregistration') }}</button>
					<span v-if="isCreator">&nbsp;&nbsp;</span>
					<button type="button" class="btn btn-custom" data-bs-toggle="modal" data-bs-target="#successModal" v-if="isCreator" @click="deleteTournament(translatedStrings.tournamentIsNowDeleted)">{{useI18n().t('singletournamentsview.deletetournament')}}</button>

					<div class="alert alert-danger" v-else>{{useI18n().t('singletournamentsview.registrationforthistournamentisnotyetopen')}} <b>{{ tournament.creator.nickname }}</b> {{useI18n().t('singletournamentsview.formoreinfo')}}</div>
				</div>

				<div v-if="tournament.status === 'registration_open'">
					<button type="button" class="btn btn-custom" data-bs-toggle="modal" data-bs-target="#successModal" v-if="isCreator" @click="changeState(translatedStrings.registrationIsNowClosed)" >{{useI18n().t('singletournamentsview.closeregistration')}}</button>
					<span v-if="isCreator">&nbsp;&nbsp;</span>
					<button type="button" class="btn btn-custom" data-bs-toggle="modal" data-bs-target="#successModal" v-if="isCreator" @click="cancelTournament(translatedStrings.theTournamentHasBeenCancelled)">{{useI18n().t('singletournamentsview.canceltournament')}}</button>
        			<button type="button" class="btn btn-custom" data-bs-toggle="modal" data-bs-target="#successModal" v-else @click="isJoined ? unjoinTournament(translatedStrings.successfullUnjoinTournament) : joinTournament(translatedStrings.successfullJoinTournament)">{{ isJoined ? useI18n().t('singletournamentsview.unjointhetournament') : useI18n().t('singletournamentsview.jointhetournament') }}</button>		
				</div>

				<div v-if="tournament.status === 'registration_closed'">
					<div v-if="isCreator">
						<button type="button" class="btn btn-custom" data-bs-toggle="modal" data-bs-target="#successModal" @click="startTournament(translatedStrings.tournamentWillStartGetReady)">{{useI18n().t('singletournamentsview.starttournament')}}</button>
						<span>&nbsp;&nbsp;</span>
						<button type="button" class="btn btn-custom" data-bs-toggle="modal" data-bs-target="#successModal" @click="cancelTournament(translatedStrings.theTournamentHasBeenCancelled)">{{useI18n().t('singletournamentsview.canceltournament')}}</button>
					</div>
					<div class="alert alert-success" v-else-if="isJoined">{{useI18n().t('singletournamentsview.tournamentwillstartgetready')}}</div>
					<div class="alert alert-danger" v-else>{{useI18n().t('singletournamentsview.youarenotpartofthistournament')}}</div>
				</div>

				<div v-if="tournament.status === 'ongoing'">
					<div v-if="isCreator || isJoined" class="tcontainer">
						<div class="tournament-bracket__round">
							<GameSelection title="Select a game" :is_Creator="isCreator" :tournament_Id="tournamentId" :games.sync="games" @update:games="handleUpdateTesT"></GameSelection>								
						</div>
					</div>
					<div class="alert alert-danger" v-else>{{useI18n().t('singletournamentsview.youarenotpartofthistournament')}}</div>
				</div>

				<div v-if="tournament.status === 'done'">
					<div class="tcontainer">
						<div class="tournament-bracket__round">
							<WinnerRanking :games="games"></WinnerRanking>
						</div>
					</div>
            	</div>

				<div v-if="tournament.status === 'cancelled'">
					<button type="button" class="btn btn-custom" data-bs-toggle="modal" data-bs-target="#successModal" v-if="isCreator" @click="deleteTournament(translatedStrings.tournamentIsNowDeleted)">{{useI18n().t('singletournamentsview.deletetournament')}}</button>
				</div>
            </div>


			<ModalSettings
			  :title_child="alerts.title"
			  :message_child="alerts.message"
			/>

            <div class="col-lg-4">
                <h3 class="mb-3 text-color-custom">{{useI18n().t('tournamentsview.creator')}}</h3>
				<b><p>{{ tournament.creator.nickname }}
				<span v-if="isCreator">{{useI18n().t('tournamentsview.(you)')}}</span></p></b>
                <h3 class="mb-3 mt-4 text-color-custom">{{useI18n().t('tournamentsview.players')}}</h3>
                <table class="table">
                    <thead>
                        <tr><th>{{useI18n().t('singletournamentsview.tournamentnickname')}}</th></tr>
                    </thead>
                    <tbody>
                        <tr v-for="(player, index) in tournament.players" :key="index">
							<td>
								<b v-if="player.username === currentUser.username">{{ player.nickname }} {{useI18n().t('tournamentsview.(you)')}}</b>
        						<template v-else>{{ player.nickname }}</template>
							</td>
                        </tr>
                    </tbody>
                </table>
				<GameSelection v-if="tournament.status === 'ongoing' || tournament.status === 'done'" title="Completed games" :is_Creator="isCreator" :tournament_Id="tournamentId" :games="games" @update:games="handleUpdateTesT"/>
            </div>
        </div>
    	</div>
	</div>
</div>
</template> 


<style>

.text-color-custom {
	color: #4d20e9;
	font-weight: bold;
}

.tcontainer {
  width: 90%;
  min-width: 18em;
  padding-top:1em;
  margin: 4px;
}

.tournament-bracket__round {
  display: block;
  margin-left: -3px;
  flex: 1;
}

.btn-custom {
    background-color: #000000;
    border-color: #000000;
    color: #ffffff;
}

/* Hover effect */
.btn-custom:hover {
    background-color: #4d20e9;
    border-color: #4d20e9;
	color: #ffffff;
}


</style>
