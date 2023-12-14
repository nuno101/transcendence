<script>
import SVG from 'svg.js';
import { ref, onMounted } from 'vue';

export default {
  props: {
    width : Number,
    height : Number
  },
  setup(props, { emit }){
    const draw = ref(null);

    onMounted(() => {
        document.body.style.overflow = 'hidden';
        initializeGameMap();
    });

    const initializeGameMap = () => {
      draw.value = SVG(document.querySelector('.pong')).size(props.width, props.height);
      draw.value.rect(props.width, props.height).fill('#555555');
      const line = draw.value.line(props.width / 2, 0, props.width / 2, props.height);
      line.stroke({ width: 3, color: '#fff'});
      // Emitting the draw object to the parent component
      emit('update:draw', draw.value);
    };
    return {};
  }
};
</script>

<template>
  <div class="container d-flex justify-content-center align-items-center">
    <div ref="pong" class="pong"></div>
  </div></template>

<style scoped>
.pong {
    max-height: 100vh;
}
</style>