<script setup>

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
  <main>
    <h1>HOME VIEW</h1>
    <h1>WELCOME TO OUR TRANSCENDENCE PROJECT</h1>
  </main>
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