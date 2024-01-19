<script>
import { ref, onMounted, watch, toRefs } from 'vue';

export default {
  props: {
    canvas : Object,
    height : Number,
    width : Number,
    paddle1 : Object,
    paddle2 : Object
  },
  setup(props){
    const scoreLeft = ref(Number(localStorage.getItem('scoreLeft')) || 0);
    const scoreRight = ref(Number(localStorage.getItem('scoreRight')) || 0);
    const isGameOver = ref(localStorage.getItem('isGameOver') || false);
    const ball = ref(null);
    let radius, xSpeed, ySpeed;
    // Destructure reactive props
    const { paddle1, paddle2 } = toRefs(props);
    // const paddle1 = ref(props.paddle1);
    // const paddle2 = ref(props.paddle2);

    const isRoundStartMessageVisible = ref(false);

    onMounted(() => {
        console.log(props.canvas);
        initializeScoresAndBall();
        ballMovement();
    });

    watch(() => props.canvas, () => {
      initializeScoresAndBall();
    });

  watch([() => paddle1.value?.y, () => paddle2.value?.y], ([newPaddle1Y, newPaddle2Y]) => {
    console.log("PADDLE1 Y: " + newPaddle1Y);
    console.log("PADDLE2 Y: " + newPaddle2Y);
  });

    const initializeScoresAndBall = () => {
      if (props.canvas) {
        const ctx = props.canvas.getContext('2d');
        radius = 10;
        ball.value = {
          x: props.width / 2,
          y: props.height / 2,
          radius, 
          fillStyle: 'eeeeee'
        };

        resetBall();

        ctx.font = '32px Arial';
        ctx.fillStyle = 'fff';
        ctx.textAlign = 'end';
        ctx.fillText(scoreLeft.value + '', props.width / 2 - 10, 40);

        ctx.textAlign = 'start';
        ctx.fillText(scoreRight.value + '', props.width / 2 + 10, 40);
      }
    };

    const incrementRightScore = () => {
      scoreRight.value++;
      localStorage.setItem('scoreRight', scoreRight.value.toString());
      initializeScoresAndBall();
      if (scoreRight.value === 3) {
        isGameOver.value = true;
        localStorage.setItem('isGameOver', 'true');
      }
    };

    const incrementLeftScore = () => {
      scoreLeft.value++;
      localStorage.setItem('scoreLeft', scoreLeft.value.toString());
      initializeScoresAndBall();
      if (scoreLeft.value === 3) {
        isGameOver.value = true;
        localStorage.setItem('isGameOver', 'true');
      }
    };
   
    const resetBall = () => {
        xSpeed = 0;
        ySpeed = 0;
        ball.value.x = props.width / 2;
        ball.value.y = props.height / 2;
        // RESET PADDLES HERE
        const handleKeyPress = (event) => {
            if (event.key === ' ' && isGameOver.value === false) {
                // Set random direction for the ball movement
                // should it be dependent on who scored?
                xSpeed = Math.random() > 0.5 ? -Math.random() * 2 - 1 : Math.random() * 2 + 1;
                ySpeed = Math.random() * 6 - 3;
                document.removeEventListener('keydown', handleKeyPress);
                isRoundStartMessageVisible.value = false;
            }
        };
        // Add the event listener for keydown events
        document.removeEventListener('keydown', handleKeyPress);
        document.addEventListener('keydown', handleKeyPress);
        // Show the round start message
        isRoundStartMessageVisible.value = true;
    };

    const ballMovement = () => {
      const update = () => {
        if(props.canvas){
            const ctx = props.canvas.getContext('2d');

            paddleCollision();
            // hits top or bottom border
            if (ball.value.y - ball.value.radius <= 0 || ball.value.y + ball.value.radius >= props.height)
                ySpeed = -ySpeed;
            // restart game, hits left or right border
            if (ball.value.x - ball.value.radius <= 0) {
                incrementRightScore();
                resetBall();
            } else if (ball.value.x + ball.value.radius >= props.width) {
                incrementLeftScore();
                resetBall();
            }
            ball.value.x += xSpeed;
            ball.value.y += ySpeed;
  
            ctx.clearRect(0, 0, props.canvas.width, props.canvas.height);
            ctx.beginPath();
            ctx.arc(ball.value.x, ball.value.y, ball.value.radius, 0, Math.PI * 2);
            ctx.fillStyle = ball.value.fillStyle;
            ctx.fill();
            ctx.closePath();
  
            ctx.font = '32 Arial';
            ctx.fillStyle = 'fff';
            ctx.textAlign = 'end';
            ctx.fillText(scoreLeft.value + '', props.width / 2 - 10, 40);
            ctx.textAlign = 'start';
            ctx.fillText(scoreRight.value + '', props.width / 2 + 10, 40);
          }
          requestAnimationFrame(update);
        };
        update();
    };

    const paddleCollision = () => {
        // if(props.paddle1)
        //     console.log("PADDLE1 Y" + props.paddle1.y);
        // Collision with the left paddle (paddle1)
        if(props.paddle1 &&
          ball.value.x - ball.value.radius <= props.paddle1.x + props.paddle1.width &&
          ball.value.x > props.paddle1.x &&
          Math.abs(ball.value.y - props.paddle1.y) <= props.paddle1.height / 2){
            // && ball.value.x > props.paddle1.x + props.paddle1.width / 2)
            xSpeed = -xSpeed;
        }
        // Collision with the right paddle (paddle2)
        if(props.paddle2 &&
          ball.value.x + ball.value.radius >= props.paddle2.x &&
          ball.value.x < props.paddle2.x + props.paddle2.width &&
          Math.abs(ball.value.y - props.paddle2.y) <= props.paddle2.height / 2){
          // && ball.value.x < props.paddle2.x + props.paddle2.width / 2)
            xSpeed = -xSpeed;
        }
    };

    const handleEndOfGame = (type) => {
      localStorage.clear();
      if(type === "rematch") window.location.reload();
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