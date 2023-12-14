<script setup>
import Map from '../components/game/GameMap.vue';
import Paddle from '../components/game/GamePaddle.vue';
import { ref } from 'vue';

  const width = 624;
  const height = 351;
  let draw = ref(null);

  const handleDrawUpdate = (updatedDraw) => {
    draw.value = updatedDraw;
    console.log("Draw in handle it: " + draw.value);
  };
</script>

<template>
  <div>
  <!-- <h1> WIDTH {{ width}} </h1> -->
  <Map @update:draw="handleDrawUpdate" :width="width" :height="height" />
  <Paddle :draw="draw" :width="width" :height="height" :paddleX="26" keyUp="w" keyDown="s"/>
  <Paddle :draw="draw" :width="width" :height="height" :paddleX="width - 48" keyUp="ArrowUp" keyDown="ArrowDown"/>
  </div>
</template>

<style scoped>
</style>