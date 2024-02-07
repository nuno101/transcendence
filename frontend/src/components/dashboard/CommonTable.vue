<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../../js/Backend';
import { ref, defineProps, onMounted } from 'vue';

const props = defineProps(['games', 'id']);
const me = ref([]);

onMounted(() => {
    fetchData();
});

const fetchData = async() => {
  try {
    me.value = await Backend.get(`/api/users/${props.id}`);
    for (const game of props.games) {
      const opponentId = game.player1_id === props.id ? game.player2_id : game.player1_id;
      game.opponent = await getOpponentData(opponentId);
    }
  } catch (err) {
    console.error(err.message);
  }
};
    
const getOpponentData = async (id) => {
    try {
    const response = await Backend.get(`/api/users/${id}`);
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
</script>

<template>
    <div class="gamestable col-md-5 rounded img-thumbnail d-md-none">
    <table class="table">
        <tbody>
        <tr v-for="game in games" :key="game">
            <td :class="{ 'bg-success': isWin(game), 'bg-danger': !isWin(game) }"
                class="align-middle text-start">
                {{ game.updated_at.slice(0, 10)}}
            </td>
            <td :class="{ 'bg-success': isWin(game), 'bg-danger': !isWin(game) }">
            <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                alt="..."
                class="img-thumbnail rounded float-end"
                style="width: 50px; height: 50px; object-fit: cover;">
            </td>
            <td :class="{ 'bg-success': isWin(game), 'bg-danger': !isWin(game) }"
                class="align-middle text-start">
                {{ game.opponent }}
            </td>
            <td :class="{ 'bg-success': isWin(game), 'bg-danger': !isWin(game) }"
                class="align-middle text-end">
                {{ game.player1_id !== props.id
                ? game.player1_score + ' : ' + game.player2_score
                : game.player2_score + ' : ' + game.player1_score}}
            </td>
        </tr>
        </tbody>
    </table>
    </div>   
</template>