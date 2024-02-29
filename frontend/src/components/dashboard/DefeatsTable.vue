<script setup>
import { useI18n } from 'vue-i18n';
import { defineProps, onMounted, watch, ref} from 'vue';
import Avatar from '../../js/Avatar';
import Loading from '../common/Loading.vue';
import GetAvatar from '../common/GetAvatar.vue';

const props = defineProps(['games', 'id']);

</script>

<template>
    <div class="gamestable col-md-5 rounded img-thumbnail d-none d-md-block">
    <table class="table">
        <tbody>
        <tr v-if="props.games.length > 0" v-for="game in props.games" :key="game">
            <td class="bg-danger align-middle text-start">{{ game.updated_at.slice(0, 10)}}</td>
            <td class="bg-danger d-none d-lg-table-cell">
              <GetAvatar class="float-end" :id="game.player1.id !== props.id ? game.player1.id : game.player2.id" />
            </td>
            <td class="bg-danger align-middle text-start">
              {{ game.player1.id !== props.id ? game.player1.nickname : game.player2.nickname }}
            </td>
            <td class="bg-danger align-middle text-end">
                {{ game.player1.id !== props.id
                ? game.player1_score + ' : ' + game.player2_score
                : game.player2_score + ' : ' + game.player1_score}}
            </td>
        </tr>
        <tr v-else class="text-center">NO DEFEATS</tr>
        </tbody>
    </table>
    </div>   
</template>