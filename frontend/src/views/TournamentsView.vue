
<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted } from 'vue';

const tournaments = ref([])
const submit = ref(false);
const input = defineModel();
input.value = {title: '', description: ''};

const fetchData = async () => {
  try {
    tournaments.value = await Backend.get('/api/tournaments');
    console.log(tournaments.value); // Log the response data to the console  
    return tournaments.value;  // Return the data to be used in the template
  } catch (err) {
    console.error(err.message);
  }
};

const addNewTournament = async () => {
  try {
    let data = await Backend.post('/api/tournaments', input.value);
    console.log("in POST: " + data);
    tournaments.value.push(data);

    resetInputFields();
  } catch (err) {
    console.error(err.message);
  }
};

//FIXME -  the function below is not working atm
const updatestateTournament = async (t_id, state) => {
  try {
    let data = await Backend.put('/api/tournaments/'+ t_id, state);
    console.log("in POST: " + data);
    //tournaments.value.push(data);

    resetInputFields();
  } catch (err) {
    console.error(err.message);
  }
};

const deleteTournament = async (t_id) => {
  try {
    await Backend.delete('/api/tournaments/'+ t_id, input.value);
    console.log("in POST: " + tournaments.value);
    // FIXME - the line below is not working atm. should delete the tournament from the list
    //tournaments.value.delete(t_id)

    resetInputFields();
  } catch (err) {
    console.error(err.message);
  }
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
                    <th scope="col">{{useI18n().t('tournamentsview.name')}}</th>
                    <th scope="col">{{useI18n().t('tournamentsview.creator')}}</th>
                    <th scope="col">{{useI18n().t('tournamentsview.created_at')}}</th>
                    <th scope="col">{{useI18n().t('tournamentsview.updated_at')}}</th>
                    <th scope="col">{{useI18n().t('tournamentsview.status')}}</th>
                    <th scope="col">{{useI18n().t('tournamentsview.actions')}}</th>
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
                        <td>{{ tournament.updated_at }}</td>
                        <td>{{ tournament.status }}</td>
                        <td>
                            <!-- FIXME - the button s below are not working atm -->
                            <button type="button" class="btn btn-primary">{{useI18n().t('tournamentsview.open_register')}}</button>
							              <button type="button" class="btn btn-primary" @click="updatestateTournament(tournament.id, 'cancelled')">{{useI18n().t('tournamentsview.cancel')}}</button>
                            <!-- TODO - disable unless status is created -->
                            <button type="button" class="btn btn-primary" @click="deleteTournament(tournament.id)">{{useI18n().t('tournamentsview.delete')}}</button>
                            <!-- TODO - use icon below instead of button above for deletion -->
                            &nbsp;<a href="" @click="deleteTournament"><i class="bi bi-trash3-fill"></i></a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    <div>
	<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#CreateTournamentModal">
		{{useI18n().t('tournamentsview.createatournament')}}
	</button>

<!-- Modal -->
<div class="modal fade" id="CreateTournamentModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="CreateTournamentModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="CreateTournamentModalLabel">{{ useI18n().t('tournamentsview.modaltitle') }}</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                    <form @submit.prevent="submitForm">
                        <div class="form-group">
                            <label for="title">{{ useI18n().t('tournamentsview.titleoftournament') }}</label>
                            <input type="text" class="form-control" id="title" placeholder="Enter title" v-model="input.title" required>
                        </div>
                        <div class="form-group">
                            <label for="description">{{ useI18n().t('tournamentsview.descriptionoftournament') }}</label>
                            <input class="form-control" id="description" placeholder="Enter description" v-model="input.description" required>
                        </div>
                        <br/>
                        <div>
                            <button type="button" class="btn btn-danger" @click="resetInputFields" data-bs-dismiss="modal">{{ useI18n().t('tournamentsview.cancel') }}</button>
                            <button type="submit" class="btn btn-success" @click="addNewTournament" data-bs-dismiss="modal">{{ useI18n().t('tournamentsview.addtournament') }}</button>
                        </div>   
                        <PostRequest v-if="submit" :apiPath="'/api/tournaments'" :data='formData'></PostRequest>
                    </form >
            </div>
        </div>
    </div>
</div>
</div >
</div>
</template>

<style>
</style>
