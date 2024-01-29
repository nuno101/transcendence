<script setup>
import { useI18n } from 'vue-i18n';
import { ref, onMounted} from 'vue';

const defeats = ref(123);
const wins = ref(222);

const total = defeats.value + wins.value;
const defeatsRatio = (defeats.value / total) * 100;
const winsRatio = (wins.value / total) * 100;

onMounted(() => {
})
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
                    <div class="text-end pe-5">{{defeats}}</div>
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
            <div class="name bg-primary pe-4 ps-4 pt-3 pb-1 text-white d-inline-block rounded-bottom">NAMENAME</div>
          </div>
        <div class="row mt-4">
              <div class="gamestable col-md-5 rounded img-thumbnail d-none d-md-block">
                <table class="table">
                  <tbody >
                    <tr v-for="row in 4" :key="row">
                      <td class="bg-danger align-middle text-start">20.01.24</td>
                      <td class="bg-danger d-none d-lg-table-cell">
                        <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                          alt="..."
                          class="img-thumbnail rounded float-end"
                          style="width: 50px; height: 50px; object-fit: cover;">
                      </td>
                      <td class="bg-danger align-middle text-start">opponent</td>
                      <td class="bg-danger align-middle text-end">5 : 1</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="col-md-2 d-none d-md-block">
                <div class="bar-chart rounded">
                  <div class="bar defeat-bar rounded" :style="{height: `${defeatsRatio}%`}"></div>
                  <div class="bar wins-bar rounded" :style="{height: `${winsRatio}%`}"></div>
                </div>
              </div>
              <div class="gamestable col-md-5 rounded img-thumbnail d-none d-md-block">
                <table class="table">
                  <tbody>
                    <tr v-for="row in 8" :key="row">
                      <td class="bg-success align-middle">5 : 1</td>
                      <td class="bg-success align-middle text-end">opponent</td>
                      <td class="bg-success d-none d-lg-table-cell">
                        <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                          alt="..."
                          class="img-thumbnail rounded float-start"
                          style="width: 50px; height: 50px; object-fit: cover;">
                      </td>
                      <td class="bg-success align-middle text-end">20.01.24</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="gamestable col-md-5 rounded img-thumbnail d-md-none">
                <table class="table">
                  <tbody >
                    <tr v-for="row in 10" :key="row">
                      <!-- IF DEFEAT IN DEFEAT COLOR IF WIN IN WIN COLOR -->
                        <td v-if="row % 2 === 0" class="bg-danger align-middle text-start">20.01.24</td>
                        <td v-if="row % 2 === 0" class="bg-danger">
                          <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                            alt="..."
                            class="img-thumbnail rounded float-end"
                            style="width: 50px; height: 50px; object-fit: cover;">
                        </td>
                        <td v-if="row % 2 === 0" class="bg-danger align-middle text-start">opponent</td>
                        <td v-if="row % 2 === 0" class="bg-danger align-middle text-end">5 : 1</td>
                        <td v-if="row % 2 !== 0" class="bg-success align-middle text-start">20.01.24</td>
                        <td v-if="row % 2 !== 0" class="bg-success">
                          <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                            alt="..."
                            class="img-thumbnail rounded float-end"
                            style="width: 50px; height: 50px; object-fit: cover;">
                        </td>
                        <td v-if="row % 2 !== 0" class="bg-success align-middle text-start">opponent</td>
                        <td v-if="row % 2 !== 0" class="bg-success align-middle text-end">1 : 5</td>
                    </tr>
                  </tbody>
                </table>
              </div>
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
