<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const tournament = ref(null);
const tournamentId = ref('');

const fetchData = async () => {
  try {
	console.log("TEST");
    const tournamentData = await Backend.get(`/api/tournaments/${tournamentId.value}`);
    console.log(tournamentData);
	tournament.value = tournamentData;
	return tournamentData;
  } catch (err) {
    console.error(err.message);
  }
};

onMounted(() => {
	const route = useRoute();
  	tournamentId.value = route.params.id;
	console.log("Tournament value:");
	console.log(tournamentId.value);
	fetchData();
})
</script>

<template>
	<div> <!-- Check if tournament is defined before accessing its properties-->
    	<h1>TEST</h1>
		<h2>TEST 2: {{ tournament.title }}</h2>
  	</div>
</template>

<style>
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
-->