<script setup>
import { useI18n } from 'vue-i18n';
import TournamentsTable from '../components/dashboard/TournamentsTable.vue';
import AddTournament from '../components/dashboard/AddTournament.vue';
import axios from 'axios';
import { ref, onMounted } from 'vue';

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
    <TournamentsTable :tournaments="tournaments"/>
    <AddTournament :updateData="fetchData"/>
  </div>
</template>

<style>
</style>
