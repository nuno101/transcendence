<template>
	<div class="d-flex justify-content-center">
		<div class="position-relative w-100 ratio ratio-4x3 game-canvas">
			<canvas ref="canvas"></canvas>
			<div class="position-absolute d-flex align-items-center justify-content-center">
				<GameError v-if="showGameError" :message="showGameError" :during="showGameLoading"/>
				<GameLoading v-else-if="showGameLoading" :message="showGameLoading"/>
				<GameOver v-else-if="showGameOver" :winner="Scores.winner() === 'left' ? playerName.left : playerName.right" :firstscore="Scores.leftScore()" :secondscore="Scores.rightScore()" :ai="playerName.ai"/>
				<InstructionInfo v-else-if="showHelp" :firstplayer="playerName.left" :secondplayer="playerName.right" :ai="playerName.ai"/>
				<GamePaused v-else-if="showGamePaused" />
			</div>
		</div>
	</div>
</template>

<script setup>
import { onMounted, onUnmounted, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Vector from '../js/game/Vector'
import Polygon from '../js/game/Polygon'
import Circle from '../js/game/Circle'
import Scene from '../js/game/Scene'
import Style from '../js/game/Style'
import Scores from '../js/game/Scores'
import fps from '../js/game/fps'
import Backend from '../js/Backend'
import InstructionInfo from '../components/game/InstructionInfo.vue'
import GameOver from '../components/game/GameOver.vue'
import GamePaused from '../components/game/GamePaused.vue'
import GameLoading from '../components/game/GameLoading.vue'
import GameError from '../components/game/GameError.vue'
import { paddleCollision, playerCollision } from '../js/game/Collision'
import Ai from '../js/game/Ai'
import { globalUser } from '../main'
import { useI18n } from 'vue-i18n'

const canvas = ref(null)
const route = useRoute()
const router = useRouter()
const i18n = useI18n()
const playerName = ref({})
const showGameOver = ref(false)
const showHelp = ref(true)
const showGamePaused = ref(false)
const showGameLoading = ref('')
const showGameError = ref('')
const paddleSpeed = 0.002
const playerSpeed = 0.002
const player = new Circle(0.05)
const paddle = new Polygon([
	new Vector(-0.01, -0.1),
	new Vector(0.01, -0.1),
	new Vector(0.01, 0.1),
	new Vector(-0.01, 0.1),
])
const border = new Polygon([
	new Vector(-2, -1),
	new Vector(2, -1),
	new Vector(2, 1),
	new Vector(-2, 1),
])
const objects = []
const startTimerInitialValue = 1000
let startTimer = startTimerInitialValue
let gameStarted = false
let game
let tournament
let endpoint
const ai = []

const onscored = () => {
	player.position = new Vector(0, 10)
	player.direction = new Vector(0, 0)
}

const draw = () => {
	Scene.clear()
	Scene.drawLine(new Vector(0, -1), new Vector(0, 1), 'darkblue', 0.015, [0.025, 0.05], -0.0125)
	Scene.drawText(Scores.leftScore(), new Vector(-0.5, -0.5), 0.2, 'Monospace', new Style('darkblue'))
	Scene.drawText(Scores.rightScore(), new Vector(0.5, -0.5), 0.2, 'Monospace', new Style('darkblue'))
	for (let i = 0; i < 3; ++i) {
		Scene.drawObject(objects[i])
	}
	fps.draw()
}

const loophook = () => {
	draw()
	fps.update()
	
	if (player.direction.length === 0) {
		startTimer -= Scene.deltaTime
		if (startTimer <= 0) {
			initPlayer(player)
			ai.forEach(e => e.reset())
		}
	} else {
		startTimer = startTimerInitialValue
	}
	
	if (player.position.x < -4 / 3) Scores.rightScored()
	if (player.position.x > 4 / 3) Scores.leftScored()
	if (gameStarted && Scores.winner()) {
		gameStarted = false
		endOfGame()
	}

	if (gameStarted) {
		ai.forEach(e => e.update())
	}

	paddleInput(Scene.keys, Scene.deltaTime)
	
	player.direction.length = Scene.deltaTime * playerSpeed
	paddleCollision(objects)
	playerCollision(objects, objects[0])
}

const pausehook = () => showGamePaused.value = true

const continuehook = () => showGamePaused.value = false

const keyhook = (key) => {
	if (showGameLoading.value || showGameError.value) return
	if (key === ' ') {
		if (showGameOver.value && game) {
			if (tournament) {
				router.push({ path: '/tournaments/' + tournament.id })
			} else {
				router.push({ path: '/game/onsite' })
			}
		}
		showGameOver.value = false
		
		if (!gameStarted) {
			gameStarted = true
			if (Scores.winner()) Scores.reset()
			objects[1] = paddle.copy()
			objects[2] = paddle.copy()
			objects[1].position = new Vector(-1, 0)
			objects[2].position = new Vector(1, 0)
			player.direction = new Vector()
			player.position = new Vector(0, 10)
		} else {
			Scene.pause = !Scene.pause
		}
		if (!Scene.pause) showHelp.value = false
	}

	if (key === 'f') {
		fps.show = !fps.show
	}

	if (key === 'h') {
		showHelp.value = !showHelp.value
		if (gameStarted && showHelp.value && !Scene.pause) {
			onscored()
			draw()
			Scene.pause = true
		}
	}
}

const paddleInput = (keys, deltaTime) => {
	if (!gameStarted) return
	const deltaPaddleSpeed = deltaTime * paddleSpeed
	if (ai[0]) {
		objects[2].direction.y = deltaPaddleSpeed * ai[0].input()
	} else {
		objects[2].direction.y = deltaPaddleSpeed * keys.has('arrowdown') - deltaPaddleSpeed * keys.has('arrowup')
	}
	if (ai[1]) {
		objects[1].direction.y = deltaPaddleSpeed * ai[1].input()
	} else {
		objects[1].direction.y = deltaPaddleSpeed * keys.has('s') - deltaPaddleSpeed * keys.has('w')
	}
}

const initPlayer = (player) => {
	const startLeft = Math.random() < 0.5
	let rotationAngle = -Math.PI * 3 / 8
	rotationAngle += Math.random() * Math.PI * 3 / 4
	rotationAngle += Math.PI * startLeft

	player.position = new Vector(-0.5 + startLeft, Math.random() - 0.5)
	player.direction = new Vector(1, 0)
	player.direction.rotate(rotationAngle)	
}

const isGlobalUserPartOfGame = (game) => {
	if (game.player1.id === globalUser.value.id) return
	if (game.player2.id === globalUser.value.id) return
	throw new Error(i18n.t('ponggameview.wronguser'))
}

const fetchData = async (gameId) => {
	if (!gameId) {
		game = undefined
		endpoint = undefined
		playerName.value.left = undefined
		playerName.value.right = undefined
		showGameLoading.value = ''
		return
	}
	try {
		showGameLoading.value = 'ponggameview.loadingfetch'
		game = await Backend.get('/api/games/' + route.params.id)
		isGlobalUserPartOfGame(game)
		endpoint = '/games/' + game.id
		tournament = game.tournament
		if (game.tournament) {
			endpoint = '/tournaments/' + tournament.id + endpoint
		}
		endpoint = '/api' + endpoint
		playerName.value.left = game.player1.nickname
		playerName.value.right = game.player2.nickname
		showGameLoading.value = ''
	} catch (err) {
		showGameError.value = err.message
		console.error(err.message)
	}
}

const initGame = async () => {
	await fetchData(route.params.id)
	initPlayer(player)
	if (game) {
		Scores.init(game.player1_score, game.player2_score)
	} else {
		Scores.init()
	}
	Scores.onscored = onscored
	showGameOver.value = Scores.winner() !== undefined
	showHelp.value = true
	showGamePaused.value = false
	startTimer = startTimerInitialValue
	gameStarted = false
	fps.reset()
	objects[0] = player
	objects[1] = border.copy()
	objects[2] = border.copy()
	objects[3] = border.copy()
	objects[4] = border.copy()
	objects[1].position = new Vector(-10 / 3, 0)
	objects[2].position = new Vector(10 / 3, 0)
	objects[3].position = new Vector(0, -2)
	objects[4].position = new Vector(0, 2)
}

const onmounted = async () => {
	await initGame()
	Ai.init(ai, objects, route, playerName)
	Scene.init(canvas.value)
	Scene.onupdate = loophook
	Scene.onkeyup = keyhook
	Scene.onpause = pausehook
	Scene.oncontinue = continuehook
	Scene.loop()
}

const sendData = async () => {
	if (!endpoint) {
		showGameLoading.value = ''
		return
	}
	const scores = {
		player1_score: Scores.leftScore(),
		player2_score: Scores.rightScore()
	}
	try {
		game = await Backend.patch(endpoint, scores)
		showGameLoading.value = ''
	} catch (err) {
		showGameError.value = err.message
		console.error(err.message)
	}
}

const endOfGame = () => {	
	objects[1] = border.copy()
	objects[2] = border.copy()
	objects[1].position = new Vector(-10 / 3, 0)
	objects[2].position = new Vector(10 / 3, 0)

	showGameLoading.value = 'ponggameview.loadingsend'
	sendData()
	showGameOver.value = true
}

const onunmounted = Scene.unmount

watch(route, () => {
	onunmounted()
	onmounted()
})

onMounted(onmounted)
onUnmounted(onunmounted)
</script>

<style scoped>
.game-canvas {
	max-width: 100vh;
}
</style>
