import Vector from './Vector'
import Polygon from './Polygon'
import Circle from './Circle'
import Style from './Style'

class Scene {
	static #lastTimeStamp
	static deltaTime
	static oncreate
	static onupdate
	static onkeydown
	static onkeyup
	static onstop
	static canvas
	static width
	static height
	static ctx
	static translate
	static keys
	static #stop
	static #onstopCalled
	static init(canvas, width, height) {
		Scene.canvas = canvas
		Scene.width = width
		Scene.height = height
		Scene.canvas.width = width
		Scene.canvas.height = height
		Scene.ctx = Scene.canvas.getContext('2d', { alpha: false })
		Scene.translate = new Vector(Scene.width / 2, Scene.height / 2)
		Scene.keys = new Set()
		Scene.#stop = false
		Scene.#onstopCalled = false

		Scene.oncreate = () => {}
		Scene.onupdate = () => {}
		Scene.onkeydown = () => {}
		Scene.onkeyup = () => {}
		Scene.onstop = () => {}
		document.addEventListener('keydown', Scene.#onkeydown)
		document.addEventListener('keyup', Scene.#onkeyup)
	}

	static #onkeydown (evt) {
		Scene.keys.add(evt.key.toLowerCase())
		Scene.onkeydown(evt.key.toLowerCase())
	}

	static #onkeyup (evt) {
		Scene.keys.delete(evt.key.toLowerCase())
		Scene.onkeyup(evt.key.toLowerCase())
	}

	static unmount() {
		Scene.stop = true
		document.removeEventListener('keydown', Scene.#onkeydown)
		document.removeEventListener('keyup', Scene.#onkeyup)
	}

	static loop() {
		requestAnimationFrame(Scene.#create)
	}

	static get stop () {
		return Scene.#stop
	}

	static set stop (value) {
		if (Scene.#stop && value === false) requestAnimationFrame(Scene.#continue)
		Scene.#stop = value
		if (value) Scene.#onstopCalled = false
	}

	static #create(timeStamp) {
		Scene.#lastTimeStamp = timeStamp
		Scene.oncreate()
		requestAnimationFrame(Scene.#update)
	}
	static #update(timeStamp) {
		Scene.deltaTime = timeStamp - Scene.#lastTimeStamp
		Scene.#lastTimeStamp = timeStamp
		if (Scene.deltaTime) {
			Scene.onupdate()
		}
		if (Scene.#stop === false) requestAnimationFrame(Scene.#update)
		else if (Scene.#onstopCalled === false) {
			Scene.onstop()
			Scene.#onstopCalled = true
		}
	}

	static #continue(timeStamp) {
		Scene.#lastTimeStamp = timeStamp
		requestAnimationFrame(Scene.#update)
	}
	static clear() {
		Scene.ctx.clearRect(0, 0, Scene.width, Scene.height)
	}
	static transform(v) {
		return new Vector(v.x * Scene.translate.y + Scene.translate.x, v.y * Scene.translate.y + Scene.translate.y)
	}
	static drawLine(a, b, color = 'white', lineWidth = 5, lineDash = [], lineDashOffset = 0) {
		const a1 = Scene.transform(a)
		const b1 = Scene.transform(b)

		Scene.ctx.beginPath()
		Scene.ctx.moveTo(a1.x, a1.y)
		Scene.ctx.lineTo(b1.x, b1.y)
		Scene.ctx.strokeStyle = color
		Scene.ctx.lineWidth = lineWidth
		Scene.ctx.setLineDash(lineDash)
		Scene.ctx.lineDashOffset = lineDashOffset
		Scene.ctx.stroke()
		Scene.ctx.lineDash = []
		Scene.ctx.lineDashOffset = 0
	}
	static drawDirectionVector(direction, position, color = 'white', lineWidth = 5) {
		const sum = position.copy()
		sum.add(direction)
		Scene.drawLine(position, sum, color, lineWidth)
	}
	static drawCircle(position, radius, color = 'white', lineWidth = 5) {
		const position1 = Scene.transform(position)
		const radius1 = radius * Scene.translate.y
		Scene.ctx.beginPath()
		Scene.ctx.moveTo(position1.x + radius1, position1.y)
		Scene.ctx.arc(position1.x, position1.y, radius1, 0, Math.PI * 2, true)
		Scene.ctx.strokeStyle = color
		Scene.ctx.lineWidth = lineWidth
		Scene.ctx.stroke()
	}
	static drawObject(object) {
		if (object instanceof Polygon && object.vertices.length) {
			Scene.ctx.beginPath()
			let point = Scene.transform( object.vertices[0] )
			Scene.ctx.moveTo(point.x, point.y)
			for (let i = 1; i < object.vertices.length; ++i) {
				point = Scene.transform( object.vertices[i])
				Scene.ctx.lineTo( point.x, point.y )
			}
		} else if (object instanceof Circle) {
			const position = Scene.transform(object.position)
			const radius = object.radius * Scene.translate.y
			
			Scene.ctx.beginPath()
			Scene.ctx.moveTo(position.x + radius, position.y)
			Scene.ctx.arc(position.x, position.y, radius, 0, Math.PI * 2, true)
		}
		
		object.style.applyOn(Scene.ctx)
	}

	static normalize(v) {
		v.x -= Scene.translate.x
		v.x /= Scene.translate.y 
		v.y -= Scene.translate.y
		v.y /= Scene.translate.y
	}

	static drawText(text, position, font, style = new Style()) {
		const positionTranslated = Scene.transform(position)

		Scene.ctx.beginPath()
		Scene.ctx.font = font
		Scene.ctx.textAlign = 'center'
		if (style.fillShape) {
			Scene.ctx.fillStyle = style.color
			Scene.ctx.fillText(text, positionTranslated.x, positionTranslated.y)
		} else {
			Scene.ctx.strokeStyle = style.color
			Scene.ctx.strokeText(text, positionTranslated.x, positionTranslated.y)
		}
	}
}

export default Scene
