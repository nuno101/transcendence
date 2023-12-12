<template>
  <div class="container">
    <div class="row justify-content-center">
      <div ref="pong" class="col-md-8 pong d-flex justify-content-center align-items-center"></div>
    </div>
  </div>
</template>

<script>
import SVG from 'svg.js';
import { onMounted, ref } from 'vue';


export default {
    setup() {
        const draw = ref(null);
        const width = 435;
        const height = 300;
        let playerLeft = ref(0);
        let playerRight = ref(0);
        const vx = ref(7);
        const vy = ref(7);
        const paddleHeight = 100;
        const paddleWidth = 20;
        const ballSize = 20;
        const paddleDirectionLeft = ref(0);
        const paddleDirectionRight = ref(0);
        const paddleSpeed = 7;
        let paddleLeft;
        let paddleRight;
        let ball;
        const scoreLeft = ref(0);
        const scoreRight = ref(0);

        // const exposeVariables = () => {
        //     return {
        //        exposedPlayerLeft: playerLeft,
        //         exposedPlayerRight: playerRight,
        //     };
        // }; 

        onMounted(() => {
            document.body.style.overflow = 'hidden'; // non-scrollable page
            initializeGame();
            startGameLoop();
            setupKeyboardControls();
            setupGameClick();
        });
        
        const initializeGame = () => {
            // GAME FIELD
            draw.value = SVG(document.querySelector('.pong')).size(width, height);
            draw.value.rect(width, height).fill('#555555');
            const line = draw.value.line(width / 2, 0, width / 2, height);
            line.stroke({ width: 3, color: '#fff'});

            // DRAW PADDLES & BALL
            paddleLeft = draw.value.rect(paddleWidth, paddleHeight).x(0).cy(height / 2).fill('#00ff99');
            paddleRight = paddleLeft.clone().x(width - paddleWidth).fill('#ff0066');
            ball = draw.value.circle(ballSize).center(width / 2, height / 2).fill('#7f7f7f');

            // SCORE BOARDs
            scoreLeft.value = draw.value.text(playerLeft.value + '').font({
                size: 32,
                anchor: 'end',
                fill: '#fff'
            }).move(width / 2 - 10, 10);
            scoreRight.value = scoreLeft.value.clone().text(playerRight.value + '').font('anchor', 'start').x(width / 2 + 10);
        };

        const startGameLoop = () => {
            setInterval(() => {
                updateGame();
            }, 30); //possibility to adjust interval
        };

        const setupKeyboardControls = () => {
            // Listen for keydown events to control the paddles
            SVG.on(document, 'keydown', (e) => {
                if (e.key === 'ArrowUp') {
                paddleDirectionRight.value = -1;
                } else if (e.key === 'ArrowDown') {
                paddleDirectionRight.value = 1;
                } else if (e.key === 'w') {
                paddleDirectionLeft.value = -1;
                } else if (e.key === 's') {
                paddleDirectionLeft.value = 1;
                }
            });
            // Reset the direction when the key is released
            SVG.on(document, 'keyup', (e) => {
                if (e.key === 'ArrowUp' || e.key === 'ArrowDown') {
                paddleDirectionRight.value = 0;
                } else if (e.key === 'w' || e.key === 's') {
                paddleDirectionLeft.value = 0;
                }
            });
        };

        const setupGameClick = () => {
            draw.value.on('click', () => {
                if (vx.value === 0 && vy.value === 0) {
                    // Set random direction with constant speed
                    const maxAngle = 20 * (Math.PI / 180); // Convert degrees to radians
                    const minAngle = -20 * (Math.PI / 180); // Convert degrees to radians
                    let angle = Math.random() * (maxAngle - minAngle) + minAngle;
                    const speed = 7; // Adjust the speed as needed
                    vx.value = speed * Math.cos(angle);
                    vy.value = speed * Math.sin(angle);
                }
            });
        };

        const updateGame = () => {
            movePlayerPaddles();
            updateBallPosition();
            checkPaddleCollisions();
            updateBallPosition();
        };

        const updateBallPosition = () => {   
            ball.cx(ball.cx() + vx.value);
            ball.cy(ball.cy() + vy.value);

            const ballTop = ball.cy() - ballSize / 2;
            const ballBottom = ball.cy() + ballSize / 2;
            const ballLeft = ball.cx() - ballSize / 2;
            const ballRight = ball.cx() + ballSize / 2;

            // CHECK FOR HITTED BORDERS
            if (ballLeft <= 0 || ballRight >= width) {
                // Check if the ball is within the height range of the paddles
                if (ballTop >= paddleLeft.y() && ballBottom <= paddleLeft.y() + 100) {
                    vx.value = -vx.value; // Reverse the horizontal velocity
                } else {
                    // Scoring event
                    // If the ball hits the left border, playerRight scores; if it hits the right border, playerLeft scores
                    if (ballLeft <= 0) {
                        ++playerRight.value;
                    } else {
                        ++playerLeft.value;
                    }
                    // Update scores
                    scoreLeft.value.text(playerLeft.value + '');
                    scoreRight.value.text(playerRight.value + '');
                    reset();
                }
            }
            // Check for top and bottom borders hit
            if (ballTop <= 0 || ballBottom >= height) {
                vy.value = -vy.value; // Reverse the vertical velocity
            }
        };

        const reset = () => {
            vx.value = 0;
            vy.value = 0;
            ball.center(width / 2, height / 2);
            paddleLeft.animate(100).cy(height / 2);
            paddleRight.animate(100).cy(height / 2);
        };

        const movePlayerPaddles = () => {
            // Move the right player paddle based on user input
            let playerPaddleRightY = paddleRight.y();
            if (playerPaddleRightY <= 0 && paddleDirectionRight.value === -1) {
                paddleRight.cy(paddleHeight / 2);
            } else if (playerPaddleRightY >= height - paddleHeight && paddleDirectionRight.value === 1) {
                paddleRight.y(height - paddleHeight);
            } else {
                paddleRight.dy(paddleDirectionRight.value * paddleSpeed);
            }
            // Move the left player paddle based on user input
            let playerPaddleLeftY = paddleLeft.y();
            if (playerPaddleLeftY <= 0 && paddleDirectionLeft.value === -1) {
                paddleLeft.cy(paddleHeight / 2);
            } else if (playerPaddleLeftY >= height - paddleHeight && paddleDirectionLeft.value === 1) {
                paddleLeft.y(height - paddleHeight);
            } else {
                paddleLeft.dy(paddleDirectionLeft.value * paddleSpeed);
            }
        };

        const checkPaddleCollisions = () => {
            const ballLeft = ball.cx() - ballSize / 2;
            const ballRight = ball.cx() + ballSize / 2;
            const ballTop = ball.cy() - ballSize / 2;
            const ballBottom = ball.cy() + ballSize / 2;

            // Check collision with left paddle
            if (ballLeft <= paddleWidth && ballRight >= 0 &&
                ballTop <= paddleLeft.y() + paddleHeight &&
                ballBottom >= paddleLeft.y()) {
                vx.value = -vx.value; // Reverse the horizontal velocity
                vy.value = -vy.value;
            }
            // Check collision with right paddle
            if (ballRight >= width - paddleWidth && ballLeft <= width &&
                ballTop <= paddleRight.y() + paddleHeight &&
                ballBottom >= paddleRight.y()) {
                vx.value = -vx.value; // Reverse the horizontal velocity
                vy.value = -vy.value;
            }
            // Check collision with left paddle wall
            if (ballLeft <= 0) {
                vx.value = Math.abs(vx.value); // Ensure positive horizontal velocity
            }
            // Check collision with right paddle wall
            if (ballRight >= width) {
                vx.value = -Math.abs(vx.value); // Ensure negative horizontal velocity
            }
            // Check collision with bottom or top of paddle
            if (ballTop <= paddleLeft.y() + paddleHeight &&
                ballBottom >= paddleLeft.y() &&
                ballLeft <= paddleWidth) {
                vy.value = -vy.value; // Reverse the vertical velocity
            }
            if (ballTop <= paddleRight.y() + paddleHeight &&
                ballBottom >= paddleRight.y() &&
                ballRight >= width - paddleWidth) {
                vy.value = -vy.value; // Reverse the vertical velocity
            }
        };
    }
};

</script>

<style scoped>
.pong {
    min-height: 100vh;
}
</style>

