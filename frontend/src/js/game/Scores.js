class Scores {
	static #left
	static #right
	static max = 10

    static init() {
        Scores.#left = localStorage.getItem('leftScore') | 0
        Scores.#right = localStorage.getItem('rightScore') | 0
    }
	
	static leftScored(callback) {
		Scores.#left++
		localStorage.setItem('leftScore', Scores.#left.toString())
		Scores.#scored(callback)
	}

	static leftScore() {
		return Scores.#left
	}
	
	static rightScored(callback) {
		Scores.#right++
		localStorage.setItem('rightScore', Scores.#right.toString())
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
        Scores.resetLocalStorage()
	}
    
    static resetLocalStorage() {
        localStorage.setItem('leftScore', '0')
        localStorage.setItem('rightScore', '0')
    }
	
	static #scored(callback) {
        callback()
	}
}

export default Scores
