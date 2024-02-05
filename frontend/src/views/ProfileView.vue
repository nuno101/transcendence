<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import WinsTable from '../components/dashboard/WinsTable.vue';
import DefeatsTable from '../components/dashboard/DefeatsTable.vue';
import CommonTable from '../components/dashboard/CommonTable.vue';
import { ref, onMounted, watch} from 'vue';

// GENERAL
const defeats = ref(null);
const wins = ref(null);
const total = ref(null);
const defeatsRatio = ref(null);
const winsRatio = ref(null);

// INDIVIDUAL
const username = ref('');
const users = ref({});
const userStats = ref({});

onMounted(() => {
  fetchData();
})

const isLoading = ref(true);

const fetchData = async () => {
  try {
    users.value = await Backend.get('/api/users/me');
    if(users.value) {
      username.value = users.value.username;
      userStats.value = await Backend.get(`/api/users/${users.value.id}/stats`);
      initValues(userStats.value);
    }
  } catch (err) {
    console.error(err.message);
  } finally {
    isLoading.value = false; //data available
  }
};

const initValues = (userStats) => {
  defeats.value = userStats.losses;
  wins.value = userStats.wins;
  total.value = userStats.losses + userStats.wins;
  defeatsRatio.value = (userStats.losses / total.value) * 100;
  winsRatio.value = (userStats.wins / total.value) * 100;
};
</script>

<template>
    <div class="cont">
      <div class="box">
        <div class="con mt-5">
            <div class="row">
              <div class="col-6">
                <div class="bg-danger rounded-pill">
                  <div class="ms-4 p-2 ps-0 text-white d-flex justify-content-between">
                    <div class="p-0">Defeats</div>
                    <div class="text-end pe-5">{{ defeats }}</div>
                  </div>
                </div>
              </div>
              <div class="col-6"> 
                <div class="bg-success rounded-pill">
                <div class="me-4 p-2 pe-0 text-white d-flex justify-content-between">
                  <div class="ps-5">{{ wins }}</div>
                  <div class="text-end">Wins</div>
                </div>
              </div>
            </div>
          </div>
          <div class="avatar-circle position-absolute start-50 translate-middle">
            <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
              alt="..."
              class="img-thumbnail rounded float-start"
              style="width: 100px; height: 100px; object-fit: cover;">
          </div>
          <div class="text-center">
            <div class="name bg-primary pe-4 ps-4 pt-3 pb-1 text-white d-inline-block rounded-bottom text-uppercase">{{ username }}</div>
          </div>
        <div class="row mt-4">
            <DefeatsTable v-if="!isLoading" :id="users.id"/>
              <div class="col-md-2 d-none d-md-block">
                <div class="bar-chart rounded">
                  <div class="bar defeat-bar rounded" :style="{height: `${defeatsRatio}%`}"></div>
                  <div class="bar wins-bar rounded" :style="{height: `${winsRatio}%`}"></div>
                </div>
              </div>
            <WinsTable v-if="!isLoading" :id="users.id"/>
            <CommonTable v-if="!isLoading" :id="users.id"/>
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
