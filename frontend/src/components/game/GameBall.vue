<script>
import { ref, onMounted, watch, toRefs } from 'vue';

export default {
  props: {
    draw : Object,
    height : Number,
    width : Number,
    paddle1 : Object,
    paddle2 : Object,
    incrementRightScore: Function,
    incrementLeftScore: Function
  },
  setup(props){
    const ball = ref(null);
    let x, y, radius, xSpeed, ySpeed;
    // Destructure reactive props
    const { paddle1, paddle2 } = toRefs(props);

    onMounted(() => {
        ballMovement();
    });

    watch(() => props.draw, () => {
      initializeBall();
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
            paddleCollision(paddle1.value);
            paddleCollision(paddle2.value);

            // hits top or bottom border
            if(y < radius || y > props.height - radius) {
                ySpeed = -ySpeed;
            }
            // restart game, hits left or right border
            if(x < radius) {
                props.incrementRightScore();
                resetBall();
            }
            else if(x > props.width + radius) {
                props.incrementLeftScore();
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
            console.log("PADDLE Y: " + paddle.y);
            console.log("PADDLE X: " + paddle.x);
            console.log("PADDLE height: " + paddle.height);
            console.log("PADDLE width: " + paddle.width);
            console.log("BALL Y: " + ball.value.y());
            if (paddle.x <= props.width / 2) {
                // Collision with the left paddle (paddle1)
                if (x - radius <= paddle.x + paddle.width && x > paddle.x) {
                    if (isSameHeight(paddle)) {
                    xSpeed = -xSpeed;
                    }
                }
                } else {
                // Collision with the right paddle (paddle2)
                if (x + radius >= paddle.x && x < paddle.x + paddle.width) {
                    if (isSameHeight(paddle)) {
                    xSpeed = -xSpeed;
                    }
                }
            }
        }
    };

    const isSameHeight = (paddle) => {
        return y >= paddle.y - paddle.height / 2 && y <= paddle.y + paddle.height / 2;
    }
  }
};
</script>

<template>
</template>

<style scoped>
</style>