<script setup>
import Map from '../components/game/GameMap.vue';
import Paddle from '../components/game/GamePaddle.vue';
import BallandScores from '../components/game/GameBallandScores.vue';
import Scores from '../components/game/GameScores.vue';
import { ref } from 'vue';

  const mapWidth = 624;
  const mapHeight = 351;
  const isOver = ref(false);
  let draw = ref(null);
  let paddle1 = ref(null);
  let paddle2 = ref(null);
  let score = ref(null);

  const handleDrawUpdate = (updatedDraw) => {
    draw.value = updatedDraw;
    console.log("Draw in handle it: " + draw.value);
  };
</script>

<template>
  <div>
  <Map @update:draw="handleDrawUpdate" :width="mapWidth" :height="mapHeight" />
  <Paddle ref="paddle1" :draw="draw" :mapWidth="mapWidth" :mapHeight="mapHeight" :paddleX="26" keyUp="w" keyDown="s"/>
  <Paddle ref="paddle2" :draw="draw" :mapWidth="mapWidth" :mapHeight="mapHeight" :paddleX="mapWidth - 48" keyUp="ArrowUp" keyDown="ArrowDown"/>
  <BallandScores :draw="draw" :width="mapWidth" :height="mapHeight" :paddle1="paddle1" :paddle2="paddle2" />
  </div>
</template>

<style scoped>
</style>