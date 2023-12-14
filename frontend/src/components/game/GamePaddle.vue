<script>
import SVG from 'svg.js';
import { ref, onMounted, watch } from 'vue';

export default {
  props: {
    draw : Object,
    width : Number,
    height : Number,
    paddleX : Number,
    keyUp : String,
    keyDown : String
  },
  setup(props){
    const paddleHeight = 80;
    const paddleWidth = 20;
    const paddle = ref(null);
    const yMov = ref(props.height / 2);

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
        paddle.value = props.draw.rect(paddleWidth, paddleHeight).x(props.paddleX).cy(props.height / 2).fill('#00ff99');
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
        // Ensure that the paddle stays within the height boundaries
        yMov.value += dir;
        yMov.value = Math.max(paddleHeight / 2, Math.min(yMov.value, props.height - paddleHeight / 2));

        if (paddle.value) {
          paddle.value.cy(yMov.value);
        }
      };

      const update = () => {
        handleKeys();
        requestAnimationFrame(update);
      };

      update();
    };
    return {};
  }
};
</script>

<template>
</template>

<style scoped>
</style>