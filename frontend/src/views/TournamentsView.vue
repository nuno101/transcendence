
<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted, defineProps, watch } from 'vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'
import SingleTournamentsView from './SingleTournamentsView.vue';
import { useRoute } from 'vue-router'

const tournaments = ref([])
const userTournaments = ref([])
const submit = ref(false);
const input = ref({ title: '', description: '' })
const showAlert = ref(false);
const personalTournaments = ref([]);
const currentUser = ref(false);

const route = useRoute();

watch(route, (newRoute) => {
  bootstrap.Modal.getInstance("#CreateTournamentModal")?.hide()
})

const fetchData = async () => {
  try {
    tournaments.value = await Backend.get('/api/tournaments');
	userTournaments.value = await Backend.get(`/api/users/me`);
	personalTournaments.value = userTournaments.value.tournaments;
	tournaments.value = tournaments.value.filter(tournament => !personalTournaments.value.some(pt => pt.id === tournament.id));
	currentUser.value = userTournaments.value.username;
    return tournaments.value;
  } catch (err) {
    console.error(err.message);
  }
};

const addNewTournament = async () => {
  try {
	const existingTournament = tournaments.value.find(tournament => tournament.title === input.value.title);
    if (existingTournament) {
		resetInputFields();
		showAlert.value = true;
		return;
    }
    let data = await Backend.post('/api/tournaments', input.value);
    tournaments.value.push(data);
	cancelModal();
	showAlert.value = false;
	userTournaments.value = await Backend.patch(`/api/users/me`, { "tournament_id": `${data.id}` });
	personalTournaments.value = userTournaments.value.tournaments;
	tournaments.value = tournaments.value.filter(tournament => !personalTournaments.value.some(pt => pt.id === tournament.id));
	
  } catch (err) {
    console.error(err.message);
  }
};

const cancelModal = () => {
	resetInputFields();
	const modal = bootstrap.Modal.getInstance("#CreateTournamentModal");
	modal.hide();
};

const resetInputFields = () => {
   input.value.title = '';
   input.value.description = '';
};

onMounted(() => {
  fetchData();
})

</script>

<template>
    <div>
        <h1>{{useI18n().t('tournamentsview.listoftournaments')}}</h1>
        <div>
            <table class="table table-striped table-hover">
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
                    <tr v-for="tournament in tournaments" :key="tournament.id">
                        <td>
                            <router-link :to="'/tournaments/' + tournament.id">
                                {{ tournament.title }}
                            </router-link>
                        </td>
                        <td>{{ tournament.creator.username }}</td>
                        <td>{{ tournament.created_at }}</td>
                        <td>{{ tournament.last_update }}</td>
                        <td>{{ useI18n().t(`singletournamentsview.${tournament.status}`)}}</td>
						<td>{{ tournament.players.length }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
	</div>

	<div style="margin-top: 20px;"></div>

 <!-- Button to create a new tournament -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#CreateTournamentModal">
	{{useI18n().t('tournamentsview.createatournament')}}
</button>

<!-- Modal -->
<div class="modal fade" id="CreateTournamentModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="CreateTournamentModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="CreateTournamentModalLabel">{{ useI18n().t('tournamentsview.createatournament') }}</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
				<div v-if="showAlert" class="alert alert-danger" role="alert">
					{{ useI18n().t('tournamentsview.titlealreadytaken') }}
    			</div>
                        <div class="form-group">
                            <label for="title">{{ useI18n().t('tournamentsview.title') }}</label>
                            <input type="text" class="form-control" id="title" placeholder="Enter title" v-model="input.title" required>
                        </div>
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

<div style="margin-top: 100px;"></div>

<!-- Second table for user's tournaments -->
<div>
        <h1>{{useI18n().t('tournamentsview.mytournaments')}}</h1>
        <div>
            <table class="table table-striped table-hover">
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
                    <tr v-for="tournament in personalTournaments" :key="tournament.id">
                        <td>
                            <router-link :to="'/tournaments/' + tournament.id">
                                {{ tournament.title }}
                            </router-link>
                        </td>
						<td>
							<template v-if="tournament.creator.username === currentUser">
								<b>{{ tournament.creator.username }} {{useI18n().t('tournamentsview.(you)')}}</b>
							</template>
							<template v-else>
								{{ tournament.creator.username }}
							</template>
                    	</td>
                        <td>{{ tournament.created_at }}</td>
                        <td>{{ tournament.updated_at }}</td>
                        <td>{{ useI18n().t(`singletournamentsview.${tournament.status}`)}}</td>
						<td>{{ tournament.players.length }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
	</div>

</template>

<style>
</style>
