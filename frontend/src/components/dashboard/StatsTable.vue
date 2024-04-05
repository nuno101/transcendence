<script setup>
import { useI18n } from 'vue-i18n';
import { defineProps, computed, onMounted, watch } from 'vue';
import UserRow from '../common/UserRow.vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'


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
  return props.flag === 'GAMES' ? 'd-lg-none' : 'd-none d-lg-block';
});

const avatarBootstrap = computed(() => {
  return (game) => {
    if (props.flag === 'GAMES')
      return `${bgColor.value(game)}`;
    return `d-none d-lg-table-cell ${bgColor.value(game)}`;
  };
});


const initializeTooltips = () => {
  for (const game of filteredGames.value) {
    if (game.tournament !== null) {
      new bootstrap.Tooltip(`#${props.flag + game.id}`);
    }
  }
};

onMounted(() => {
  initializeTooltips();
});

watch(filteredGames, () => {
  initializeTooltips();
});
</script>

<template>
    <div class="gamestable col-lg-5 rounded img-thumbnail" :class="tablePosition">
    <table class="table">
        <tbody v-if="filteredGames.length > 0">
        <tr  v-for="game in filteredGames" :key="game">
            <td class="align-middle text-start" :class="bgColor(game)" >{{ game.updated_at.slice(0, 10)}}</td>
            <UserRow
              :user="game.player1.id !== props.id ? game.player1 : game.player2"
              :bgColor="bgColor(game)"
              :avatarStyle="avatarBootstrap(game)"
              linkColor="link-dark link-opacity-50-hover link-underline-opacity-50-hover"/>
            <td class="align-middle" :class="bgColor(game)">
              <i v-if="game.tournament != null" 
                class="bi bi-trophy"
                :title="game.tournament.title"
                :id="props.flag + game.id"
                data-bs-placement="top"
                data-toggle="tooltip"
                style="z-index: 2;"
              ></i>
            </td>
            <td class="align-middle text-end" :class="bgColor(game)">
                {{ game.player1.id !== props.id
                ? game.player1_score + ' : ' + game.player2_score
                : game.player2_score + ' : ' + game.player1_score}}
            </td>
        </tr>
        </tbody>
        <tbody v-else class="text-center">
          {{ props.flag === "WINS" ? useI18n().t('userstats.noWins')
            : props.flag === "DEFEATS" ? useI18n().t('userstats.noDefeats')
            : useI18n().t('userstats.noGames')}}
        </tbody>
    </table>
    </div>   
</template>

<style scoped>
</style>