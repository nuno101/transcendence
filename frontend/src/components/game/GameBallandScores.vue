<script>
import { ref, onMounted, watch, toRefs } from 'vue';
import SVG from 'svg.js';

export default {
  props: {
    draw : Object,
    height : Number,
    width : Number,
    paddle1 : Object,
    paddle2 : Object
  },
  setup(props){
    const scoreLeft = ref(0);
    const scoreRight = ref(0);
    const isGameOver = ref(false);
    let textLeft = null;
    let textRight = null;
    const ball = ref(null);
    let radius, xSpeed, ySpeed;
    // Destructure reactive props
    const { paddle1, paddle2 } = toRefs(props);
    const isRoundStartMessageVisible = ref(false);

    onMounted(() => {
        initializeBall();
        initializeScores();
        ballMovement();
    });

    watch(() => props.draw, () => {
      initializeBall();
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
      if(props.draw) {
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
      }
    };

    const incrementRightScore = () => {
      scoreRight.value++;
      // Update the text content
      textRight.text(scoreRight.value + '');
      if (scoreRight.value === 3) {
        isGameOver.value = true;
      }
    };

    const incrementLeftScore = () => {
      scoreLeft.value++;
      // Update the text content
      textLeft.text(scoreLeft.value + '');
      if (scoreLeft.value === 3) {
        isGameOver.value = true;
      }
    };

    const initializeBall = () => {
        if(props.draw) {
            radius = 10;
            ball.value = props.draw
                .cx(props.width / 2)
                .cy(props.height / 2)
                .circle(radius * 2)
                .fill('#eeeeeee');
            resetBall();
        }
    };
   
    const resetBall = () => {
        xSpeed = 0;
        ySpeed = 0;
        ball.value.cx(props.width / 2).cy(props.height / 2);

        const handleKeyPress = (event) => {
            // Check if the key pressed is any key you want to use to start the ball
            if (event.key === ' ' && isGameOver.value === false) {
                // Set random direction for the ball movement
                // should it be dependent on who scored?
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
                    incrementRightScore();
                    resetBall();
                } else if (ball.value.cx() > props.width + radius) {
                    incrementLeftScore();
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
                ball.value.cx() > paddle1.value.x &&
                Math.abs(ball.value.cy() - paddle1.value.y) <= paddle1.value.height / 2)
                // && ball.value.cx() > paddle1.value.x + paddle1.value.width / 2)
                    xSpeed = -xSpeed;
        }
        // Collision with the right paddle (paddle2)
        if(paddle2.value) {
            if (ball.value.cx() + radius >= paddle2.value.x &&
                ball.value.cx() < paddle2.value.x + paddle2.value.width &&
                Math.abs(ball.value.cy() - paddle2.value.y) <= paddle2.value.height / 2)
                // && ball.value.cx() < paddle2.value.x + paddle2.value.width / 2)
                    xSpeed = -xSpeed;
        }
    };

    return {
      isRoundStartMessageVisible,
      isGameOver,
      scoreLeft,
      scoreRight
    };
  }
};
</script>

<template>
    <div v-if="isRoundStartMessageVisible && !isGameOver">
        <p>[ Press the space key to continue ]</p>
    </div>
    <div v-if="isGameOver">
      <p>{{ scoreLeft > scoreRight ? 'Player Left' : 'Player Right' }} Wins!</p>
    </div>
</template>

<style scoped>
</style>