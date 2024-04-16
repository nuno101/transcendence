<script setup>
import { onMounted, ref, defineProps } from 'vue';
import Backend from '../../js/Backend';
import Podium from './Podium.vue';
import { useI18n } from 'vue-i18n';
import { globalUser } from "../../main"

const playerWins = ref([]);
const tournament = ref(null);
const playersTournament = ref(null);
const podium = ref(null);
const DataPlayerWins = ref([]);
const winnerId = ref(null);

const props = defineProps({
  games: {
    default: null
  }
});

const fetchData = async () => {
  try {
	tournament.value = await Backend.get(`/api/tournaments/${props.games[0].tournament.id}`);
	playersTournament.value = tournament.value.players;
	DataPlayerWins.value = tournament.value.ranking;
	podium.value = tournament.value.ranking
  		.filter(entry => entry.wins !== -1)
  		.slice(0, 3)
  		.map(entry => getPlayer(entry.user_id));
  } catch (err) {
    console.error(err.message);
  }
};

const getPlayer = (playerId) => {
	const id = parseInt(playerId);
	return playersTournament.value.find(player => player.id === id);
};

onMounted(fetchData)

</script>

<template>
	<Podium v-if="podium" :podium="podium"></Podium>
	<div>
	  <table class="table table-striped table-hover text-center">
		<thead>
		  <tr>
			<th scope="col">{{useI18n().t('winnerranking.rank')}}</th>
			<th scope="col">{{useI18n().t('winnerranking.user')}}</th>
			<th scope="col">{{useI18n().t('winnerranking.gameswon')}}</th>
			<th scope="col">{{useI18n().t('winnerranking.totalpoints')}}</th>
		  </tr>
		</thead>
		<tbody>
			<tr v-for="(player, index) in DataPlayerWins" :key="player.user_id">
				<td>{{ player.wins !== -1 ? index + 1 : useI18n().t('winnerranking.nodata') }}</td>
				<td>
					<router-link :to="'/users/' + player.user_id"> 
					{{ player.nickname }} 
					</router-link>
				</td>
				<td>{{ player.wins !== -1 ? player.wins : useI18n().t('winnerranking.nodata') }}</td>
				<td>{{ player.points !== -1 ? player.points : useI18n().t('winnerranking.nodata') }}</td>
		    </tr>
		</tbody>
	  </table>
	</div>
  </template>



