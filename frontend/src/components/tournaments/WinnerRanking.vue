<script setup>
import { onMounted, ref, computed, defineProps } from 'vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle';
import router from '../../router';

const playerWins = ref([]);

const props = defineProps({
  games: {
    default: null
  }
});

const calculateWinner = () => {
   console.log("games : ", props.games);
	if (props.games && props.games.length > 0) {
		props.games.forEach(game => {
			if (game.status === 'done') {

				if (!playerWins[game.player1.id]) // Access value property
                    playerWins[game.player1.id] = 0; // Use value property
                if (!playerWins[game.player2.id]) // Access value property
                    playerWins[game.player2.id] = 0; // Use value property
				if (game.player1_score > game.player2_score) {
					playerWins[game.player1.id]++;
				} else if (game.player2_score > game.player1_score) {
					playerWins[game.player2.id]++;
				}	
			}
		});
		playerWins.sort((a, b) => b - a);
		console.log("playerWins 1 : ", playerWins);
		//const firstElement = playerWins.value[0];
	}
};

onMounted(() => {
	calculateWinner();
})

</script>

<template>
<div>
<h1> {{ playerWins }} </h1>

<ul v-if="playerWins && playerWins.length > 0" class="tournament-bracket__list">
	<h1> TEST </h1>
      <li v-for="(winCount, playerId) in playerWins" :key="playerId" class="tournament-bracket__match" tabindex="0">
        <span>Player {{ playerId }}: {{ winCount }} wins</span>
      </li>
    </ul>
</div>
</template>

<style>



</style>
