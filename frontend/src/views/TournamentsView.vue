
<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted, defineProps, watch } from 'vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'
import ModalSettings from '../components/tournaments/ModalSettings.vue';
import { useRoute } from 'vue-router'

const tournaments = ref([])
const userTournaments = ref([])
const input = ref({ title: '', description: '' })
const personalTournaments = ref([]);
const pastedPersonalTournaments = ref([]);
const ongoingPersonalTournaments = ref([]);
const pastedTournaments = ref([]);
const ongoingTournaments = ref([]);
const alerts = ref([])

const currentUser = ref(false);

const route = useRoute();

watch(route, (newRoute) => {
  bootstrap.Modal.getInstance("#CreateTournamentModal")?.hide()
  bootstrap.Modal.getInstance("#successModal")?.hide()
})


const fetchData = async () => {
  try {
    tournaments.value = await Backend.get('/api/tournaments');
	userTournaments.value = await Backend.get(`/api/users/me`);
	personalTournaments.value = userTournaments.value.tournaments;
	tournaments.value = tournaments.value.filter(tournament => !personalTournaments.value.some(pt => pt.id === tournament.id));
	currentUser.value = userTournaments.value.username;
	pastedPersonalTournaments.value = personalTournaments.value.filter(tournament => tournament.status === 'done' || tournament.status === 'cancelled');
	ongoingPersonalTournaments.value = personalTournaments.value.filter(tournament => tournament.status !== 'done' && tournament.status !== 'cancelled');
	pastedTournaments.value = tournaments.value.filter(tournament => tournament.status === 'done' || tournament.status === 'cancelled');
	ongoingTournaments.value = tournaments.value.filter(tournament => tournament.status !== 'done' && tournament.status !== 'cancelled');
    return tournaments.value;
  } catch (err) {
    console.error(err.message);
  }
};

const trimAlerts = () => {
	alerts.value = alerts.value.map(item => {
  	// Splitting the message by '\n' and filtering out empty strings
  	let messages = item.message.split("\n").filter(msg => msg.trim() !== "");
  
  	// Creating new objects for each message
  	return messages.map(message => {
    return { message: message.trim() };
  	});
	}).flat();

};

const addNewTournament = async () => {
  try {
	alerts.value = [];
    let data = await Backend.post('/api/tournaments', input.value);
    ongoingPersonalTournaments.value.push(data);
	cancelModal();
	userTournaments.value = await Backend.patch(`/api/users/me`, { "tournament_id": `${data.id}` });
	personalTournaments.value = userTournaments.value.tournaments;
	tournaments.value = tournaments.value.filter(tournament => !personalTournaments.value.some(pt => pt.id === tournament.id));
  } catch (err) {
	alerts.value.push({
		message: err.message,
	})
	trimAlerts();
    console.error(err);
	}
};

const cancelModal = () => {
	resetInputFields();
	alerts.value = []
	const modal = bootstrap.Modal.getInstance("#CreateTournamentModal");
	modal.hide();
};

const resetInputFields = () => {
   input.value.title = '';
   input.value.description = '';
};

<<<<<<< HEAD
onMounted(fetchData)
=======
const formatDateTime = (dateTimeString) => {
  const date = new Date(dateTimeString);
  const formattedDateTime = date.toLocaleString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
  });
  return formattedDateTime;
};

const deleteTournament = async (tournamentId) => {
  try {
    await Backend.delete(`/api/tournaments/${tournamentId}`);
	pastedPersonalTournaments.value = pastedPersonalTournaments.value.filter(tournament => tournament.id !== tournamentId);
  } catch (err) {
    console.error(err.message);
  }
};

onMounted(() => {
	const createTournamentModal = bootstrap.Modal.getInstance("#CreateTournamentModal");

	createTournamentModal?.addEventListener('hidden.bs.modal', () => {
  	// Clear alerts when the modal is hidden
  	alerts.value = [];
	});
	fetchData();
})
>>>>>>> 1aa407da95a6d8d6f90473279b656866eef1b42e

