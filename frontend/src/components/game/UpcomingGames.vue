<template>
<div v-if="isLoggedIn" class="dropdown text-end">
    <button type="button" 
        class="btn btn-outline-dark px-2"
        data-bs-toggle="dropdown"
        aria-expanded="false"
        @click="toggleDropdown"
    >
    upcoming Games
    <span v-if="upcomingGames.length > 0 && dropdownShown > 0"
        class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger text-light">
        {{dropdownShown}}<span class="visually-hidden">unread messages</span>
    </span>
    </button>
    <table class="dropdown-menu table-bordered p-0" @click="toggleDropdown">
      <thead class="">
        <tr>
          <th class="px-3">Opponent</th>
          <th class="px-3">Tournament</th>
          <th class="px-3">Time</th>
        </tr>
      </thead>
      <tbody v-if="upcomingGames.length > 0">
        <tr v-for="(game, index) in upcomingGames.slice().reverse()" :key="index">
          <td class="align-middle px-2 text-start">
            <UserRow :bgColor="''" :user="game.player1.id === user.id ? game.player2 : game.player1"/>
          </td>
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
</template>

<script setup>
import Backend from "../../js/Backend"
import { ref } from 'vue'
import { watch, onMounted } from "vue"
import UserRow from "../common/UserRow.vue"

let dropdownShown = ref(0);
const isLoggedIn = ref(false);
const user = ref({});
const upcomingGames = ref([]);

onMounted(() => {
  fetchData();
})

const fetchData = async () => {
  try {
    user.value = await Backend.get('/api/users/me');
    isLoggedIn.value = true;
    console.log(user.value);
    upcomingGames.value = await Backend.get(`api/users/${user.value.id}/games_upcoming`);
    console.log(upcomingGames.value);
  } catch (err) {
    console.error(err.message);
    user.value = {};
    // alert(err.message);
  }
};

watch(() => upcomingGames.value, () => {
  dropdownShown.value++;
});

function toggleDropdown() {
  dropdownShown.value = 0;
}

</script>

<style scoped>

.dropdown-menu {
  max-height: 249px;
  overflow-y: auto;
}

</style>
