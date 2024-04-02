<script setup>
import { useI18n } from 'vue-i18n';
import UpcomingGames from '../components/game/UpcomingGames.vue';

const profileLinks = [
  { link: 'https://github.com/Anoukmch', name: 'amechain' },
  { link: 'https://github.com/jharrach', name: 'jharrach' },
  { link: 'https://github.com/jmatheis00', name: 'jmatheis' },
  { link: 'https://github.com/nuno101', name: 'nlouro' },
  { link: 'https://github.com/PythonGermany', name: 'rburgsta' }
]

</script>

<template>
  <div>
    <UpcomingGames/>
    <div class="d-flex justify-content-center align-items-center mt-3">
      <div class="text-center">
        <h1 class="m-0 p-0">PONG GAME</h1>
        <h5>{{useI18n().t('home.ourTranscendenceProject')}}</h5>
        <p>{{useI18n().t('home.transcendenceDescription')}}</p>
      </div>
    </div>
  <footer class="container-fluid bg-light fixed-bottom p-3 text-center" style="z-index: 1;">
      <h6 class="text-uppercase fw-bold pb-1">{{useI18n().t('home.connectOnGithub')}}</h6>
      <div class="d-flex flex-wrap justify-content-center">
        <p class="mx-md-4 mx-2" v-for="(link, index) in profileLinks" :key="index">
          <i class="bi bi-github"></i> <a class="link-opacity-50-hover" :href="link.link">{{ link.name }}</a>
        </p>
      </div>
    <div>
      <i class="bi bi-github"></i> <a class="link-opacity-50-hover" href="https://github.com/nuno101/transcendence">{{useI18n().t('home.ourTranscendenceProject')}}</a>
    </div>
  </footer>
  </div>
</template>

<style></style>