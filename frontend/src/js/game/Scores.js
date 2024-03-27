class Scores {
	static #left
	static #right
	static max = 10
	static onscored = () => {}

    static init(left = 0, right = 0) {
        Scores.#left = left
        Scores.#right = right
    }
	
	static leftScored() {
		Scores.#left++
		Scores.onscored()
	}

	static leftScore() {
		return Scores.#left
	}
	
	static rightScored() {
		Scores.#right++
		Scores.onscored()
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
}

export default Scores
