<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import Helpers from '../js/Helpers';
import WinsTable from '../components/dashboard/WinsTable.vue';
import DefeatsTable from '../components/dashboard/DefeatsTable.vue';
import CommonTable from '../components/dashboard/CommonTable.vue';
import Loading from '../components/common/Loading.vue';
import { ref, onMounted, computed} from 'vue';

// GENERAL
const total = ref(null);
const defeatsRatio = ref(null);
const winsRatio = ref(null);

// INDIVIDUAL
const users = ref({});
const games = ref ([]);
const avatar = ref(null);

const isLoaded = ref(false);

onMounted(() => {
  fetchData();
})

const fetchData = async () => {
  try {
    users.value = await Backend.get('/api/users/me');
    if(users.value) {
      games.value = await Backend.get(`/api/users/${users.value.id}/games`);
      avatar.value = await Helpers.getAvatarById(users.value.id);
      total.value = DefeatGames.value.length + WinGames.value.length;
      defeatsRatio.value = (DefeatGames.value.length / total.value) * 100;
      winsRatio.value = (WinGames.value.length / total.value) * 100;
    }
  } catch (err) {
    console.error(err.message);
  } finally {
    isLoaded.value = true; //data available
  }
};

const isWin = (game) => {
  if(game.player1.id === users.value.id &&
    game.player1_score >= game.player2_score)
    return true;
  else if (game.player2.id === users.value.id &&
    game.player1_score <= game.player2_score)
    return true;
  return (false);
};

const WinGames = computed(() => {
    return games.value.filter(game => isWin(game));
});

const DefeatGames = computed(() => {
    return games.value.filter(game => !isWin(game));
});
</script>

<template>
    <div class="cont">
      <Loading v-if="!isLoaded"/>
      <div v-if="isLoaded" class="box">
        <div class="con mt-5">
            <div class="row">
              <div class="col-6">
                <div class="bg-danger rounded-pill">
                  <div class="ms-4 p-2 ps-0 text-white d-flex justify-content-between">
                    <div class="p-0">Defeats</div>
                    <div class="text-end pe-5">{{ DefeatGames.length }}</div>
                  </div>
                </div>
              </div>
              <div class="col-6"> 
                <div class="bg-success rounded-pill">
                <div class="me-4 p-2 pe-0 text-white d-flex justify-content-between">
                  <div class="ps-5">{{ WinGames.length }}</div>
                  <div class="text-end">Wins</div>
                </div>
              </div>
            </div>
          </div>
          <div class="avatar-circle position-absolute start-50 translate-middle">
            <img :src="avatar"
              alt="..."
              class="img-thumbnail rounded float-start"
              style="width: 100px; height: 100px; object-fit: cover;">
          </div>
          <div class="text-center">
            <div class="name bg-primary pe-4 ps-4 pt-3 pb-1 text-white d-inline-block rounded-bottom text-uppercase">{{ users.nickname }}</div>
          </div>
        <div class="row mt-4">
            <DefeatsTable :id="users.id" :games="DefeatGames"/>
              <div class="col-md-2 d-none d-md-block">
                <div class="bar-chart rounded">
                  <div class="bar defeat-bar rounded" :style="{height: `${defeatsRatio}%`}"></div>
                  <div class="bar wins-bar rounded" :style="{height: `${winsRatio}%`}"></div>
                </div>
              </div>
            <WinsTable :id="users.id" :games="WinGames"/>
            <CommonTable :id="users.id" :games="games"/>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

.cont {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  margin-top: 50px;
  height: 100vh;
  width: 100%;
}

.box {
  box-sizing: border-box;
  margin: 0;
  width: 80%;
  padding: 10px 20px;
  padding-bottom: 20px;
  background-color: white;
}

.curved-bg {
  position: relative;
  background: #007bff;
}

.bar-chart {
  display: flex;
  justify-content: center;
  align-items: end;
  background-color: #f0f0f0;
  height: 270px;
}

.bar {
  width: 50px;
  border: 1px solid #fff;
}
.defeat-bar {
  background-color: red;
}

.wins-bar {
  background-color: green;
}

.gamestable {
  max-height: 270px;
  overflow-y: scroll;
  padding: 0;
}

.avatar-circle {
  top: 210px;
}

@media (max-width: 991.98px) {
  .gamestable, .bar-chart {
    height: 164px;
  }
  .avatar-circle {
    top: 245px;
  }
}

@media (max-width: 768px) {
  .gamestable, .bar-chart {
    height: 280px;
  }
  .avatar-circle {
    top: 255px;
  }
}
</style>
