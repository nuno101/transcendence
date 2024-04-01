<script setup>
import { onMounted, ref, computed, defineProps } from 'vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle';
import router from '../../router';
import Backend from '../../js/Backend';

const playerWins = ref({});
const tournament = ref(null);
const playersTournament = ref(null);

const props = defineProps({
  games: {
    default: null
  }
});

const fetchData = async () => {
  try {
	tournament.value = await Backend.get(`/api/tournaments/${props.games[0].tournament.id}`);
	playersTournament.value = tournament.value.players;
	console.log("playersTournament_fetchdata: ", playersTournament.value);
	calculateWinner();
  } catch (err) {
    console.error(err.message);
  }
};


const calculateWinner = async () => {
	if (props.games && props.games.length > 0) {
		props.games.forEach(game => {
			if (game.status === 'done') {
				if (!playerWins.value[game.player1.id])
					playerWins.value[game.player1.id] = { wins: 0, points: 0 };
                if (!playerWins.value[game.player2.id])
                    playerWins.value[game.player2.id] = { wins: 0, points: 0 };
				if (game.player1_score > game.player2_score) {
					playerWins.value[game.player1.id].wins++;
					playerWins.value[game.player1.id].points += (game.player1_score - game.player2_score);
					playerWins.value[game.player2.id].points -= (game.player1_score - game.player2_score);
				} 
				else if (game.player2_score > game.player1_score) {
					playerWins.value[game.player2.id].wins++;
					playerWins.value[game.player2.id].points += (game.player2_score - game.player1_score);
					playerWins.value[game.player1.id].points -= (game.player2_score - game.player1_score);
				}
			}
		});

		const sortedPlayerWins = Object.values(playerWins.value).sort((a, b) => {
    		// Sort by wins first
    		if (a.wins !== b.wins) {
        		return b.wins - a.wins; // Sort by wins descending
    		} else {
        	// If wins are equal, sort by points
        		return b.points - a.points; // Sort by points descending
    		}
		});
		// Reassigning sortedPlayerWins to playerWins.value
		playerWins.value = sortedPlayerWins;
		console.log("playerWins.value: ", playerWins.value);
	}
};


const getPlayer = (playerId) => {
	console.log("playertournaments: ", playersTournament.value);
	const id = parseInt(playerId);
	return playersTournament.value.find(player => player.id === id);
};

onMounted(() => {
	fetchData();
})

</script>

<template>
	<div>
	  <table class="table table-striped table-hover">
		<thead>
		  <tr>
			<th scope="col">Rank</th>
			<th scope="col">User</th>
			<th scope="col">Games won</th>
			<th scope="col">Total points</th>
		  </tr>
		</thead>
		<tbody>
			<tr v-for="(playerData, playerId, index) in playerWins" :key="playerId">
			<td>{{ playerId }}</td>
			<!--<td>
			  <router-link :to="'/users/' + getPlayer(playerId).id"> 
				{{ getPlayer(playerId).nickname }} 
			</router-link>
			</td>--> 
			<td>{{ playerData.wins }}</td>
			<td>{{ playerData.points }}</td>
		  </tr>
		</tbody>
	  </table>
	</div>
  </template>
  

<style>


</style>
