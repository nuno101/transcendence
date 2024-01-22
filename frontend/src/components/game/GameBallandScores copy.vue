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
    const scoreLeft = ref(Number(localStorage.getItem('scoreLeft')) || 0);
    const scoreRight = ref(Number(localStorage.getItem('scoreRight')) || 0);
    const isGameOver = ref(localStorage.getItem('isGameOver') || false);
    let textLeft = null;
    let textRight = null;
    const ball = ref(null);
    let radius, xSpeed, ySpeed;
    // Destructure reactive props
    const { paddle1, paddle2 } = toRefs(props);
    const isRoundStartMessageVisible = ref(false);

    onMounted(() => {
        initializeScoresAndBall();
        ballMovement();
    });

    watch(() => props.draw, () => {
      initializeScoresAndBall();
    });

    const initializeScoresAndBall = () => {
        // Remove existing text elements if they exist
      if (textLeft)
        textLeft.remove();
      if (textRight)
        textRight.remove();
      // Create text elements for scores
      if(props.draw) {
        // BALL
        radius = 10;
        ball.value = props.draw
            .cx(props.width / 2)
            .cy(props.height / 2)
            .circle(radius * 2)
            .fill('#eeeeeee');
        resetBall();
        // SCORES
        textLeft = props.draw.text(scoreLeft.value + '')
        .font({size: 32, anchor: 'end', fill: '#fff'})
        .move(props.width / 2 - 10, 10);
        textRight = props.draw.text(scoreRight.value + '')
        .font({size: 32, anchor: 'start', fill: '#fff'})
        .move(props.width / 2 + 10, 10);
      }
    };

    const incrementRightScore = () => {
      scoreRight.value++;
      localStorage.setItem('scoreRight', scoreRight.value.toString());
      // Update the text content
      textRight.text(scoreRight.value + '');
      if (scoreRight.value === 3) {
        isGameOver.value = true;
        localStorage.setItem('isGameOver', 'true');
      }
    };

    const incrementLeftScore = () => {
      scoreLeft.value++;
      localStorage.setItem('scoreLeft', scoreLeft.value.toString());
      // Update the text content
      textLeft.text(scoreLeft.value + '');
      if (scoreLeft.value === 3) {
        isGameOver.value = true;
        localStorage.setItem('isGameOver', 'true');
      }
    };
   
    const resetBall = () => {
        xSpeed = 0;
        ySpeed = 0;
        ball.value.cx(props.width / 2).cy(props.height / 2);

        const handleKeyPress = (event) => {
            if (event.key === ' ' && isGameOver.value === false) {
                // Set random direction for the ball movement
                // should it be dependent on who scored?
                xSpeed = Math.random() > 0.5 ? -Math.random() * 2 - 1 : Math.random() * 2 + 1;
                ySpeed = Math.random() * 6 - 3;
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
    const handleEndOfGame = (type) => {
      localStorage.clear();
      if(type === "rematch")
        window.location.reload();
    };
    return {
      isRoundStartMessageVisible,
      isGameOver,
      scoreLeft,
      scoreRight,
      handleEndOfGame
    };
  }
};
</script>

<template>
  <div class="container d-flex justify-content-center align-items-center">
    <div v-if="isRoundStartMessageVisible && !isGameOver" class="alert alert-success spaceoverlay" role="alert">
      [ Press the space key to continue ]
    </div>
    <div v-if="isGameOver" class="overlay" role="alert">
      <p>{{ scoreLeft > scoreRight ? 'Player Left' : 'Player Right' }} wins!</p>
      <div class="button-container">
      <!-- IN BOTH CASES: POST RESULT OF GAME TO BACKEND BEFORE RESETTING -->
      <button @click="handleEndOfGame('rematch')" type="button" class="btn btn-outline-primary">Rematch</button>
      <router-link to="/dashboard">
        <button @click="handleEndOfGame('')" type="button" class="btn btn-outline-primary">Back to Menu</button>
      </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.overlay {
  position: absolute;
  top: 118%;
  left: 50%;
  transform: translate(-50%, -250%);
  background: rgba(255, 255, 255, 0.8);
  padding: 90px 100vh;
  text-align: center;
}

.spaceoverlay {
  position: absolute;
  top: 40%;
}

.button-container {
  margin-top: 20px;
  display: flex;
  gap: 20px;
  justify-content: center;
}

.btn {
  margin: 0 0 0 35px;
  white-space: nowrap;
}
</style>