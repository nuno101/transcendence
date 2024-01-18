<script>
import { ref, onMounted, onUnmounted, watch } from 'vue';

export default {
  props: {
    canvas : Object,
    context : Object,
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
    const y = ref(props.mapHeight / 2);
    const keys = new Set();

    const handleKeys = () => {
      const dir = keys.has(props.keyUp) ? -3 : keys.has(props.keyDown) ? 3 : 0;
      movePaddle(dir);
    };

    const movePaddle = (dir) => {
      y.value += dir;
      y.value = Math.max(paddleHeight / 2, Math.min(y.value, props.mapHeight - paddleHeight / 2));
    };

    const handleKeyDown = (e) => {
      keys.add(e.key);
      handleKeys();
    };

    const handleKeyUp = (e) => {
      keys.delete(e.key);
      handleKeys();
    };

    onMounted(() => {
      initializePaddle();
      paddleMovement();
    });

    watch(() => props.canvas, () => {
      initializePaddle();
      paddleMovement();
    });

    onUnmounted(() => {
      document.removeEventListener('keydown', handleKeyDown);
      document.removeEventListener('keyup', handleKeyUp);
    });

    const initializePaddle = () => {
      if (props.canvas) {
        paddle.value = {
          x: props.paddleX,
          width: paddleWidth,
          height: paddleHeight,
          color: '#00ff99'
        }
        drawPaddle();
      }
    };
    
    const drawPaddle = () => {
      if(props.canvas){
        const context = props.canvas.getContext('2d');
        context.clearRect(paddle.value.x, 0, paddle.value.width, props.mapHeight);
        context.fillStyle = paddle.value.color;
        context.fillRect(paddle.value.x, y.value - paddleHeight / 2, paddle.value.width, paddle.value.height);
      }
    };

    const paddleMovement = () => {  
      const update = () => {
        handleKeys();
        drawPaddle();
        requestAnimationFrame(update);
      };

      document.addEventListener('keydown', handleKeyDown);
      document.addEventListener('keyup', handleKeyUp);

      update();
    };

    return {
      paddle
    };
  }
};
</script>

<template>
</template>

<style scoped>
</style>