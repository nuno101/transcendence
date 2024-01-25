<script>
import { ref, onMounted, watch } from 'vue';

export default {
  props: {
    width : Number,
    height : Number
  },
  setup(props, { emit }){
    const canvas = ref(null);

    onMounted(() => {
      initializeGameMap();
      document.body.style.overflow = 'hidden';
    });

    const initializeGameMap = () => {
        canvas.value = document.querySelector('.pong');
        if(canvas.value) {
          canvas.value.width = props.width;
          canvas.value.height = props.height;
        }
        emit('update:canvas', canvas.value);
    };

    return {
      props
    };
  }
};
</script>

<template>
  <div class="container d-flex justify-content-center align-items-center">
    <canvas ref="canvas" id="pong" class="pong">
    </canvas>
    <div class="middle-line"></div>
  </div></template>

<style scoped>
canvas {
    border: 1px solid black;
    position: absolute;
    top: 20%;
    background: #111111;
}

.middle-line {
  position: absolute;
  top: 20%;
  left: 50%;
  width: 2px;
  height: 351px;
  background: repeating-linear-gradient(
    to bottom,
    #fff,
    #fff 14px,
    #000 14px,
    #000 28px
  );
}
</style>