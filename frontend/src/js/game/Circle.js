import Vector from './Vector'
import Style from './Style'

class Circle {
    constructor(radius, position = new Vector(), direction = new Vector(), style = new Style) {
        this.radius = radius
        this.position = position
        this.direction = direction
        this.style = style
    }

    copy() {
        return new Circle(this.radius, this.position.copy(), this.direction.copy(), this.color, this.fill)
    }

    intersectionPolygon(polygon) {
        let shortestFactor = 1
        let intersectionDir = []

        polygon.edges.forEach((edge, i) => {
            const delta = edge.orthogonal(false)
            // delta.normalize()
            // delta.scalarMul(this.radius) RTODO
            delta.length = this.radius
            const factors = Vector.factorsToEdge(Vector.add(delta, this.position), this.direction, polygon.vertices[i], edge, new Vector())
            if (!factors.length) return
            if (factors[0] < Vector.minFactor && factors[0] > -Vector.minFactor) factors[0] = 0
            if (factors[0] >= 1 || factors[0] < 0 || factors[1] >= 1 || factors[1] < 0) return
            if (factors[0] === 0 && Vector.dotProduct(this.direction, delta) / (this.direction.length * delta.length) <= 0) {
                return
            }

            if (factors[0] < shortestFactor) {
                shortestFactor = factors[0]
                intersectionDir = []
                intersectionDir.push(delta)
            } else if (factors[0] !== 1 && factors[0] === shortestFactor) {
                intersectionDir.push(delta)
            }
        })

        polygon.vertices.forEach((vertex) => {
            const factors = Vector.factorsCircleToVertex(this.position, this.direction, this.radius, vertex, new Vector())

            if (!factors.length) return

            let factor = Math.abs(factors[0]) < Math.abs(factors[1]) ? factors[0] : factors[1]

            if (factor < Vector.minFactor && factor > -Vector.minFactor) factor = 0
            if (factor < 0 || factor >= 1) return

            const delta = Vector.scalarMul(this.direction, -factor)
            delta.sub(this.position)
            delta.add(vertex)
            if (factor === 0 && Vector.dotProduct(this.direction, delta) / (this.direction.length / delta.length) <= 0) return
            
            if (factor < shortestFactor) {
                shortestFactor = factor
                intersectionDir = []
                intersectionDir.push(delta)
            } else if (factor !== 1 && factor === shortestFactor) {
                intersectionDir.push(delta)
            }
        })

        return { factor: shortestFactor, dir: intersectionDir }
    }
}

export default Circle
