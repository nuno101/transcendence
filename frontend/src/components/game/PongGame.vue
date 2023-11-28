<template>
  <div class="container">
    <div class="row justify-content-center">
      <div ref="pong" class="col-md-8 pong d-flex justify-content-center align-items-center"></div>
    </div>
  </div>
</template>

<script>
import SVG from 'svg.js';

export default {
    data() {
        return {
            draw: null,
            width: 450,
            height: 300,
            playerLeft: 0,
            playerRight: 0,
            vx: 5, //possibility to adjust x-velocity
            vy: 5, //possibility to adjust y-velocity
            paddleDirectionLeft: 0,
            paddleDirectionRight: 0,
            paddleSpeed: 5,
            paddleLeft: null, // Added reference for left paddle
            paddleRight: null, // Added reference for right paddle
            scoreLeft: null, // Added reference for left score
            scoreRight: null // Added reference for right score
        };
    },
    mounted() {
        this.initializeGame();
        this.startGameLoop();
        this.setupKeyboardControls();
        this.setupGameClick();
    },
    methods: {
        initializeGame() {
            // GAME FIELD
            this.draw = SVG(this.$refs.pong).size(this.width, this.height);
            const background = this.draw.rect(this.width, this.height).fill('#555555');
            const line = this.draw.line(this.width / 2, 0, this.width / 2, this.height);
            line.stroke({ width: 3, color: '#fff'});

            // PADDLE AND BALL SIZE
            const paddleWidth = 20;
            const paddleHeight = 100;
            const ballSize = 20;

            // DRAW PADDLES & BALL
            this.paddleLeft = this.draw.rect(paddleWidth, paddleHeight).x(0).cy(this.height / 2).fill('#00ff99');
            this.paddleRight = this.paddleLeft.clone().x(this.width - paddleWidth).fill('#ff0066');
            this.ball = this.draw.circle(ballSize).center(this.width / 2, this.height / 2).fill('#7f7f7f');

            // SCORE BOARD
            this.scoreLeft = this.draw.text(this.playerLeft + '').font({
                size: 32,
                anchor: 'end',
                fill: '#fff'
            }).move(this.width / 2 - 10, 10);

            this.scoreRight = this.scoreLeft.clone().text(this.playerRight + '').font('anchor', 'start').x(this.width / 2 + 10);
        },
        startGameLoop() {
            setInterval(() => {
                this.updateGame();
            }, 60); //possibility to adjust interval
        },
        setupKeyboardControls() {
            // Listen for keydown events to control the paddles
            SVG.on(document, 'keydown', (e) => {
                if (e.key === 'ArrowUp') {
                this.paddleDirectionRight = -1;
                } else if (e.key === 'ArrowDown') {
                this.paddleDirectionRight = 1;
                } else if (e.key === 'w') {
                this.paddleDirectionLeft = -1;
                } else if (e.key === 's') {
                this.paddleDirectionLeft = 1;
                }
            });
            // Reset the direction when the key is released
            SVG.on(document, 'keyup', (e) => {
                if (e.key === 'ArrowUp' || e.key === 'ArrowDown') {
                this.paddleDirectionRight = 0;
                } else if (e.key === 'w' || e.key === 's') {
                this.paddleDirectionLeft = 0;
                }
            });
        },
        setupGameClick() {
            if (!this.draw) {
                console.error("SVG instance not initialized.");
                return;
            }
            this.draw.on('click', () => {
                if (this.vx === 0 && this.vy === 0) {
                    this.vx = Math.random() * 300 - 150;
                    this.vy = Math.random() * 300 - 150;
                }
            });
        },
        updateGame() {
            this.updateBallPosition();
            this.checkPaddleCollisions();
            this.movePlayerPaddles();
        },
        updateBallPosition() {
            const ballSize = 20;
        
            this.ball.cx(this.ball.cx() + this.vx);
            this.ball.cy(this.ball.cy() + this.vy);

            const ballTop = this.ball.cy() - ballSize / 2;
            const ballBottom = this.ball.cy() + ballSize / 2;

            // CHECK FOR BORDERS HITTED
            // Check for collisions with top and bottom walls
            if (ballTop <= 0 || ballBottom >= this.height) {
                this.vy = -this.vy;
            }
            else if((this.vx < 0 && this.ball.cx() <= 0)
                || (this.vx > 0 && this.ball.cx() >= this.width)) {
                // Check if the ball is within the height range of the paddles
                if (ballTop >= this.paddleLeft.y() && ballBottom <= this.paddleLeft.y() + 100) {
                    this.vx = -this.vx; // Reverse the horizontal velocity
                } else {
                    // If not within paddle height, consider it a scoring event
                    // if x-velocity < 0 --> point for player 2, else player 1
                    if (this.vx < 0) {
                        ++this.playerRight;
                    } else {
                        ++this.playerLeft;
                    }

                // UPDATE SCORES
                this.scoreLeft.text(this.playerLeft + '');
                this.scoreRight.text(this.playerRight + '');

                this.reset();
                }
            }
        },
        reset(){
            this.vx = 0;
            this.vy = 0;
            this.ball.center(this.width / 2, this.height / 2);
            this.paddleLeft.animate(100).cy(this.height / 2);
            this.paddleRight.animate(100).cy(this.height / 2);       
        },
        movePlayerPaddles() {
            const height = 300;
            const paddleHeight = 100;

            // Move the right player paddle based on user input
            let playerPaddleRightY = this.paddleRight.y();
            if (playerPaddleRightY <= 0 && this.paddleDirectionRight === -1) {
                this.paddleRight.cy(paddleHeight / 2);
            } else if (playerPaddleRightY >= height - paddleHeight && this.paddleDirectionRight === 1) {
                this.paddleRight.y(height - paddleHeight);
            } else {
                this.paddleRight.dy(this.paddleDirectionRight * this.paddleSpeed);
            }

            // Move the left player paddle based on user input
            let playerPaddleLeftY = this.paddleLeft.y();
            if (playerPaddleLeftY <= 0 && this.paddleDirectionLeft === -1) {
                this.paddleLeft.cy(paddleHeight / 2);
            } else if (playerPaddleLeftY >= height - paddleHeight && this.paddleDirectionLeft === 1) {
                this.paddleLeft.y(height - paddleHeight);
            } else {
                this.paddleLeft.dy(this.paddleDirectionLeft * this.paddleSpeed);
            }
        },
        checkPaddleCollisions() {
            const ballSize = 20;
            const paddleWidth = 20;
            const paddleHeight = 100;

            const ballLeft = this.ball.cx() - ballSize / 2;
            const ballRight = this.ball.cx() + ballSize / 2;
            const ballTop = this.ball.cy() - ballSize / 2;
            const ballBottom = this.ball.cy() + ballSize / 2;

            // Check collision with left paddle
            if (
                ballLeft <= paddleWidth &&
                ballTop >= this.paddleLeft.y() &&
                ballBottom <= this.paddleLeft.y() + paddleHeight
            ) {
                this.vx = -this.vx; // Reverse the horizontal velocity
            }

            // Check collision with right paddle
            if (
                ballRight >= this.width - paddleWidth &&
                ballTop >= this.paddleRight.y() &&
                ballBottom <= this.paddleRight.y() + paddleHeight
            ) {
                this.vx = -this.vx; // Reverse the horizontal velocity
            }

            // Check collision with left paddle wall
            if (ballLeft <= 0) {
                this.vx = Math.abs(this.vx); // Ensure positive horizontal velocity
            }

            // Check collision with right paddle wall
            if (ballRight >= this.width) {
                this.vx = -Math.abs(this.vx); // Ensure negative horizontal velocity
            }
        }
    }
};
</script>

<style scoped>
.pong {
    min-height: 100vh;
}
</style>