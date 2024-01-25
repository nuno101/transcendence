<script setup>
// import HomeSelection from '../components/dashboard/DashboardChoice.vue';
import { useI18n } from 'vue-i18n';
</script>

<template>
  <div class="home">
    <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
    <div class="cont">
      <div class="box">
        <div class="con mt-4">
          <div class="curved-bg bg-primary p-1">
            <div class="row">
              <div class="col-md-4">
                <div class="ms-4 bg-danger p-1 text-white d-flex justify-content-between">
                  <div>Defeat</div>
                  <div class="text-end">123</div>
                </div>
              </div>
              <div class="col-md-4 text-center">
                <!-- Place your avatar circle here -->
                <div class="avatar-circle">Avatar</div>
              </div>
              <div class="col-md-4"> 
                <div class="me-4 bg-success p-1 text-white d-flex justify-content-between">
                  <div>222</div>
                  <div class="text-end">Wins</div>
                </div>
              </div>
            </div>
          </div>
          <!-- UNDER BALKEN -->
        <div class="row mt-4">
              <div class="gamestable col-md-5">
                <table class="table">
                  <tbody >
                    <tr v-for="row in 4" :key="row">
                      <td class="bg-danger d-none d-lg-table-cell">
                        <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                          alt="..."
                          class="img-thumbnail rounded float-start"
                          style="width: 50px; height: 50px; object-fit: cover;">
                      </td>
                      <td class="bg-danger align-middle">opponent</td>
                      <td class="bg-danger align-middle">20.01.24</td>
                      <td class="bg-danger align-middle">5 : 1</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="col-md-2">
                <!-- Place your bar chart here -->
                <div class="bar-chart">
                  <div class="bar defeat-bar" style="height: 50%;"></div>
                  <div class="bar wins-bar" style="height: 75%;"></div>
                </div>
              </div>
              <div class="gamestable col-md-5 ">
                <table class="table ">
                  <tbody>
                    <tr v-for="row in 8" :key="row">
                      <td class="bg-success align-middle">5 : 1</td>
                      <td class="bg-success align-middle">20.01.24</td>
                      <td class="bg-success align-middle">opponent</td>
                      <td class="bg-success d-none d-lg-table-cell">
                        <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                          alt="..."
                          class="img-thumbnail rounded float-start"
                          style="width: 50px; height: 50px; object-fit: cover;">
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<style>
.cont {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  margin-top: 50px;
  height: 100vh;
}

.box {
  box-sizing: border-box;
  margin: 0;
  width: 80%;
  padding: 10px 20px;
  background-color: white;
}

.curved-bg {
  background: #007bff;
  clip-path: polygon(5% 0%, 100% 0%, 95% 100%, 0% 100%);
}

.bar-chart {
  display: flex;
  justify-content: center;
  align-items: end;
  background-color: #f0f0f0; /* Example background color for the chart area */
  height: 270px; /*Adjust the height as needed */
  /* margin: 10px 0; Add margin for spacing */
}

.bar {
  width: 50px; /* Adjust the width of each bar */
  border: 1px solid #fff; /* Add a border for better visibility */
}
.defeat-bar {
  background-color: red; /* Color for the Defeat bar */
}

.wins-bar {
  background-color: green; /* Color for the Wins bar */
}

.gamestable {
  max-height: 270px;
  overflow-y: scroll;
  padding: 0;
}

@media (max-width: 991.98px) {
  .gamestable {
    height: 164px;
  }
  .bar-chart {
    height: 164px;
  }
}
</style>
