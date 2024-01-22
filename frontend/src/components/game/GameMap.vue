<script>
import { ref, onMounted } from 'vue';

export default {
  props: {
    width : Number,
    height : Number
  },
  setup(props, { emit }){
    const canvas = ref(null);
    const context = ref(null);
    const ctx = ref(null);

    onMounted(() => {
      draw();
      initializeGameMap();
      document.body.style.overflow = 'hidden';
    });

    // onUnmounted(() => {
    //   document.body.style.overflow = 'auto';
    // });

    const initializeGameMap = () => {
      // if(canvas.value) {
        canvas.value = document.querySelector('.pong');
        console.log(props.width);
        console.log(props.height);
        console.log(canvas);
        if(canvas.value) {
          canvas.value.width = props.width;
          canvas.value.height = props.height;
        }

        context.value = canvas.value.getContext('2d');
        // Draw middle line
        context.value.beginPath();
        context.value.moveTo(props.width/2, 0);
        context.value.lineTo(props.width/2, props.height);
        context.value.lineWidth = 2;
        context.value.strokeStyle = '#fff';
        context.value.stroke();
        context.value.closePath();

      emit('update:canvas', canvas.value);
    };

    const draw = ()  =>{
      const canvas = document.getElementById("pong");
      if (canvas.getContext) {
        ctx.value = canvas.getContext("2d");
      }
      window.addEventListener("load", draw);
    };
    return {
      props
    };
  }
};
</script>

<template>
  <div class="container d-flex justify-content-center align-items-center">
    <canvas ref="pong" id="pong" class="pong" width="props.width" height="props.height"></canvas>
  </div></template>

<style scoped>
canvas {
    border: 1px solid black;
    position: absolute;
    top: 20%;
    background: #555555;
}
</style>