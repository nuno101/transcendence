<script>
import SVG from 'svg.js';
import { ref, onMounted, watch } from 'vue';

export default {
  props: {
    draw : Object,
    mapWidth : Number,
    mapHeight : Number,
    paddleX : Number,
    keyUp : String,
    keyDown : String
  },
  setup(props){
    const paddleHeight = 80;
    const paddleWidth = 20;
    const paddle = ref(null);
    const x = ref(props.paddleX);
    const y = ref(props.mapHeight / 2);
    const width = ref(16);
    const height = ref(60);

    onMounted(() => {
      initializePaddle();
      paddleMovement();
    });

    watch(() => props.draw, () => {
      initializePaddle();
      paddleMovement();
    });

    const initializePaddle = () => {
      if (props.draw) {
        paddle.value = props.draw.rect(paddleWidth, paddleHeight)
          .x(props.paddleX)
          .cy(props.mapHeight / 2)
          .fill('#00ff99');
      }
    };

    const paddleMovement = () => {
      const keys = new Set();

      SVG.on(document, 'keydown', (e) => {
        keys.add(e.key);
        handleKeys();
      });

      SVG.on(document, 'keyup', (e) => {
        keys.delete(e.key);
        handleKeys();
      });

      const handleKeys = () => {
        const dir = keys.has(props.keyUp) ? -2 : keys.has(props.keyDown) ? 2 : 0;
        movePaddle(dir);
      };

      const movePaddle = (dir) => {
        y.value += dir;
        // Ensure that the paddle stays within the height boundaries
        y.value = Math.max(paddleHeight / 2, Math.min(y.value, props.mapHeight - paddleHeight / 2));
        if (paddle.value) {
          paddle.value.cy(y.value);
        }
      };

      const update = () => {
        handleKeys();
        requestAnimationFrame(update);
      };

      update();
    };

    return {
      paddle,
      x,
      y,
      width,
      height
    };
  }
};
</script>

<template>
</template>

<style scoped>
</style>