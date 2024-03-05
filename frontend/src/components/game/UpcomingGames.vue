<template>
<div v-if="globalUser" class="table-wrapper text-center">
  <h6>Upcoming Games</h6>
  <div class="gamestable tablesize rounded img-thumbnail d-flex justify-content-center">
  <table class="table m-0">
    <thead class="table-dark">
      <tr>
        <th colspan="2" class="px-3">Opponent</th>
        <th class="px-3">Tournament</th>
        <th class="px-3">Time</th>
      </tr>
    </thead>
    <tbody v-if="upcomingGames.length > 0">
      <tr v-for="(game, index) in upcomingGames.slice().reverse()" :key="index">
          <UserRow :bgColor="''" :user="game.player1.id === globalUser.id ? game.player2 : game.player1"/>
        <td class="align-middle px-2 text-center">
          {{ game.tournament ? game.tournament.title : 'x'}}
        </td>
        <td class="align-middle px-2 text-center">
          ? start time ?
        </td>
      </tr>
    </tbody>
    <tbody v-else class="text-center">no upcoming games</tbody>
  </table>
  </div>
</div>
</template>

<script setup>
import Backend from "../../js/Backend"
import { ref } from 'vue'
import { watch, onMounted } from "vue"
import UserRow from "../common/UserRow.vue"
import { globalUser } from "../../main"

const upcomingGames = ref([]);

onMounted(() => {
  fetchData();
})

const fetchData = async () => {
  try {
    if(globalUser.value)
      upcomingGames.value = await Backend.get(`api/users/${globalUser.value.id}/games_upcoming`);
    console.log(upcomingGames.value);
  } catch (err) {
    console.error(err.message);
  }
};

watch(() => globalUser.value, () => {
  fetchData();
});

</script>

<style scoped>

th {
  position: sticky;
  top: 0;
  z-index: 1;
}

.tablesize {
  height: 171px;
  max-width: 600px;
  margin: auto;
}

 .gamestable {
  overflow-y: scroll;
  padding: 0;
}
</style>