</script>

<template>
	<div class="boxstyling">
	  <div class="box rounded">
		<div>
		  <!-- Tabs -->
		  <ul class="nav nav-tabs" id="myTab" role="tablist">
			<li class="nav-item" role="presentation">
			  <button class="nav-link nav-link-custom active" id="all-tournaments-tab" data-bs-toggle="tab" data-bs-target="#all-tournaments" type="button" role="tab" aria-controls="all-tournaments" aria-selected="true">{{useI18n().t('tournamentsview.ongoingtournaments')}}</button>
			</li>
			<li class="nav-item" role="presentation">
			  <button class="nav-link nav-link-custom" id="my-tournaments-tab" data-bs-toggle="tab" data-bs-target="#my-tournaments" type="button" role="tab" aria-controls="my-tournaments" aria-selected="false">{{useI18n().t('tournamentsview.pasttournaments')}}</button>
			</li>
		  </ul>
		  
		  <!-- Tab panes -->
		  <div class="tab-content" id="myTabContent">
			<div class="tab-pane fade show active" id="all-tournaments" role="tabpanel" aria-labelledby="all-tournaments-tab">
			  <!-- Table for all tournaments -->
			  <h1 class="text-color-custom">{{useI18n().t('tournamentsview.alltournaments')}}</h1>
			  <div v-if="ongoingTournaments.length === 0" class="text-center">
    			<p>{{useI18n().t('tournamentsview.nodataavailable')}}</p>
				</div>
			  <table v-else class="table table-striped table-hover text-center">
				<thead>
						<tr>
							<th scope="col">{{useI18n().t('tournamentsview.title')}}</th>
							<th scope="col">{{useI18n().t('tournamentsview.creator')}}</th>
							<th scope="col">{{useI18n().t('tournamentsview.created_at')}}</th>
							<th scope="col">{{useI18n().t('tournamentsview.last_update')}}</th>
							<th scope="col">{{useI18n().t('tournamentsview.status')}}</th>
							<th scope="col">{{useI18n().t('tournamentsview.players')}}</th>
						</tr>
					</thead>

					<tbody>
						<tr v-for="tournament in ongoingTournaments" :key="tournament.id">
							<td>
								<router-link :to="'/tournaments/' + tournament.id">
									{{ tournament.title }}
								</router-link>
							</td>
							<td>{{ tournament.creator.nickname }}</td>
							<td>{{ formatDateTime(tournament.created_at) }}</td>
							<td>{{ formatDateTime(tournament.updated_at) }}</td>
							<td>{{ useI18n().t(`singletournamentsview.${tournament.status}`)}}</td>
							<td>{{ tournament.players.length }}</td>
						</tr>
					</tbody>
			  </table>


	<div style="margin-top: 20px;"></div>

<!-- Button to create a new tournament -->
<button type="button" class="btn btn-primary custom-button" data-bs-toggle="modal" data-bs-target="#CreateTournamentModal">
   {{useI18n().t('tournamentsview.createatournament')}}
</button>

