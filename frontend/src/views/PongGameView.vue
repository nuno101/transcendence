<script setup>
import Map from '../components/game/GameMap.vue';
import Paddle from '../components/game/GamePaddle.vue';
import Ball from '../components/game/GameBall.vue';
import { ref, toRefs } from 'vue';

  const mapWidth = 624;
  const mapHeight = 351;
  let draw = ref(null);
  let paddle1 = ref(null);
  let paddle2 = ref(null);

  const handleDrawUpdate = (updatedDraw) => {
    draw.value = updatedDraw;
    console.log("Draw in handle it: " + draw.value);
  };

  // const paddles = toRefs({ paddle1, paddle2 });
</script>

<template>
  <div>
  <!-- <h1> WIDTH {{ width}} </h1> -->
  <Map @update:draw="handleDrawUpdate" :width="mapWidth" :height="mapHeight" />
  <Paddle ref="paddle1" :draw="draw" :mapWidth="mapWidth" :mapHeight="mapHeight" :paddleX="26" keyUp="w" keyDown="s"/>
  <Paddle ref="paddle2" :draw="draw" :mapWidth="mapWidth" :mapHeight="mapHeight" :paddleX="mapWidth - 48" keyUp="ArrowUp" keyDown="ArrowDown"/>
  <Ball :draw="draw" :width="mapWidth" :height="mapHeight" :paddle1="paddle1" :paddle2="paddle2" />
  </div>
</template>

<style scoped>
</style>