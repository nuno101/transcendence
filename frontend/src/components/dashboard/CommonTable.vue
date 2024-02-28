<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../../js/Backend';
import { defineProps, watch, onMounted, ref} from 'vue';
import Avatar from '../../js/Avatar';
import Loading from '../common/Loading.vue';

const props = defineProps(['games', 'id']);
const avatars = ref({});
const isLoaded = ref(false);

watch(() => props.games, () => {
  fetchAvatars();
});

const fetchAvatars = async () => {
    try {
        for (const game of props.games) {
            const playerId = game.player1.id !== props.id ? game.player1.id : game.player2.id;
            const avatarUrl = await Avatar.getAvatarById(playerId);
            avatars.value[playerId] = avatarUrl;
        }
    } catch (error) {
      console.error(`Error fetching avatar for player:`, error.message);
    } finally {
    isLoaded.value = true;
  }
};

onMounted(fetchAvatars);

const isWin = (game) => {
  if(game.player1.id === props.id &&
    game.player1_score >= game.player2_score)
    return true;
  else if (game.player2.id === props.id &&
    game.player1_score <= game.player2_score)
    return true;
  return (false);
};
</script>

<template>
    <div class="gamestable col-md-5 rounded img-thumbnail d-md-none">
    <Loading v-if="!isLoaded"/>
    <table v-if="isLoaded" class="table">
        <tbody>
        <tr v-if="props.games.length > 0" v-for="game in games" :key="game">
            <td :class="{ 'bg-success': isWin(game), 'bg-danger': !isWin(game) }"
                class="align-middle text-start">
                {{ game.updated_at.slice(0, 10)}}
            </td>
            <td :class="{ 'bg-success': isWin(game), 'bg-danger': !isWin(game) }">
            <img :src="avatars[game.player1.id !== props.id ? game.player1.id : game.player2.id]"
                alt="..."
                class="img-thumbnail rounded float-end"
                style="width: 50px; height: 50px; object-fit: cover;">
            </td>
            <td :class="{ 'bg-success': isWin(game), 'bg-danger': !isWin(game) }"
                class="align-middle text-start">
                {{ game.player1.id === props.id ? game.player2.nickname : game.player1.nickname }}
            </td>
            <td :class="{ 'bg-success': isWin(game), 'bg-danger': !isWin(game) }"
                class="align-middle text-end">
                {{ game.player1.id !== props.id
                ? game.player1_score + ' : ' + game.player2_score
                : game.player2_score + ' : ' + game.player1_score}}
            </td>
        </tr>
        <tr v-else class="text-center">NO GAMES</tr>
        </tbody>
    </table>
    </div>   
</template>