<script setup>
import { onMounted, ref, defineProps } from 'vue';
import Backend from '../../js/Backend';
import Podium from './Podium.vue';
import { useI18n } from 'vue-i18n';

const playerWins = ref([]);
const tournament = ref(null);
const playersTournament = ref(null);
const podium = ref(null);

const props = defineProps({
  games: {
    default: null
  }
});

const fetchData = async () => {
  try {
	tournament.value = await Backend.get(`/api/tournaments/${props.games[0].tournament.id}`);
	playersTournament.value = tournament.value.players;
	playersTournament.value.forEach(player => {
        playerWins.value.push({
            playerId: player.id,
            wins: 0,
            points: 0
        });
     });
	calculateWinner();
  } catch (err) {
    console.error(err.message);
  }
};


const calculateWinner = async () => {
	if (props.games && props.games.length > 0) {
		props.games.forEach(game => {
			if (game.status === 'done') {
				const player1Index = playerWins.value.findIndex(player => player.playerId === game.player1.id);
                const player2Index = playerWins.value.findIndex(player => player.playerId === game.player2.id);
				if (game.player1_score > game.player2_score) {
                    playerWins.value[player1Index].wins++;
                    playerWins.value[player1Index].points += (game.player1_score - game.player2_score);
                    playerWins.value[player2Index].points -= (game.player1_score - game.player2_score);
                } else if (game.player2_score > game.player1_score) {
                    playerWins.value[player2Index].wins++;
                    playerWins.value[player2Index].points += (game.player2_score - game.player1_score);
                    playerWins.value[player1Index].points -= (game.player2_score - game.player1_score);
                }
			}
		});

		const sortedPlayerWins = Object.values(playerWins.value).sort((a, b) => {
    		if (a.wins !== b.wins) {
        		return b.wins - a.wins;
    		} else {
        		return b.points - a.points;
    		}
		});
		playerWins.value = sortedPlayerWins;
		podium.value = sortedPlayerWins.slice(0, 3).map(player => getPlayer(player.playerId));
	}
};


const getPlayer = (playerId) => {
	const id = parseInt(playerId);
	return playersTournament.value.find(player => player.id === id);
};

onMounted(() => {
	fetchData();
})

</script>

<template>
	<Podium v-if="podium" :podium="podium"></Podium>
	<div>
	  <table class="table table-striped table-hover text-center-custom">
		<thead>
		  <tr>
			<th scope="col">{{useI18n().t('winnerranking.rank')}}</th>
			<th scope="col">{{useI18n().t('winnerranking.user')}}</th>
			<th scope="col">{{useI18n().t('winnerranking.gameswon')}}</th>
			<th scope="col">{{useI18n().t('winnerranking.totalpoints')}}</th>
		  </tr>
		</thead>
		<tbody>
			<tr v-for="(playerData, index) in playerWins" :key="playerData.playerId">
			<td>{{ index + 1 }}</td>
			<td>
        		<router-link :to="'/users/' + playerData.playerId"> 
            	{{ getPlayer(playerData.playerId).nickname }} 
       			</router-link>
    		</td>
			<td>{{ playerData.wins }}</td>
    		<td>{{ playerData.points }}</td>
		  </tr>
		</tbody>
	  </table>
	</div>
  </template>
  

<style>

.text-center-custom {
  text-align: center;
}

</style>


