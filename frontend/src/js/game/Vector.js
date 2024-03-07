class Vector {
	static minFactor = 0.001

	constructor(x = 0.0, y = 0.0) {
		this.x = x
		this.y = y
	}

	copy() {
		return new Vector(this.x, this.y)
	}

	assign(other) {
		this.x = other.x
		this.y = other.y
	}

	add(other) {
		this.x += other.x
		this.y += other.y
	}

	sub(other) {
		this.x -= other.x
		this.y -= other.y
	}

	scalarMul(factor) {
		this.x *= factor
		this.y *= factor
	}

	get length () {
		return Math.sqrt(this.x * this.x + this.y * this.y)
	}

	set length (value) {
		this.normalize()
		this.scalarMul(value)
	}

	normalize() {
		const length = this.length
		if (length === 0) return
		this.x /= length
		this.y /= length
	}

	orthogonal(clockwise = true) {
		return clockwise ? new Vector(-this.y, this.x) : new Vector(this.y, -this.x)
	}

	rotate(angle) {
		const tmp = this.x * Math.cos(angle) - this.y * Math.sin(angle)
		this.y = this.x * Math.sin(angle) + this.y * Math.cos(angle)
		this.x = tmp
	}

	static pow(v, exponent) {
		return new Vector(Math.pow(v.x, exponent), Math.pow(v.y, exponent))
	}

	static mul(v1, v2) {
		return new Vector(v1.x * v2.x, v1.y * v2.y)
	}

	static add(v1, v2) {
		return new Vector(v1.x + v2.x, v1.y + v2.y)
	}

	static sub(v1, v2) {
	    return new Vector(v1.x - v2.x, v1.y - v2.y)
	}

	static scalarMul(v, factor) {
		return new Vector(v.x * factor, v.y * factor)
	}

	static factorToXOf(x, position, direction) {
		if (direction.x === 0) return 0
		return (x - position.x) / direction.x
	}

	static factorToYOf(y, position, direction) {
		if (direction.y === 0) return 0
		return (y - position.y) / direction.y
	}

	static factorsToCircle(CirclePos, CircleRadius, position, direction) {
		const a = Math.pow(direction.x, 2) + Math.pow(direction.y, 2)
		let b = position.x * direction.x + position.y * direction.y - CirclePos.x * direction.x - CirclePos.y * direction.y
		b *= 2
		const c = Math.pow(position.x, 2) + Math.pow(position.y, 2) + Math.pow(CirclePos.x, 2) + Math.pow(CirclePos.y, 2)
		- 2 * CirclePos.x * position.x - 2 * CirclePos.y * position.y - Math.pow(CircleRadius, 2)

		const radicant = Math.pow(b, 2) - 4 * a * c
		if (a === 0) return [] // direction is invalid
		if (radicant < 0) return []
		return [
			(-b + Math.sqrt(radicant)) / (2 * a),
			(-b - Math.sqrt(radicant)) / (2 * a)
		]
	}

	static factorsToMovingCircle(circlePos, circleDir, circleRadius, pointPos, pointDir) {
		const aV = new Vector()
		aV.sub( Vector.mul(circleDir, pointDir) )
		aV.scalarMul(2)
		aV.add(Vector.pow(circleDir, 2))
		aV.add(Vector.pow(pointDir, 2))
		const bV = new Vector()
		bV.add(Vector.mul(pointPos, pointDir))
		bV.sub(Vector.mul(pointPos, circleDir))
		bV.sub(Vector.mul(circlePos, pointDir))
		bV.add(Vector.mul(circlePos, circleDir))
		bV.scalarMul(2)
		const cV = new Vector()
		cV.sub(Vector.mul(circlePos, pointPos))
		cV.scalarMul(2)
		cV.add(Vector.pow(pointPos, 2))
		cV.add(Vector.pow(circlePos, 2))
		const a = aV.x + aV.y
		const b = bV.x + bV.y
		const c = cV.x + cV.y - Math.pow(circleRadius, 2)

		const radicant = Math.pow(b, 2) - 4 * a * c
		if (a === 0) return [] // direction is invalid
		if (radicant < 0) return []
		return [
			(-b + Math.sqrt(radicant)) / (2 * a),
			(-b - Math.sqrt(radicant)) / (2 * a)
		]
	}

	static factorsToPointFromCircle(circlePos, circleDir, circleRadius, pointPos) {
		const aV = new Vector()
		aV.add( Vector.pow(circleDir, 2) )
		const bV = new Vector()
		bV.sub( Vector.mul(pointPos, circleDir) )
		bV.add( Vector.mul(circlePos, circleDir) )
		bV.scalarMul(2)
		const cV = new Vector()
		cV.sub( Vector.mul(pointPos, circlePos) )
		cV.scalarMul(2)
		cV.add( Vector.pow(pointPos, 2) )
		cV.add( Vector.pow(circlePos, 2) )
		const a = aV.x + aV.y
		const b = bV.x + bV.y
		const c = cV.x + cV.y - Math.pow(circleRadius, 2)

		const radicant = Math.pow(b, 2) - 4 * a * c
		if (a === 0) return [] // direction is invalid
		if (radicant < 0) return []
		return [
			(-b + Math.sqrt(radicant)) / (2 * a),
			(-b - Math.sqrt(radicant)) / (2 * a)
		]
	}

	// static helper(posA, dirA, posB, dirB) {
	//     const factorA = (dirA.x)
	//     const factorB = (posA.x + dirA.x * factorA - posB.x) / dirB.x

	//     return [factorA, factorB]
	// }

	static factorsToOther(posA, dirA, posB, dirB) {
		const denominator = dirB.y * dirA.x - dirB.x * dirA.y
		if (denominator === 0) return []
		const numerator = -dirB.y * posA.x + dirB.y * posB.x + dirB.x * posA.y - dirB.x * posB.y
		return [numerator / denominator, 1]
	}

	static factorsToMovingLine(pointPos, pointDir, line) {
		if (line.ab.x === 0 && line.ab.y === 0) return []
		const denominator = line.ab.y * line.dir.x + line.ab.x * pointDir.y - line.ab.x * line.dir.y - line.ab.y * pointDir.x
		if (denominator === 0) return []
		const numerator = line.ab.y * pointPos.x + line.ab.x * line.a.y - line.ab.y * line.a.x - line.ab.x * pointPos.y
		const factor1 = numerator / denominator
		let factor2
		if (line.ab.y !== 0) {
			factor2 = (pointPos.y + pointDir.y * factor1 - line.a.y - line.dir.y * factor1) / line.ab.y
		} else {
			factor2 = (pointPos.x + pointDir.x * factor1 - line.a.x - line.dir.x * factor1) / line.ab.x
		}
		return [factor1, factor2]
	}

	static factorsToEdge(pointPos, pointDir, edgePos, edge, edgeDir) {
		if (edge.x === 0 && edge.y === 0) return []
		const denominator = edge.y * edgeDir.x + edge.x * pointDir.y - edge.x * edgeDir.y - edge.y * pointDir.x
		if (denominator === 0) return []
		const numerator = edge.y * pointPos.x + edge.x * edgePos.y - edge.y * edgePos.x - edge.x * pointPos.y
		const factor1 = numerator / denominator
		let factor2
		if (edge.y !== 0) {
			factor2 = (pointPos.y + pointDir.y * factor1 - edgePos.y - edgeDir.y * factor1) / edge.y
		} else {
			factor2 = (pointPos.x + pointDir.x * factor1 - edgePos.x - edgeDir.x * factor1) / edge.x
		}
		return [factor1, factor2]
	}

	static factorToEdgeDir(edgeDir, edge, direction) {
		const denominator = edge.x * direction.y - edge.y * direction.x
		if (denominator === 0) return 0
		return (edge.x * edgeDir.y - edge.y * edgeDir.x) / denominator
	}

	static factorsCircleToVertex(circlePos, circleDir, circleRadius, vertex, vertexDir) {
		const aV = Vector.mul(vertexDir, circleDir)
		aV.scalarMul(-2)
		aV.add(Vector.pow(vertexDir, 2))
		aV.add(Vector.pow(circleDir, 2))
		const bV = Vector.mul(vertex, vertexDir)
		bV.sub(Vector.mul(vertex, circleDir))
		bV.sub(Vector.mul(vertexDir, circlePos))
		bV.add(Vector.mul(circlePos, circleDir))
		bV.scalarMul(2)
		const cV = Vector.mul(vertex, circlePos)
		cV.scalarMul(-2)
		cV.add(Vector.pow(vertex, 2))
		cV.add(Vector.pow(circlePos, 2))
		const a = aV.x + aV.y
		const b = bV.x + bV.y
		const c = cV.x + cV.y - Math.pow(circleRadius, 2)

		const radicant = Math.pow(b, 2) - 4 * a * c
		if (a === 0) return [] // direction is invalid
		if (radicant < 0) return []
		return [
			(-b + Math.sqrt(radicant)) / (2 * a),
			(-b - Math.sqrt(radicant)) / (2 * a)
		]
	}

	static dotProduct(a, b) {
		return a.x * b.x + a.y * b.y
	}

	static angle(a, b) {
		return Math.acos(this.dotProduct(a, b) / (a.length * b.length))
	}

	static rotate(v, angle) {
		return new Vector(
			v.x * Math.cos(angle) - v.y * Math.sin(angle),
			v.x * Math.sin(angle) + v.y * Math.cos(angle)
		)
	}
}

export default Vector
