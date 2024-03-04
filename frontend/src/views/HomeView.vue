<script setup>
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
    <UpcomingGames />
    <div class="d-flex justify-content-center align-items-center" style="margin-top: 120px;">
      <div class="text-center">
        <h1 class="m-0 p-0">PONG GAME</h1>
        <h5>Our Transcendence Project</h5>
        <p>Transcendence is the last project of the Core Curriculum at 42. 
          The goal of this project is to develop a web application that allows users to engage in a basic Pong Game 
          while also providing a platform for social interaction with other users. 
          It involves implementing various modules, making choices about technologies and libraries, 
          and ensuring that all decisions align with the project's requirements and limitations.
        </p>
      </div>
    </div>
  <footer class="container-fluid bg-light fixed-bottom p-3 text-center" style="z-index: -1;">
      <h6 class="text-uppercase fw-bold pb-1">Connect with us on Github</h6>
      <div class="d-flex flex-wrap justify-content-center">
        <p class="mx-md-4 mx-2" v-for="(link, index) in profileLinks" :key="index">
          <i class="bi bi-github"></i> <a class="link-opacity-50-hover" :href="link.link">{{ link.name }}</a>
        </p>
      </div>
    <div>
      <i class="bi bi-github"></i> <a class="link-opacity-50-hover" href="https://github.com/nuno101/transcendence">Our Transcendence Project</a>
    </div>
  </footer>
  </div>
</template>

<style></style>