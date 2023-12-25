<script>
import { ref, watch } from 'vue';

export default {
  props: {
      draw : Object,
      height : Number,
      width : Number,
    },
  setup(props) {
    const scoreLeft = ref(0);
    const scoreRight = ref(0);
    let textLeft = null;
    let textRight = null;

    watch(() => props.draw, () => {
      initializeScores();
    });

    const initializeScores = () => {
        // Remove existing text elements if they exist
      if (textLeft) {
        textLeft.remove();
      }
      if (textRight) {
        textRight.remove();
      }

      // Create text elements for scores
      textLeft = props.draw.text(scoreLeft.value + '')
        .font({
          size: 32,
          anchor: 'end',
          fill: '#fff'
        }).move(props.width / 2 - 10, 10);

      textRight = props.draw.text(scoreRight.value + '')
        .font({
          size: 32,
          anchor: 'start',
          fill: '#fff'
        }).move(props.width / 2 + 10, 10);
    };

    const incrementRightScore = () => {
      scoreRight.value++;
      // Update the text content
      textRight.text(scoreRight.value + '');
    };

    const incrementLeftScore = () => {
      scoreLeft.value++;
      // Update the text content
      textLeft.text(scoreLeft.value + '');
    };

    return {
        incrementRightScore,
        incrementLeftScore
    }
  }
};
</script>

<template>
</template>

<style scoped>
</style>