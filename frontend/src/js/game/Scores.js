class Scores {
	static #left
	static #right
	static max = 10

    static init(left = 0, right = 0) {
        Scores.#left = left
        Scores.#right = right
    }
	
	static leftScored(callback) {
		Scores.#left++
		Scores.#scored(callback)
	}

	static leftScore() {
		return Scores.#left
	}
	
	static rightScored(callback) {
		Scores.#right++
		Scores.#scored(callback)
	}

	static rightScore() {
		return Scores.#right
	}

	static winner() {
		if (Scores.#left > Scores.max) return 'left'
		if (Scores.#right > Scores.max) return 'right'
	}
	
	static reset() {
		Scores.#left = 0
		Scores.#right = 0
	}
	
	static #scored(callback) {
        callback()
	}
}

export default Scores
