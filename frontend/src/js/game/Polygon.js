import Vector from './Vector'
import Style from './Style'

class Polygon {
    #verticesFromCenter
    #position
    
    constructor(vertices, position = new Vector(), direction = new Vector(), style = new Style) {
        this.#verticesFromCenter = vertices
        
        this.style = style

        this.#position = position
        this.direction = direction
        this.edges = []
        
        for (let i = 0; i < vertices.length; ++i) {
            this.edges.push(Vector.sub(vertices.at(i - 1), vertices.at(i)))
        }
        this.#translate()
    }

    get position() {
        return this.#position
    }

    set position(value) {
        this.#position = value
        this.#translate()
    }

    copy() {
        const verticesCopy = []
        this.#verticesFromCenter.forEach((vertex) => {
            verticesCopy.push(vertex.copy())
        })
        return new Polygon(verticesCopy, this.#position.copy(), this.direction.copy())
    }

    #translate() {
        this.vertices = []
        this.#verticesFromCenter.forEach((vertex) => {
            this.vertices.push(Vector.add(vertex, this.#position))
        })
    }

    intersectionPolygon(polygon) {
        let shortestFactor = 1
        let intersectionDir = []

        this.vertices.forEach((vertex) => {
            polygon.edges.forEach((edge, i) => {
                const factors = Vector.factorsToEdge(vertex, this.direction, polygon.vertices[i], edge, new Vector())

                if (!factors.length) return
                if (factors[0] < Vector.minFactor && factors[0] > -Vector.minFactor) factors[0] = 0
                if (factors[0] >= 1 || factors[0] < 0 || factors[1] >= 1 || factors[1] < 0) return

                const orthogonal = edge.orthogonal(false)
                if (factors[0] === 0 && Vector.dotProduct(this.direction, orthogonal) / (this.direction.length * orthogonal.length) <= 0) {
                    return
                }

                if (factors[0] < shortestFactor) {
                    shortestFactor = factors[0]
                    intersectionDir = []
                    intersectionDir.push(orthogonal)
                } else if (factors[0] !== 1 && factors[0] === shortestFactor) {
                    intersectionDir.push(orthogonal)
                }
            })
        })

        this.edges.forEach((edge, i) => {
            polygon.vertices.forEach((vertex) => {
                const factor = Vector.factorsToEdge(vertex, Vector.scalarMul(this.direction, -1), this.vertices[i], edge, new Vector())

                if (!factor.length) return
                if (factor[0] < Vector.minFactor && factor[0] > -Vector.minFactor) factor[0] = 0
                if (factor[0] >= 1 || factor[0] < 0 || factor[1] >= 1 || factor[1] < 0) return

                const orthogonal = edge.orthogonal(true)
                if (factor[0] === 0 && Vector.dotProduct(this.direction, orthogonal) / (this.direction.length * orthogonal.length) <= 0) {
                    return
                }

                if (factor[0] < shortestFactor) {
                    shortestFactor = factor[0]
                    intersectionDir = [orthogonal]
                } else if (factor[0] === shortestFactor) {
                    intersectionDir.push(orthogonal)
                }
            })
        })

        return { factor: shortestFactor, dir: intersectionDir }
    }

    intersectionCircle(circle) {
        let shortestFactor = 1
        let intersectionDir = []

        this.edges.forEach((edge, i) => {
            const delta = edge.orthogonal(false)
            // delta.normalize()
            // delta.scalarMul(circle.radius) RTODO
            delta.length = circle.radius
            const factors = Vector.factorsToEdge(Vector.add(delta, circle.position), new Vector(), this.vertices[i], edge, this.direction)
            if (!factors.length) return
            if (factors[0] < Vector.minFactor && factors[0] > -Vector.minFactor) factors[0] = 0
            if (factors[0] >= 1 || factors[0] < 0 || factors[1] >= 1 || factors[1] < 0) return

            delta.scalarMul(-1)

            if (factors[0] === 0 && Vector.dotProduct(this.direction, delta) / (this.direction.length * delta.length) <= 0) {
                return
            }

            if (factors[0] < shortestFactor) {
                shortestFactor = factors[0]
                intersectionDir = [delta]
            } else if (factors[0] === shortestFactor) {
                intersectionDir.push(delta)
            }
        })

        this.vertices.forEach((vertex) => {
            const factors = Vector.factorsCircleToVertex(circle.position, new Vector(), circle.radius, vertex, this.direction)

            if (!factors.length) return
            
            let factor = Math.abs(factors[0]) < Math.abs(factors[1]) ? factors[0] : factors[1]

            if (factor < Vector.minFactor && factor > -Vector.minFactor) factor = 0
            if (factor < 0 || factor >= 1) return

            const delta = Vector.scalarMul(this.direction, factor)
            delta.sub(circle.position)
            delta.add(vertex)
            delta.scalarMul(-1)

            if (factor === 0 && Vector.dotProduct(this.direction, delta) / (this.direction.length * delta.length) <= 0) {
                return
            }

            if (factor < shortestFactor) {
                shortestFactor = factor
                intersectionDir = [delta]
            } else if (factor === shortestFactor) {
                intersectionDir.push(delta)
            }
        })

        return { factor: shortestFactor, dir: intersectionDir }
    }
}
export default Polygon