<!-- Modal -->
<div class="modal fade" id="CreateTournamentModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="CreateTournamentModalLabel" aria-hidden="true">
   <div class="modal-dialog">
	   <div class="modal-content">
		   <div class="modal-header">
			   <h1 class="modal-title fs-5" id="CreateTournamentModalLabel">{{ useI18n().t('tournamentsview.createatournament') }}</h1>
			   <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="cancelModal"></button>
		   </div>
		   <div class="modal-body">
						<div v-if="alerts.length > 0 && !input.title" class="alert alert-danger" style="margin-bottom: 0.5em;">{{ useI18n().te(`err.${alerts[0].message}`) ? useI18n().t(`err.${alerts[0].message}`) :  alerts[0].message}}</div>
					   	<div class="form-group">
						   <label for="title">{{ useI18n().t('tournamentsview.title') }}</label>
						   <input type="text" class="form-control" id="title" placeholder="Enter title" v-model="input.title" required>
					   </div>
					   <br/>
					   <div v-if="alerts.length > 0 && !input.description" class="alert alert-danger" style="margin-bottom: 0.5em;">{{ useI18n().te(`err.${alerts[0].message}`) ? useI18n().t(`err.${alerts[0].message}`) :  alerts[0].message}}</div>
					   <div class="form-group">
						   <label for="description">{{ useI18n().t('tournamentsview.descriptionoftournament') }}</label>
						   <input class="form-control" id="description" placeholder="Enter description" v-model="input.description" required>
					   </div>
					   <br/>
					   <div>
						   <button type="button" class="btn btn-danger" @click="cancelModal">{{ useI18n().t('tournamentsview.cancel') }}</button>
						   <button type="submit" class="btn btn-success" @click="addNewTournament">{{ useI18n().t('tournamentsview.addtournament') }}</button>
					   </div>   
		   </div>
	   </div>
   </div>
</div>

