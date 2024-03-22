<template>
<div v-if="globalUser" class="boxstyling">
<div class="box rounded">
<div class="table-wrapper text-center">
  <Loading v-if="!isLoaded" />
  <h6 class="fw-bold text-uppercase">{{useI18n().t('upcomingGames.upcomingGames')}}</h6>
  <div class="gamestable rounded img-thumbnail d-flex justify-content-center">
  <table class="table m-0 table-hover">
    <thead>
      <tr>
        <th colspan="2" class="px-3">{{useI18n().t('upcomingGames.opponent')}}</th>
        <th class="px-3">{{useI18n().t('upcomingGames.tournament')}}</th>
      </tr>
    </thead>
    <tbody v-if="upcomingGames.length > 0">
      <tr v-for="(game, index) in upcomingGames.slice().reverse()" :key="index">
          <UserRow :bgColor="''" :user="game.player1.id === globalUser.id ? game.player2 : game.player1"/>
        <td class="align-middle px-2 text-center">
            <router-link v-if="game.tournament" :to="`/tournaments/${game.tournament.id}`">
              {{ game.tournament.title }}
            </router-link>
        </td>
      </tr>
    </tbody>
    <tbody v-else><tr><td class="text-center" colspan="3">{{useI18n().t('upcomingGames.noUpcomingGames')}}</td></tr></tbody>
  </table>
  </div>
</div>
</div>
</div>
</template>

<script setup>
import { useI18n } from 'vue-i18n';
import Backend from "../../js/Backend"
import { ref } from 'vue'
import { watch, onMounted } from "vue"
import UserRow from "../common/UserRow.vue"
import { globalUser } from "../../main"
import Loading from "../common/Loading.vue"

const upcomingGames = ref([]);
const isLoaded = ref(false);

onMounted(() => {
  fetchData();
})

const fetchData = async () => {
  try {
    if(globalUser.value)
      upcomingGames.value = await Backend.get(`/api/users/${globalUser.value.id}/games_upcoming`);
  } catch (err) {
    console.error(err.message);
  } finally {
    isLoaded.value = true;
  }
};

watch(() => globalUser.value, () => {
  fetchData();
});
</script>

<style scoped>
@import url('@/assets/colors.css');
th {
  position: sticky;
  top: 0;
  z-index: 1;

}

.gamestable {
  max-height: 240px;
  max-width: 400px;
  margin: auto;
  overflow-y: scroll;
  padding: 0;
}

thead {
  --bs-table-bg: var(--COLOR1);
  --bs-table-color: white;
}

tbody {
  box-shadow: inset 0 0 0 9999px var(--bs-table-accent-bg);

}
</style>
