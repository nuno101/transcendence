<script setup>
import Map from '../components/game/GameMap.vue';
import Paddle from '../components/game/GamePaddle.vue';
import BallandScores from '../components/game/GameBallandScores.vue';
// import Scores from '../components/game/OLDGameScores.vue';
import { ref } from 'vue';

  const mapWidth = 624;
  const mapHeight = 351;
  const isOver = ref(false);
  let canvas = ref(null);
  let context = ref(null);
  let paddle1 = ref(null);
  let paddle2 = ref(null);
  let score = ref(null);

  const handleCanvasUpdate = (updateCanvas) => {
    canvas.value = updateCanvas;
    context.value = canvas.value.getContext('2d');
    console.log("canvas in handle it: " + canvas.value);
  };
</script>

<template>
  <div>
  <Map @update:canvas="handleCanvasUpdate" :width="mapWidth" :height="mapHeight" />
  <Paddle ref="paddle1" :canvas="canvas" :context="context" :mapWidth="mapWidth" :mapHeight="mapHeight" :paddleX="26" keyUp="w" keyDown="s"/>
  <Paddle ref="paddle2" :canvas="canvas" :context="context" :mapWidth="mapWidth" :mapHeight="mapHeight" :paddleX="mapWidth - 48" keyUp="ArrowUp" keyDown="ArrowDown"/>
  <!-- <Paddle ref="paddle2" :canvas="canvas" :mapWidth="mapWidth" :mapHeight="mapHeight" :paddleX="mapWidth - 48" keyUp="ArrowUp" keyDown="ArrowDown"/> -->
  <!-- <BallandScores :canvas="canvas" :width="mapWidth" :height="mapHeight" :paddle1="paddle1" :paddle2="paddle2" /> -->
  </div>
</template>

<style scoped>
</style>