<script setup>
import { useI18n } from 'vue-i18n';
import { defineProps, watch, ref, onMounted } from 'vue';
import Loading from '../common/Loading.vue';
import GetAvatar from '../common/GetAvatar.vue';

const props = defineProps(['games', 'id']);

</script>

<template>
    <div class="gamestable col-md-5 rounded img-thumbnail d-none d-md-block">
    <table class="table">
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
              <GetAvatar :id="game.player1.id !== props.id ? game.player1.id : game.player2.id" />
            </td>
            <td class="bg-success align-middle text-end">{{ game.updated_at.slice(0, 10)}}</td>
        </tr>
        <tr v-else class="text-center">NO WINS</tr>
        </tbody>
    </table>
    </div>   
</template>