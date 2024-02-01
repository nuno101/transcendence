<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const tournament = ref(null);
const tournamentId = ref(null);
const title = ref(null);
const description = ref(null);
const status = ref(null);

const fetchData = async () => {
  try {
    tournament.value = await Backend.get(`/api/tournaments/${tournamentId.value}`);
    console.log(tournament.value);
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
};	

onMounted(() => {
	const route = useRoute();
  	tournamentId.value = route.params.id;
	console.log("Tournament value: " + tournamentId.value);
	fetchData();
})
</script>

<template>
	<div>
    	<h1>TEST</h1>
		<h2>TEST 2: {{ title }}</h2>
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

<h2>TEST 2 : {{ tournamentId.value }}</h2>

-->