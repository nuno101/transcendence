<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../../js/Backend';
import { ref, defineProps, onMounted, computed } from 'vue';

const props = defineProps(['id']);
const games = ref([]);
const me = ref([]);

onMounted(() => {
    getData();
});

const getData = async() => {
  try {
    games.value = await Backend.get(`/api/users/${props.id}/games`);
    me.value = await Backend.get(`/api/users/${props.id}`);

    for (const game of games.value) {
      const opponentId = game.player1_id === props.id ? game.player2_id : game.player1_id;
      game.opponent = await getOpponentData(opponentId);
    }
    console.log(games.value);
  } catch (err) {
    console.error(err.message);
  }
};
    
const getOpponentData = async (id) => {
    try {
    const response = await Backend.get(`/api/users/${id}`);
    console.log(response.username);
    return response.username;
    } catch (err) {
    console.error(err.message);
    return '';
    }
};

const isWin = (game) => {
  if(game.player1_id === props.id &&
    game.player1_score >= game.player2_score)
    return true;
  else if (game.player2_id === props.id &&
    game.player1_score <= game.player2_score)
    return true;
  return (false);
};

const filteredGames = computed(() => {
    return games.value.filter(game => !isWin(game));
});

</script>


<template>
    <div class="gamestable col-md-5 rounded img-thumbnail d-none d-md-block">
    <table class="table">
        <tbody>
        <tr v-for="game in filteredGames" :key="game">
            <td class="bg-danger align-middle text-start">{{ game.updated_at.slice(0, 10)}}</td>
            <td class="bg-danger d-none d-lg-table-cell">
            <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                alt="..."
                class="img-thumbnail rounded float-end"
                style="width: 50px; height: 50px; object-fit: cover;">
            </td>
            <td class="bg-danger align-middle text-start">{{ game.opponent }}</td>
            <td class="bg-danger align-middle text-end">
                {{ game.player1_id !== props.id
                ? game.player1_score + ' : ' + game.player2_score
                : game.player2_score + ' : ' + game.player1_score}}
            </td>
        </tr>
        </tbody>
    </table>
    </div>   
</template>