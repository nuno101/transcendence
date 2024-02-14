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
const created_at = ref(null);
const updated_at = ref(null);
const nickname = ref(null);
const creator = ref(null);
const players = ref([]);
const isCreator = ref(false);
const isJoined = ref(false);

const fetchData = async () => {
  try {
    tournament.value = await Backend.get(`/api/tournaments/${tournamentId.value}`);
	const users = await Backend.get('/api/users/me');
    nickname.value = users.nickname;
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
	created_at.value = data.created_at
	updated_at.value = data.updated_at
	creator.value = data.creator.nickname
	players.value = data.players;
	if (creator.value === nickname.value) {
    	isCreator.value = true;
}
};

const joinTournament = async () => {
    const currentPlayer = nickname.value;
    await Backend.patch(`/api/tournaments/${tournamentId.value}`, { player: currentPlayer });
	isJoined.value = true;
	console.log("PLAYERS : ");
	console.log(status.value);
};

onMounted(() => {
	const route = useRoute();
  	tournamentId.value = route.params.id;
	fetchData();
})
</script>

<template>
    <div class="container mt-5">
        <h1 class="display-4 mb-4">{{ title }}</h1>
        <div class="row">
            <div class="col-lg-8">
                <p class="lead mb-4">Status: <span class="text-muted">{{ status }}</span></p>
                <p>{{ description }}</p>
                <div class="row mt-5">
                    <div class="col-md-6">
                        <p class="text-muted">Created at: {{ created_at ? created_at.slice(0, 10) : 'N/A' }}</p>
                    </div>
                    <div class="col-md-6">
						<p class="text-muted">Last updated: {{ updated_at ? updated_at.slice(0, 10) : 'N/A' }}</p>
                    </div>
                </div>
				<button @click="joinTournament" :disabled="isCreator || isJoined" class="btn btn-primary mt-3">Join</button>
				 <!-- Hover over message -->
				<button @click="startMatchmaking" :disabled="!isCreator" class="btn btn-primary mt-3">Matchmaking</button>
				<p class="text-muted">Username: {{ username }}</p>
				<p class="text-muted">isCreator: {{ isCreator }}</p>
				<p class="text-muted">isJoined: {{ isJoined }}</p>
            </div>
            <div class="col-lg-4">
                <h3 class="mb-3">Created by</h3>
                <p>{{ creator }}</p>
                <h3 class="mb-3 mt-4">Players</h3>
                <table class="table">
                    <thead>
                        <tr>
                            <th>Nickname</th>
                            <!-- Add more table headers if needed -->
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(nickname, index) in players" :key="index">
                            <td>{{ nickname }}</td>
                            <!-- Add more table cells if needed -->
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
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
-->