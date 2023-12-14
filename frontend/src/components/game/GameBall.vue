<script>
import { ref, onMounted, watch, toRefs } from 'vue';

export default {
  props: {
      draw : Object,
      height : Number,
      width : Number,
      paddle1 : Object,
      paddle2 : Object
  },
  setup(props){
    const ball = ref(null);
    let x, y, radius, xSpeed, ySpeed;
    // Destructure reactive props
    // const { paddle1, paddle2 } = toRefs(props);

    onMounted(() => {
        initializeBall();
        ballMovement();
    });

    watch(() => props.draw, () => {
      initializeBall();
    });

    // Use watchEffect to watch reactive properties
    watch(() => [props.paddle1?.y, props.paddle2?.y], ([paddle1Y, paddle2Y]) => {
      console.log('IN BALL PADDLE1 Y:', paddle1Y);
      console.log('IN BALL PADDLE2 Y:', paddle2Y);
    });

    const initializeBall = () => {
        if(props.draw) {
            radius = 10;
            resetBall();
            ball.value = props.draw.circle(radius * 2).cx(x).cy(y).fill('#eeeeeee');
        }
    };
   
    const resetBall = () => {
        x = props.width / 2;
        y = props.height / 2;
        xSpeed = Math.random() > 0.5 ? -Math.random() * 2 - 1 : Math.random() * 2 + 1;
        ySpeed = Math.random() * 6 - 3;
    };

    const ballMovement = () => {
        const update = () => {
            paddleCollision(props.paddle1);
        paddleCollision(props.paddle2);

            // hits top or bottom border
            if(y < radius || y > props.height - radius) {
                ySpeed = -ySpeed;
            }
            // restart game, hits left or right border
            if(x < radius || x > props.width + radius) {
                resetBall();
            }

            x += xSpeed;
            y += ySpeed;
            if (ball.value) {
                ball.value.cx(x).cy(y);
            }
            requestAnimationFrame(update);
        };
        update();
    };

    const paddleCollision = (paddle) => {
        if(paddle) {
            if(x - radius <= paddle.x + paddle.width && x > paddle.x) {
                if(isSameHeight(paddle)) {
                    xSpeed = -xSpeed;
                }
            }
        }
    };

    const isSameHeight = (paddle) => {
        return y >= paddle.y && y <= paddle.y + paddle.height;
    }
    return {};
  }
};
</script>

<template>
</template>

<style scoped>
</style>