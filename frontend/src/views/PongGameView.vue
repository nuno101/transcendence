<template>
	<div>
		<div class="d-flex justify-content-center">
			<div class="w-100 game-canvas ratio ratio-4x3">
				<canvas ref="canvas"></canvas>
			</div>
		</div>
		<div v-if="showHelp" class="position-absolute top-50 start-50 translate-middle">
			<InstructionInfo :firstplayer="'TODO'" :secondplayer="'TODO'" />
		</div>
	</div>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import Vector from '../js/game/Vector'
import Polygon from '../js/game/Polygon'
import Circle from '../js/game/Circle'
import Scene from '../js/game/Scene'
import Style from '../js/game/Style'
import Scores from '../js/game/Scores'
import fps from '../js/game/fps'
import InstructionInfo from '../components/game/InstructionInfo.vue'

const canvas = ref(null)
const showHelp = ref(true)
const startTimerInitialValue = 1000
let startTimer = startTimerInitialValue
let gameStarted = false
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
const objects = [
	player,
	border.copy(),
	border.copy(),
	border.copy(),
	border.copy(),
]

const playerCollision = (objects, player, depth) => {
	if (depth === undefined) depth = 0

	let intersection = { factor: 1, dir: [] }

	objects.forEach((object) => {
		if (object instanceof Circle) return
		const current = player.intersectionPolygon(object)
		if (current.factor < intersection.factor) {
			intersection = current
		} else if (current.factor === intersection.factor) {
			intersection.dir.push(...current.dir)
		}
	})

	if (depth && intersection.factor === 0) {
		console.warn('player is stuck')
		return
	}
	
	player.position.add(Vector.scalarMul(player.direction, intersection.factor))
	if (intersection.factor === 1) return
	player.direction = Vector.scalarMul(player.direction, 1 - intersection.factor)
	const directionLength = player.direction.length
	const dirDelta = new Vector()
	intersection.dir.forEach((dir) => {
		const factors = Vector.factorsToEdge(player.direction, dir, new Vector(), dir.orthogonal(), new Vector())
		dirDelta.add( Vector.scalarMul(dir, factors[0] * 2) )
	})
	player.direction.add(dirDelta)
	player.direction.length = directionLength

	playerCollision(objects, player, ++depth)
}

const paddleCollision = (objects) => {
	
	objects.forEach((object, i) => {
		if (object instanceof Circle) return

		let intersection = { factor: 1, dir: [] }
		objects.forEach((other) => {
			if (object === other) return
			let current
			if (other instanceof Circle)
				current = object.intersectionCircle(other)
			else if (other instanceof Polygon)
				current = object.intersectionPolygon(other)

			if (current.factor < intersection.factor) {
				intersection = current
			} else if (current.factor === intersection.factor) {
				intersection.dir.push(...current.dir)
			}
		})

		object.position = Vector.add(object.position, Vector.scalarMul(object.direction, intersection.factor))
	})
}

const onscored = () => {
	player.position = new Vector(0, 10)
	player.direction = new Vector(0, 0)
}

const loophook = () => {
	Scene.clear()
	Scene.drawLine(new Vector(0, -1), new Vector(0, 1), 'darkblue', 0.015, [0.025, 0.05], -0.0125)

	if (player.direction.length === 0) {
		startTimer -= Scene.deltaTime
		if (startTimer <= 0) {
			initPlayer(player)
		}
	} else {
		startTimer = startTimerInitialValue
	}

	if (player.position.x < -4 / 3) Scores.rightScored(onscored)
	if (player.position.x > 4 / 3) Scores.leftScored(onscored)
	if (gameStarted && Scores.winner()) {
		gameStarted = false
		endOfGame()
	}

	Scene.drawText(Scores.leftScore(), new Vector(-0.5, -0.5), 0.2, 'Monospace', new Style('darkblue'))
	Scene.drawText(Scores.rightScore(), new Vector(0.5, -0.5), 0.2, 'Monospace', new Style('darkblue'))

	fps.update()
	fps.draw()

	if (gameStarted) paddleInput(Scene.keys, Scene.deltaTime)

	for (let i = 0; i < 3; ++i) {
		Scene.drawObject(objects[i])
	}

	player.direction.length = Scene.deltaTime * playerSpeed
	paddleCollision(objects)
	playerCollision(objects, objects[0])
}

const pausehook = () => {
	Scene.drawText('Paused', new Vector(0, 0), 0.2, 'Monospace')
}

const keyhook = (key) => {
	if (key === ' ') {
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
			Scene.stop = !Scene.stop
		}
		if (!Scene.stop) showHelp.value = false
	}

	if (key === 'f') {
		fps.show = !fps.show
	}

	if (key === 'h') {
		showHelp.value = !showHelp.value
		if (showHelp.value) {
			onscored()
			Scene.stop = true
		}
	}
}

const paddleInput = (keys, deltaTime) => {
	const deltaPaddleSpeed = deltaTime * paddleSpeed
	objects[2].direction.y = deltaPaddleSpeed * keys.has('arrowdown') - deltaPaddleSpeed * keys.has('arrowup')
	objects[1].direction.y = deltaPaddleSpeed * keys.has('s') - deltaPaddleSpeed * keys.has('w')
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

const initGame = () => {
	initPlayer(player)
	Scores.init()
	fps.reset()
	objects[1].position = new Vector(-10 / 3, 0)
	objects[2].position = new Vector(10 / 3, 0)
	objects[3].position = new Vector(0, -2)
	objects[4].position = new Vector(0, 2)
}

const endOfGame = () => {
	console.log('post scores to backend: [', Scores.leftScore(), ':', Scores.rightScore(), ']') // TODO

	objects[1] = border.copy()
	objects[2] = border.copy()
	objects[1].position = new Vector(-10 / 3, 0)
	objects[2].position = new Vector(10 / 3, 0)
}

onMounted(() => {
	initGame()
	Scene.init(canvas.value)
	Scene.onupdate = loophook
	Scene.onkeyup = keyhook
	Scene.onstop = pausehook
	Scene.loop()
})

onUnmounted(() => {
	Scene.unmount()
})
</script>

<style scoped>
.game-canvas {
	max-width: 100vh;
}
</style>
