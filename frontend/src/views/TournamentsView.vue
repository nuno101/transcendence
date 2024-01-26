<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted } from 'vue';

const tournaments = ref([])
const submit = ref(false);
const openModal = ref(false);
const input = defineModel();
input.value = {title: '', description: '', creator_id: '1'};

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

const resetInputFields = () => {
    input.value.title = '';
    input.value.description = '';
    // input.value.creator_id = '';
    openModal.value = false;
};

onMounted(() => {
  fetchData();
})
</script>

<template>
  <div>
    <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
    <div>
    <table class="table table-hover">
        <thead>
            <tr>
              <th scope="col">{{useI18n().t('tournamentsview.tournaments')}}</th>
              <th scope="col">{{useI18n().t('tournamentsview.description')}}</th>
              <th scope="col">{{useI18n().t('tournamentsview.status')}}</th>
            </tr>
        </thead>
        <tbody>
            <router-link v-for="tournament in tournaments" :key="tournament.id" :to="'/tournament/' + tournament.id">
				<tr>
                	<td>{{tournament.title}}</td>
                	<td>{{tournament.description}}</td>
                	<td v-if="tournament.status === 'registration_open'">
                  		<button type="button" class="btn btn-outline-success btn-sm">{{useI18n().t('tournamentsview.register')}}</button>
                	</td>
                	<td v-else-if="tournament.status === 'registration_closed'">
                    	{{useI18n().t('tournamentsview.registrationclosed')}}
                	</td>
                	<td v-else>
                    	{{tournament.status}}
                	</td>
            	</tr>
			</router-link>
        </tbody>
    </table>
  </div>
  <div>
    <button type="button" class="btn btn-primary" @click="openModal = !openModal">{{useI18n().t('tournamentsview.addnewtournament')}}</button>
    <div v-show="openModal" class="modal-content">
        <form @submit.prevent="submitForm">
            <div class="form-group">
                <label for="title">{{useI18n().t('tournamentsview.titleoftournament')}}</label>
                <input type="text" class="form-control" id="title" placeholder="Enter title" v-model="input.title" required>
            </div>
            <div class="form-group">
                <label for="description">{{useI18n().t('tournamentsview.descriptionoftournament')}}</label>
                <input class="form-control" id="description" placeholder="Enter description" v-model="input.description" required>
            </div>
            <br/>
            <div>
                <button type="button" class="btn btn-danger" @click="resetInputFields">{{useI18n().t('tournamentsview.cancel')}}</button>
                <button type="submit" class="btn btn-success" @click="addNewTournament">{{useI18n().t('tournamentsview.addtournament')}}</button>
            </div>   
            <PostRequest v-if="submit" :apiPath="'/api/tournaments'" :data='formData'></PostRequest>
        </form >
    </div >
  </div >
  </div>
</template>

<style>
</style>
