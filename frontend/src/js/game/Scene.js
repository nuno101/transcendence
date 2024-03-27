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
	static onpause
	static oncontinue
	static canvas
	static ctx
	static translate
	static keys
	static #pause
	static #onpauseCalled

	static init(canvas) {
		Scene.canvas = canvas
		Scene.translate = new Vector()
		new ResizeObserver(Scene.resizeObserver).observe(Scene.canvas)

		Scene.ctx = Scene.canvas.getContext('2d', { alpha: false })
		Scene.keys = new Set()
		Scene.#pause = false
		Scene.#onpauseCalled = false

		Scene.oncreate = () => {}
		Scene.onupdate = () => {}
		Scene.onkeydown = () => {}
		Scene.onkeyup = () => {}
		Scene.onpause = () => {}
		Scene.oncontinue = () => {}
		document.addEventListener('keydown', Scene.#onkeydown)
		document.addEventListener('keyup', Scene.#onkeyup)
	}

	static resizeObserver(entries) {
		Scene.width = entries[0].contentRect.width
		Scene.height = entries[0].contentRect.height
	}

	static get width() {
		return Scene.canvas.width
	}

	static get height() {
		return Scene.canvas.height
	}

	static set width(value) {
		Scene.canvas.width = value
		Scene.translate.x = Scene.canvas.width / 2
	}

	static set height(value) {
		Scene.canvas.height = value
		Scene.translate.y = Scene.canvas.height / 2
	}

	static #onkeydown(evt) {
		Scene.keys.add(evt.key.toLowerCase())
		Scene.onkeydown(evt.key.toLowerCase())
	}

	static #onkeyup(evt) {
		Scene.keys.delete(evt.key.toLowerCase())
		Scene.onkeyup(evt.key.toLowerCase())
	}

	static unmount() {
		Scene.pause = true
		document.removeEventListener('keydown', Scene.#onkeydown)
		document.removeEventListener('keyup', Scene.#onkeyup)
	}

	static loop() {
		requestAnimationFrame(Scene.#create)
	}

	static get pause() {
		return Scene.#pause
	}

	static set pause(value) {
		if (Scene.#pause && value === false) requestAnimationFrame(Scene.#continue) 
		Scene.#pause = value
		if (value) Scene.#onpauseCalled = false
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
		if (Scene.#pause === false) requestAnimationFrame(Scene.#update)
		else if (Scene.#onpauseCalled === false) {
			Scene.onpause()
			Scene.#onpauseCalled = true
		}
	}

	static #continue(timeStamp) {
		Scene.#lastTimeStamp = timeStamp
		Scene.oncontinue()	
		requestAnimationFrame(Scene.#update)
	}
	static clear() {
		Scene.ctx.clearRect(0, 0, Scene.width, Scene.height)
	}
	static transform(v) {
		return new Vector(v.x * Scene.translate.y + Scene.translate.x, v.y * Scene.translate.y + Scene.translate.y)
	}
	static drawLine(a, b, color = 'white', lineWidth = 0.01, lineDash = [], lineDashOffset = 0) {
		const a1 = Scene.transform(a)
		const b1 = Scene.transform(b)

		Scene.ctx.beginPath()
		Scene.ctx.moveTo(a1.x, a1.y)
		Scene.ctx.lineTo(b1.x, b1.y)
		Scene.ctx.strokeStyle = color
		Scene.ctx.lineWidth = Scene.translate.y * lineWidth
		for (let i = 0; i < lineDash.length; ++i) {
			lineDash[i] *= Scene.translate.y
		}
		Scene.ctx.setLineDash(lineDash)
		Scene.ctx.lineDashOffset = Scene.translate.y * lineDashOffset
		Scene.ctx.stroke()
		Scene.ctx.lineDash = []
		Scene.ctx.lineDashOffset = 0
	}
	static drawDirectionVector(direction, position, color = 'white', lineWidth = 0.01) {
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

	static drawText(text, position, size, font, style = new Style()) {
		const positionTranslated = Scene.transform(position)

		Scene.ctx.beginPath()
		Scene.ctx.font = (size * Scene.translate.y).toString() + 'px ' + font
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
