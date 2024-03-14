import Scene from "./Scene"

const fps = {
	show: false,
	counter: 0,
	value: 0,
	reset: () => {
		fps.timer = 1000
	},
	update: () => {
		fps.timer -= Scene.deltaTime
		if (fps.timer <= 0) {
			fps.reset()
			fps.value = fps.counter
			fps.counter = 0
		} else {
			fps.counter++
		}
	},
	draw: () => {
		if (!fps.show) return
		Scene.ctx.beginPath()
		Scene.ctx.font = '16px Monospace'
		Scene.ctx.fillStyle = 'white'
		Scene.ctx.textAlign = 'center'
		const text = Scene.ctx.measureText(fps.value)
		Scene.ctx.fillText(fps.value, text.width / 2, text.actualBoundingBoxAscent)
	},
}

export default fps
