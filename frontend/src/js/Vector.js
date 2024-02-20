class Vector {
    constructor(x, y) {
        this.x = x
        this.y = y
    }

    clone() {
        return new Vector(this.x, this.y)
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

    length() {
        return Math.sqrt(this.x * this.x + this.y * this.y)
    }

    normalize() {
        const length = this.length()
        if (length === 0) return
        this.x /= length
        this.y /= length
    }

    static factorToXOf(x, position, direction) {
        if (direction.x === 0) return 0
        return (x - position.x) / direction.x
    }

    static factorToYOf(y, position, direction) {
        if (direction.y === 0) return 0
        return (y - position.y) / direction.y
    }
}

export default Vector