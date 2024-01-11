<script setup>
import { useI18n } from 'vue-i18n';
// import PostRequest from '../components/common/PostRequest.vue';
import TournamentsTable from '../components/dashboard/TournamentsTable.vue';
import AddTournament from '../components/dashboard/AddTournament.vue';
import axios from 'axios';
import { ref, onMounted } from 'vue';

// Use a reactive variable as a key
const tableKey = ref(0);

const tournaments = ref(null);

const fetchData = async () => {
  try {
    const response = await axios.get('/api/tournaments/');
    console.log(response.data); // Log the response data to the console
    tournaments.value = response.data.tournaments; // Fill users variable with values
    console.log('Tournaments updated:', tournaments.value);
    return response.data;  // Return the data to be used in the template
  } catch (error) {
    console.error('Error fetching data:', error);
    return null;
  }
};

// Function to update tournaments and trigger a re-render
const updateTournaments = () => {
  // Fetch updated tournaments
  // ...

  // Update the reactive variable key to force a re-render
  tableKey.value += 1;
};

onMounted(() => {
  updateTournaments();
  fetchData();
})
</script>

<template>
  <div>
    <!-- <GetRequest :apiPath="'/api/tournaments/'"></GetRequest>
    <PostRequest
      :apiPath="'/api/tournaments/'"
      :data='formData'>
    </PostRequest> -->
    <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
    <TournamentsTable :tournaments="tournaments" :key="tableKey.value" />
    <AddTournament :fetchData="fetchData"/>
  </div>
</template>

<style>
</style>
