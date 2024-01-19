<script setup>
import Map from '../components/game/GameMap.vue';
import Paddle from '../components/game/GamePaddle.vue';
import BallandScores from '../components/game/GameBallandScores.vue';
// import Scores from '../components/game/OLDGameScores.vue';
import { ref, watch, onMounted, reactive } from 'vue';

  const mapWidth = 624;
  const mapHeight = 351;
  const isOver = ref(false);
  let canvas = ref(null);
  let context = ref(null);
let paddle1 = reactive({
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

  let score = ref(null);

  const handleCanvasUpdate = (updateCanvas) => {
    canvas.value = updateCanvas;
    context.value = canvas.value.getContext('2d');
    console.log("canvas in handle it: " + canvas.value);
    console.log("paddle in parent: " + paddle1.value?.y);
  };
watch([canvas, context], () => {
  initializePaddles();
});

onMounted(() => {
  initializePaddles();
});

const initializePaddles = () => {
  // Now you can access canvas and context, and initialize paddle1 and paddle2
  paddle1.x = 26;
  paddle1.y = mapHeight / 2;
  paddle1.width = 0;
  paddle1.height = 0;
  paddle1.color = '#00ff99';

  paddle2.x = mapWidth - 48;
  paddle2.y = mapHeight / 2;
  paddle2.width = 0;
  paddle2.height = 0;
  paddle2.color = '#00ff99';
  console.log("Paddle1 Y: " + paddle1.y);
  console.log("Paddle2 Y: " + paddle2.y);
};

</script>

<template>
  <div>
  <Map @update:canvas="handleCanvasUpdate" :width="mapWidth" :height="mapHeight" />
  <Paddle ref="paddle1" :canvas="canvas" :context="context" :mapWidth="mapWidth" :mapHeight="mapHeight" :paddleX="26" keyUp="w" keyDown="s" />
  <Paddle ref="paddle2" :canvas="canvas" :context="context" :mapWidth="mapWidth" :mapHeight="mapHeight" :paddleX="mapWidth - 48" keyUp="ArrowUp" keyDown="ArrowDown" />
  <BallandScores :canvas="canvas" :width="mapWidth" :height="mapHeight" :paddle1="$refs.paddle1?.paddle" :paddle2="$refs.paddle2?.paddle" />
  <div>
      Paddle Y: {{ $refs.paddle1?.paddle?.y }}
      Paddle Y: {{ paddle1.y }}
    </div>
  </div>
</template>

<style scoped>
</style>
