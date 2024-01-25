<script setup>
import { useI18n } from 'vue-i18n';
import { ref} from 'vue';

const defeats = ref(123);
const wins = ref(222);

const total = defeats.value + wins.value;
const defeatsRatio = (defeats.value / total) * 100;
const winsRatio = (wins.value / total) * 100;
</script>

<template>
  <div class="home">
    <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
    <div class="cont">
      <div class="box">
        <div class="con mt-5">
          <div class="curved-bg bg-primary p-1 rounded-pill">
            <div class="row">
              <div class="col-md-4">
                <div class="ms-4 p-1 text-white d-flex justify-content-between">
                  <div>Defeats</div>
                  <div class="text-end">{{defeats}}</div>
                </div>
              </div>
              <div class="col-md-4 position-relative">
              </div>
              <div class="col-md-4"> 
                <div class="me-4 p-1 text-white d-flex justify-content-between">
                  <div>{{wins}}</div>
                  <div class="text-end">Wins</div>
                </div>
              </div>
            </div>
          </div>
          <div class="avatar-circle position-absolute start-50 translate-middle" style="top: 160px;">
            <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
              alt="..."
              class="img-thumbnail rounded float-start"
              style="width: 100px; height: 100px; object-fit: cover;">
          </div>
          <div class="text-center">
            <div class="name bg-primary text-center pe-4 ps-4 pt-3 pb-1 text-white d-inline-block rounded-bottom">NAMENAME</div>
          </div>
          <!-- UNDER BALKEN -->
        <div class="row mt-4">
              <div class="gamestable col-md-5 rounded img-thumbnail">
                <table class="table">
                  <tbody >
                    <tr v-for="row in 4" :key="row">
                      <td class="bg-danger d-none d-lg-table-cell">
                        <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                          alt="..."
                          class="img-thumbnail rounded float-start"
                          style="width: 50px; height: 50px; object-fit: cover;">
                      </td>
                      <td class="bg-danger align-middle text-start">opponent</td>
                      <td class="bg-danger align-middle text-start">20.01.24</td>
                      <td class="bg-danger align-middle text-end">5 : 1</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="col-md-2">
                <!-- Place your bar chart here -->
                <div class="bar-chart rounded">
                  <div class="bar defeat-bar rounded" :style="{height: `${defeatsRatio}%`}"></div>
                  <div class="bar wins-bar rounded" :style="{height: `${winsRatio}%`}"></div>
                </div>
              </div>
              <div class="gamestable col-md-5 rounded img-thumbnail">
                <table class="table ">
                  <tbody>
                    <tr v-for="row in 8" :key="row">
                      <td class="bg-success align-middle">5 : 1</td>
                      <td class="bg-success align-middle text-end">20.01.24</td>
                      <td class="bg-success align-middle text-end">opponent</td>
                      <td class="bg-success d-none d-lg-table-cell">
                        <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                          alt="..."
                          class="img-thumbnail rounded float-end"
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
  position: relative;
  background: #007bff;
  /* clip-path: polygon(5% 0%, 100% 0%, 95% 100%, 0% 100%); */
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

/* .avatar-circle {
  background-color: black;
  position: absolute;
  top: 0;
  margin-top: 90px;
  margin-left: 20px;
  z-index: 5;
} */

.name {

}

</style>
