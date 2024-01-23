<script setup>
import Map from '../components/game/GameMap.vue';
import Paddle from '../components/game/GamePaddle.vue';
import BallandScores from '../components/game/GameBallandScores.vue';
// import Scores from '../components/game/OLDGameScores.vue';
import { ref, reactive } from 'vue';

  const mapWidth = 624;
  const mapHeight = 351;
  let canvas = ref(null);
  let context = ref(null);
const paddle1 = reactive({
  x: 0,
  y: 0,
  width: 0,
  height: 0,
  color: ''
});

const paddle2 = reactive({
  x: 0,
  y: 0,
  width: 0,
  height: 0,
  color: ''
});

  const handleCanvasUpdate = (updateCanvas) => {
    canvas.value = updateCanvas;
    context.value = updateCanvas.getContext('2d');
  };
</script>

<template>
  <div>
  <Map @update:canvas="handleCanvasUpdate" :width="mapWidth" :height="mapHeight" />
  <Paddle ref="paddle1" :canvas="canvas" :context="context" :mapWidth="mapWidth" :mapHeight="mapHeight" :paddleX="10" keyUp="w" keyDown="s" />
  <Paddle ref="paddle2" :canvas="canvas" :context="context" :mapWidth="mapWidth" :mapHeight="mapHeight" :paddleX="mapWidth - 30" keyUp="ArrowUp" keyDown="ArrowDown" />
  <BallandScores :canvas="canvas" :width="mapWidth" :height="mapHeight" :paddle1="$refs.paddle1?.paddle" :paddle2="$refs.paddle2?.paddle" />
  </div>
</template>

<style scoped>
</style>
