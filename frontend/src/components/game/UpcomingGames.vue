<template>
<div v-if="globalUser" class="boxstyling">
<div class="box rounded">
  <Loading v-if="!isLoaded" />
  <h6 class="text-center fw-bold text-uppercase">{{useI18n().t('upcomingGames.upcomingGames')}}</h6>
  <div class="text-center gamestable rounded img-thumbnail">
  <table class="table m-0 table-hover">
    <thead>
      <tr>
        <th colspan="2" class="px-3">{{useI18n().t('upcomingGames.opponent')}}</th>
        <th class="d-none d-lg-table-cell">{{useI18n().t('usersview.created_at')}}</th>
        <th class="d-none d-lg-table-cell">{{useI18n().t('usersview.updated_at')}}</th>
        <th class="px-3">{{useI18n().t('upcomingGames.tournament')}}</th>
        <th></th>
      </tr>
    </thead>
    <tbody v-if="upcomingGames.length > 0">
      <tr v-for="(game, index) in upcomingGames.slice().reverse()" :key="index" class="align-middle">
        <UserRow :bgColor="''" :user="game.player1.id === globalUser.id ? game.player2 : game.player1"/>
        <td class="d-none d-lg-table-cell">{{ game.created_at }}</td>
        <td class="d-none d-lg-table-cell">{{ game.updated_at }}</td>
        <td class="px-2 text-center">
            <i v-if="game.tournament" class="bi bi-trophy"></i>&nbsp;
            <router-link v-if="game.tournament" :to="`/tournaments/${game.tournament.id}`">
              {{ game.tournament.title }}
            </router-link>
        </td>
        <td v-if="!game.tournament || game.tournament.status === 'ongoing'" class="align-middle px-2 text-center">
          <router-link :to="`/ponggame/${game.id}`">
            <button type="button" class="btn py-1 btn-outline-primary">{{useI18n().t('upcomingGames.play')}}</button></router-link>
        </td>
      </tr>
    </tbody>
    <tbody v-else><tr><td class="text-center" colspan="6">{{useI18n().t('upcomingGames.noUpcomingGames')}}</td></tr></tbody>
  </table>
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
th {
  position: sticky;
  top: 0;
  z-index: 1;

}

.gamestable {
  padding: 0;
  margin: auto;
  overflow-y: auto;
  height: calc(100vh - (var(--header-height) + var(--footer-height) + 170px));
}

@media screen and (max-height: 540px) {
  .gamestable {
    height: max(calc(100vh - (var(--header-height) + var(--footer-height))), 160px);
  }
}
</style>
