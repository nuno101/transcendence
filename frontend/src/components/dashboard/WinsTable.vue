<script setup>
import { useI18n } from 'vue-i18n';
import { defineProps, ref, onMounted } from 'vue';
import Helpers from '../../js/Helpers';
import Loading from '../common/Loading.vue';

const props = defineProps(['games', 'id']);
const avatars = ref({});
const isLoaded = ref(false);

const fetchAvatars = async () => {
    try {
        for (const game of props.games) {
            const playerId = game.player1.id !== props.id ? game.player1.id : game.player2.id;
            const avatarUrl = await Helpers.getAvatarById(playerId);
            avatars.value[playerId] = avatarUrl;
        }
    } catch (error) {
      console.error(`Error fetching avatar for player:`, error.message);
    } finally {
    isLoaded.value = true;
  }
};

onMounted(fetchAvatars);

</script>

<template>
    <div class="gamestable col-md-5 rounded img-thumbnail d-none d-md-block">
    <Loading v-if="!isLoaded"/>
    <table v-if="isLoaded" class="table">
        <tbody>
        <tr v-if="props.games.length > 0" v-for="game in props.games" :key="game">
            <td class="bg-success align-middle text-start">
                {{ game.player1.id === props.id
                ? game.player1_score + ' : ' + game.player2_score
                : game.player2_score + ' : ' + game.player1_score}}
            </td>
            <td class="bg-success align-middle text-end">
              {{ game.player1.id === props.id ? game.player2.nickname : game.player1.nickname }}
            </td>
            <td class="bg-success d-none d-lg-table-cell">
            <img :src="avatars[game.player1.id !== props.id ? game.player1.id : game.player2.id]"
                alt="..."
                class="img-thumbnail rounded float-start"
                style="width: 50px; height: 50px; object-fit: cover;">
            </td>
            <td class="bg-success align-middle text-end">{{ game.updated_at.slice(0, 10)}}</td>
        </tr>
        <tr v-else class="text-center">NO WINS</tr>
        </tbody>
    </table>
    </div>   
</template>