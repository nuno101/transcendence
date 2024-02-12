<script setup>
import { useI18n } from 'vue-i18n';
import { defineProps } from 'vue';

const props = defineProps(['games', 'id']);

</script>

<template>
    <div class="gamestable col-md-5 rounded img-thumbnail d-none d-md-block">
    <table class="table">
        <tbody>
        <tr v-if="props.games.length > 0" v-for="game in props.games" :key="game">
            <td class="bg-danger align-middle text-start">{{ game.updated_at.slice(0, 10)}}</td>
            <td class="bg-danger d-none d-lg-table-cell">
            <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                alt="..."
                class="img-thumbnail rounded float-end"
                style="width: 50px; height: 50px; object-fit: cover;">
            </td>
            <td class="bg-danger align-middle text-start">
              {{ game.player1.id === props.id ? game.player2.nickname : game.player1.nickname }}
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