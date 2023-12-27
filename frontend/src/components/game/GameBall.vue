<script>
import { ref, onMounted, watch, toRefs } from 'vue';
import SVG from 'svg.js';

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
    let radius, xSpeed, ySpeed;
    // Destructure reactive props
    const { paddle1, paddle2 } = toRefs(props);
    const isRoundStartMessageVisible = ref(false);

    onMounted(() => {
        initializeBall();
        ballMovement();
    });

    watch(() => props.draw, () => {
      initializeBall();
    });

    const initializeBall = () => {
        if(props.draw) {
            radius = 10;
            ball.value = props.draw
            .cx(props.width / 2)
            .cy(props.height / 2)
            .circle(radius * 2).fill('#eeeeeee');
            resetBall();
        }
    };
   
    const resetBall = () => {
        xSpeed = 0;
        ySpeed = 0;
        ball.value.cx(props.width / 2).cy(props.height / 2);

        const handleKeyPress = (event) => {
            // Check if the key pressed is any key you want to use to start the ball
            if (event.key === ' ') {
                // Set random direction for the ball movement
                xSpeed = Math.random() > 0.5 ? -Math.random() * 2 - 1 : Math.random() * 2 + 1;
                ySpeed = Math.random() * 6 - 3;

                // Remove the event listener after starting the ball movement
                SVG.off(document, 'keydown', handleKeyPress);
                isRoundStartMessageVisible.value = false;
            }
        };

        // Add the event listener for keydown events
        SVG.on(document, 'keydown', handleKeyPress);
        // Show the round start message
        isRoundStartMessageVisible.value = true;
    };

    const ballMovement = () => {
        const update = () => {
            if (ball.value && ball.value.cx && ball.value.cy) {
                paddleCollision();
                // hits top or bottom border
                if (ball.value.cy() < radius || ball.value.cy() > props.height - radius) {
                    ySpeed = -ySpeed;
                }
                // restart game, hits left or right border
                if (ball.value.cx() < radius) {
                    props.incrementRightScore();
                    resetBall();
                } else if (ball.value.cx() > props.width + radius) {
                    props.incrementLeftScore();
                    resetBall();
                }
                ball.value.cx(ball.value.cx() + xSpeed).cy(ball.value.cy() + ySpeed);
                }
                requestAnimationFrame(update);
            };
        update();
    };

    const paddleCollision = () => {
        // Collision with the left paddle (paddle1)
        if(paddle1.value) {
            if (ball.value.cx() - radius <= paddle1.value.x + paddle1.value.width &&
                ball.value.cx() > paddle1.value.x) {
                if (Math.abs(ball.value.cy() - paddle1.value.y) <= paddle1.value.height / 2) {
                    xSpeed = -xSpeed;
                }
            }
        }
        // Collision with the right paddle (paddle2)
        if(paddle2.value) {
            if (ball.value.cx() + radius >= paddle2.value.x &&
                ball.value.cx() < paddle2.value.x + paddle2.value.width) {
                if (Math.abs(ball.value.cy() - paddle2.value.y) <= paddle2.value.height / 2) {
                    xSpeed = -xSpeed;
                }
            }
        }
    };

    return {
      isRoundStartMessageVisible
    };
  }
};
</script>

<template>
    <div v-if="isRoundStartMessageVisible">
        <p>[ Press the space key to continue ]</p>
    </div>
</template>

<style scoped>
</style>