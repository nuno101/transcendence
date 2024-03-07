<script setup>
import { useI18n } from 'vue-i18n';
import { defineProps, computed } from 'vue';
import GetAvatar from '../common/GetAvatar.vue';

const props = defineProps(['games', 'id', 'flag']);

const isWin = (game) => {
  if(game.player1.id === props.id &&
    game.player1_score >= game.player2_score)
    return true;
  else if (game.player2.id === props.id &&
    game.player1_score <= game.player2_score)
    return true;
  return (false);
};

const filteredGames = computed(() => {
  if(props.flag === 'WINS')
    return props.games.filter(game => isWin(game));
  if(props.flag === 'DEFEATS')
    return props.games.filter(game => !isWin(game));
  return props.games;
});

const bgColor = computed(() => {
  return (game) => {
    return isWin(game) ? 'bg-success' : 'bg-danger';
  };
});

const tablePosition = computed(() => {
  return props.flag === 'GAMES' ? 'd-md-none' : 'd-none d-md-block';
});

const avatarBootstrap = computed(() => {
  return (game) => {
    if (props.flag === 'GAMES')
      return `${bgColor.value(game)}`;
    return `d-none d-lg-table-cell ${bgColor.value(game)}`;
  };
});
</script>

<template>
    <div class="gamestable col-md-5 rounded img-thumbnail" :class="tablePosition">
    <table class="table">
        <tbody v-if="filteredGames.length > 0">
        <tr  v-for="game in filteredGames" :key="game">
            <td class="align-middle text-start" :class="bgColor(game)" >{{ game.updated_at.slice(0, 10)}}</td>
            <td :class="avatarBootstrap(game)">
              <GetAvatar class="float-end" :id="game.player1.id !== props.id ? game.player1.id : game.player2.id" />
            </td>
            <td class="align-middle text-start" :class="bgColor(game)">
              {{ game.player1.id !== props.id ? game.player1.nickname : game.player2.nickname }}
            </td>
            <td class="align-middle text-end" :class="bgColor(game)">
                {{ game.player1.id !== props.id
                ? game.player1_score + ' : ' + game.player2_score
                : game.player2_score + ' : ' + game.player1_score}}
            </td>
        </tr>
        </tbody>
        <tbody v-else class="text-center">NO {{props.flag}}</tbody>
    </table>
    </div>   
</template>

<style scoped>
</style>