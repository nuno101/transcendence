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
    const keys = new Set();

    const paddle = ref({
      x: props.paddleX,
      y: props.mapHeight / 2,
      width: paddleWidth,
      height: paddleHeight,
      color: '#00ff99'
    });
    
    const handleKeys = () => {
      const dir = keys.has(props.keyUp) ? -3 : keys.has(props.keyDown) ? 3 : 0;
      movePaddle(dir);
    };

    const movePaddle = (dir) => {
      paddle.value.y += dir;
      paddle.value.y = Math.max(paddleHeight / 2, Math.min(paddle.value.y, props.mapHeight - paddleHeight / 2));
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
      drawPaddle();
      paddleMovement();
    });

    onUnmounted(() => {
      document.removeEventListener('keydown', handleKeyDown);
      document.removeEventListener('keyup', handleKeyUp);
    });

    watch(() => props.canvas, () => {
      drawPaddle();
      paddleMovement();
    });

    const drawPaddle = () => {
      if(props.canvas){
        const context = props.canvas.getContext('2d');
        context.clearRect(
          paddle.value.x,
          paddle.value.y - paddleHeight / 2,
          paddle.value.width,
          paddleHeight
        );
        context.fillStyle = paddle.value.color;
        context.fillRect(
          paddle.value.x,
          paddle.value.y - paddleHeight / 2,
          paddle.value.width,
          paddle.value.height
        );
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