class Style {
    constructor(color = 'white', fillShape = true, lineWidth = 5) {
        this.color = color
        this.fillShape = fillShape
        this.lineWidth = lineWidth
    }

    applyOn(ctx) {
        if (this.fillShape) {
            ctx.fillStyle = this.color
            ctx.fill()
        } else {
            ctx.strokeStyle = this.color
            ctx.lineWidth = this.lineWidth
            ctx.closePath()
            ctx.storke()
        }
    }
}

export default Style
