import Vector from './Vector'
import Scene from './Scene'
import { playerCollision } from './Collision'
import Circle from './Circle'

class Ai {
	#isApproaching
	constructor(objects, right = true, settings) {
		this.objects = objects
		this.right = right
		this.#isApproaching = this.right ? () => { return this.objects[0].direction.x >= 0 } : () => { return this.objects[0].direction.x <= 0 }
		this.index = 1 + this.right
		this.paddleStartX = this.right ? (1 - 0.06 + settings.inaccuracy) : (-1 + 0.06 - settings.inaccuracy)
		this.reset()
		this.returnToCenter = settings.center
		this.takeBordersIntoConsideration = settings.border
		this.takeOpponentIntoConsideration = settings.opponent
		this.borders = []
		for (let i = 0; i < 2 + this.takeOpponentIntoConsideration; ++i) {
			this.borders.push(this.objects[3].copy())
		}
		this.borders[0].position = new Vector(0, 2)
		this.borders[1].position = new Vector(0, -2)
		if (this.borders[2]) {
			this.borders[2].position = new Vector(this.right ? (-3 + 0.01) : (3 - 0.01), 0)
		}
	}

	reset() {
		this.sleepCounter = 0
		this.objects[0].style.color = 'white'
		this.playerPrediction = undefined
		this.prediction = undefined
		this.direction = new Vector()
	}

	draw(lineWidth = 0.01) {
		if (!this.playerPrediction) return
		Scene.drawObject(this.playerPrediction)
		Scene.drawDirectionVector(this.playerPrediction.direction, this.playerPrediction.position, this.playerPrediction.style.color, lineWidth)
		if (this.prediction) {
			Scene.drawObject(this.prediction)
			Scene.drawDirectionVector(Vector.scalarMul(this.prediction.direction, -1), this.prediction.position, this.playerPrediction.style.color, lineWidth)
		}
	}

	update() {
		this.sleepCounter -= Scene.deltaTime
		if (this.sleepCounter < 0) {
			this.sleepCounter = 1000
			this.calculatePosition()
		}
		if (this.prediction && this.prediction.position.y >= this.objects[this.index].vertices[0].y && this.prediction.position.y <= this.objects[this.index].vertices[3].y) {
			this.direction.y = 0
		}
	}

	input() {
		return this.direction.y
	}

	#movingAway() {
		if (this.takeOpponentIntoConsideration) {
			this.playerPrediction = this.objects[0].copy()
			const factorToOpponent = Vector.factorToXOf(-this.paddleStartX, this.playerPrediction.position, this.playerPrediction.direction)
			const factor = Vector.factorToXOf(this.paddleStartX, this.playerPrediction.position, this.playerPrediction.direction)

			this.playerPrediction.direction.scalarMul(2 * factorToOpponent - factor)
			this.prediction = this.playerPrediction.copy()
			this.prediction.style.color = this.right ? 'red' : 'green'
			if (this.takeBordersIntoConsideration) {
				playerCollision(this.borders, this.prediction)
			} else {
				this.prediction.position.add(this.prediction.direction)
			}
		} else if (this.returnToCenter) {
			this.playerPrediction = this.objects[0].copy()
			this.prediction = new Circle(0.05)
			this.prediction.style.color = this.right ? 'red' : 'green'
			this.prediction.position.x = this.paddleStartX
		} else {
			return false
		}
		return true
	}

	#approaching() {
		this.playerPrediction = this.objects[0].copy()
		const factor = Vector.factorToXOf(this.paddleStartX, this.playerPrediction.position, this.playerPrediction.direction)
		if (factor < 0) {
			this.playerPrediction = undefined
			return false
		}
		this.playerPrediction.direction.scalarMul(factor)
		this.prediction = this.playerPrediction.copy()
		this.prediction.style.color = this.right ? 'red' : 'green'
		if (this.takeBordersIntoConsideration) {
			playerCollision(this.borders, this.prediction)
		} else {
			this.prediction.position.add(this.prediction.direction)
		}
		return true
	}

	calculatePosition() {
		if (this.#isApproaching()) {
			if (!this.#approaching()) return
		} else {
			if (!this.#movingAway()) return
		}
		if (this.prediction.position.y > 1 || this.prediction.position.y < -1) {
			this.prediction = undefined
		} else {
			this.playerPrediction.style.color = this.right ? 'red' : 'green'
			if (this.prediction.position.y < this.objects[this.index].position.y) {
				this.direction.y = -1
			} else {
				this.direction.y = 1
			}
		}
	}

	static init(array, objects, route, playerName) {
		playerName.value.ai = false
		array.length = 0
		if (route.name !== 'ai') return
		playerName.value.ai = true
		playerName.value.left = 'instruction.you'
		playerName.value.right = 'insruction.you'
		if (route.query.rtype === 'ai') {
			const settings = {
				center: Boolean(route.query.rcenter),
				border: Boolean(route.query.rborder),
				opponent: Boolean(route.query.ropponent),
				inaccuracy: Number(route.query.rinaccuracy) / 500,
			}
			array[0] = new Ai(objects, true, settings)
			playerName.value.right = ''
		}
		if (route.query.ltype === 'ai') {
			const settings = {
				center: Boolean(route.query.lcenter),
				border: Boolean(route.query.lborder),
				opponent: Boolean(route.query.lopponent),
				inaccuracy: Number(route.query.linaccuracy) / 500,
			}
			array[1] = new Ai(objects, false, settings)
			playerName.value.left = ''
		}
	}
}

export default Ai
