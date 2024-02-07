<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../../js/Backend';
import { ref, defineProps, onMounted } from 'vue';

const props = defineProps(['games', 'id']);

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
                {{ game.player1.id === props.id ? game.player2.nickname : game.player1.nickname }}
            </td>
            <td :class="{ 'bg-success': isWin(game), 'bg-danger': !isWin(game) }"
                class="align-middle text-end">
                {{ game.player1.id !== props.id
                ? game.player1_score + ' : ' + game.player2_score
                : game.player2_score + ' : ' + game.player1_score}}
            </td>
        </tr>
        </tbody>
    </table>
    </div>   
</template>