<div style="margin-top: 80px;"></div>

			  <h1 class="text-color-custom">{{useI18n().t('tournamentsview.mytournaments')}}</h1>
			  <div v-if="ongoingPersonalTournaments.length === 0" class="text-center">
    			<p>{{useI18n().t('tournamentsview.nodataavailable')}}</p>
				</div>
			  <table v-else class="table table-striped table-hover text-center">
				<thead>
						<tr>
							<th scope="col">{{useI18n().t('tournamentsview.title')}}</th>
							<th scope="col">{{useI18n().t('tournamentsview.creator')}}</th>
							<th scope="col">{{useI18n().t('tournamentsview.created_at')}}</th>
							<th scope="col">{{useI18n().t('tournamentsview.last_update')}}</th>
							<th scope="col">{{useI18n().t('tournamentsview.status')}}</th>
							<th scope="col">{{useI18n().t('tournamentsview.players')}}</th>
						</tr>
					</thead>

					<tbody>
						<tr v-for="tournament in ongoingPersonalTournaments" :key="tournament.id">
							<td>
								<router-link :to="'/tournaments/' + tournament.id">
									{{ tournament.title }}
								</router-link>
							</td>
							<td>
							<template v-if="tournament.creator.username === currentUser">
								<b>{{ tournament.creator.nickname }} {{useI18n().t('tournamentsview.(you)')}}</b>
							</template>
							<template v-else>
								{{ tournament.creator.nickname }}
							</template>
                    	</td>
							<td>{{ formatDateTime(tournament.created_at) }}</td>
							<td>{{ formatDateTime(tournament.updated_at) }}</td>
							<td>{{ useI18n().t(`singletournamentsview.${tournament.status}`)}}</td>
							<td>{{ tournament.players.length }}</td>
						</tr>
					</tbody>
			  </table>

			</div>
			<div class="tab-pane fade" id="my-tournaments" role="tabpanel" aria-labelledby="my-tournaments-tab">
			  <!-- Table for ongoing tournaments you are part of -->
			  <h1 class="text-color-custom">{{useI18n().t('tournamentsview.alltournaments')}}</h1>
			  <div v-if="pastedTournaments.length === 0" class="text-center">
    			<p>{{useI18n().t('tournamentsview.nodataavailable')}}</p>
				</div>
			  <table v-else class="table table-striped table-hover text-center">
				<thead>
							<tr>
								<th scope="col">{{useI18n().t('tournamentsview.title')}}</th>
								<th scope="col">{{useI18n().t('tournamentsview.creator')}}</th>
								<th scope="col">{{useI18n().t('tournamentsview.created_at')}}</th>
								<th scope="col">{{useI18n().t('tournamentsview.last_update')}}</th>
								<th scope="col">{{useI18n().t('tournamentsview.status')}}</th>
								<th scope="col">{{useI18n().t('tournamentsview.winner')}}</th>
							</tr>
						</thead>

						<tbody>
							<tr v-for="tournament in pastedTournaments" :key="tournament.id">
								<td>
									<router-link :to="'/tournaments/' + tournament.id">
										{{ tournament.title }}
									</router-link>
								</td>
								<td>
									<template v-if="tournament.creator.username === currentUser">
										<b>{{ tournament.creator.nickname }} {{useI18n().t('tournamentsview.(you)')}}</b>
									</template>
									<template v-else>
										{{ tournament.creator.nickname }}
									</template>
								</td>
								<td>{{ formatDateTime(tournament.created_at) }}</td>
								<td>{{ formatDateTime(tournament.updated_at) }}</td>
								<td>{{ useI18n().t(`singletournamentsview.${tournament.status}`)}}</td>
								<td>
									<router-link v-if="tournament.ranking && tournament.ranking.length > 0" :to="'/users/' + tournament.ranking[0].id"> 
									{{ tournament.ranking[0].nickname }} 
									</router-link>
								</td>
							</tr>
						</tbody>
			  </table>

			  <div style="margin-top: 100px;"></div>

			  <h1 class="text-color-custom">{{useI18n().t('tournamentsview.mytournaments')}}</h1>
			  <div v-if="pastedPersonalTournaments.length === 0" class="text-center">
    			<p>{{useI18n().t('tournamentsview.nodataavailable')}}</p>
				</div>
			  
			  <table v-else class="table table-striped table-hover text-center">
				<thead>
							<tr>
								<th scope="col">{{useI18n().t('tournamentsview.title')}}</th>
								<th scope="col">{{useI18n().t('tournamentsview.creator')}}</th>
								<th scope="col">{{useI18n().t('tournamentsview.created_at')}}</th>
								<th scope="col">{{useI18n().t('tournamentsview.last_update')}}</th>
								<th scope="col">{{useI18n().t('tournamentsview.status')}}</th>
								<th scope="col"></th>
								<th scope="col">{{useI18n().t('tournamentsview.winner')}}</th>
							</tr>
						</thead>

						<tbody>
							<tr v-for="tournament in pastedPersonalTournaments" :key="tournament.id">
								<td>
									<router-link :to="'/tournaments/' + tournament.id">
										{{ tournament.title }}
									</router-link>
								</td>
								<td>
									<template v-if="tournament.creator.username === currentUser">
										<b>{{ tournament.creator.nickname }} {{useI18n().t('tournamentsview.(you)')}}</b>
									</template>
									<template v-else>
										{{ tournament.creator.nickname }}
									</template>
								</td>
								<td>{{ formatDateTime(tournament.created_at) }}</td>
								<td>{{ formatDateTime(tournament.updated_at) }}</td>
								<td>{{ useI18n().t(`singletournamentsview.${tournament.status}`)}}</td>
								<td>
									<template v-if="tournament.creator.username === currentUser">
                    					<i class="bi bi-trash3-fill" style="cursor: pointer;" data-bs-toggle="modal" data-bs-target="#successModal" @click="deleteTournament(tournament.id)"></i>
                					</template>
								</td>
								<td>
									<router-link v-if="tournament.ranking && tournament.ranking.length > 0" :to="'/users/' + tournament.ranking[0].id"> 
									{{ tournament.ranking[0].nickname }} 
									</router-link>
								</td>
							</tr>
						</tbody>
			  </table>
			  <ModalSettings
			  :title_child="useI18n().t('singletournamentsview.success')"
			  :message_child="useI18n().t('singletournamentsview.tournamentisnowdeleted')"
			/>
			</div>
		  </div>
		</div>
	  </div>
	</div>
  </template>
 

<style>

.custom-button {
	background-color: #000000;
	border-color: #000000;
}

.custom-button:hover {
    background-color: #4d20e9;
    border-color: #4d20e9;
}

.text-color-custom {
	color: #4d20e9;
	font-weight: bold;
	padding-top: 0.5em;
}

.nav-link-custom:hover {
    color: #ffffff;
	background-color: #4d20e9;
}

.nav-link-custom {
    color: #4d20e9;
}


</style>