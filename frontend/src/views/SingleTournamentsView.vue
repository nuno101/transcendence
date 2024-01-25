<script setup>
import { useI18n } from 'vue-i18n';
import axios from 'axios';

const tournaments = ref([]);

const fetchData = async () => {
  try {
    const response = await axios.get('/api/tournaments');
    console.log(response.data); // Log the response data to the console
    tournaments.value = response.data.tournaments; // Fill users variable with values
    // console.log('Tournaments updated:', tournaments.value);
    return response.data;  // Return the data to be used in the template
  } catch (error) {
    console.error('Error fetching data:', error);
    return null;
  }
};

onMounted(() => {
  fetchData();
})

</script>

<template>
  <div>
    <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
    
    
  </div>

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
            <tr v-for="tournament in tournaments" :key="tournament.id">
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
        </tbody>
    </table>
  </div>
</template>

<style>
</style>