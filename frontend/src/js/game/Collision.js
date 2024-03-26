import Circle from './Circle'
import Polygon from './Polygon'
import Vector from './Vector'

export const playerCollision = (objects, player, depth) => {
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

export const paddleCollision = (objects) => {
	for (let i = 1; i < 3; ++i) {
		let intersection = { factor: 1, dir: [] }
		objects.forEach((other) => {
			if (objects[i] === other) return
			let current
			if (other instanceof Circle)
				current = objects[i].intersectionCircle(other)
			else if (other instanceof Polygon)
				current = objects[i].intersectionPolygon(other)

			if (current.factor < intersection.factor) {
				intersection = current
			} else if (current.factor === intersection.factor) {
				intersection.dir.push(...current.dir)
			}
		})

		objects[i].position = Vector.add(objects[i].position, Vector.scalarMul(objects[i].direction, intersection.factor))
	}
}
