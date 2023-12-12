<script setup>
import PongGame from '../components/game/PongGame.vue';

const { scoreLeft, scoreRight } = PongGame;
</script>

<template>
<div>
    <p>Player Left: {{ scoreLeft }}</p>
    <p>Player Right: {{ scoreRight }}</p>
  </div>
  <PongGame>
    <!-- <div v-if="scoreLeft >= 2 || scoreRight >= 2">
    <h2>Game Over!</h2>
    <p v-if="scoreLeft >= 2">Player Left Wins!</p>
    <p v-else>Player Right Wins!</p>
    </div> -->
  </PongGame>
</template>

<style scoped>
</style>