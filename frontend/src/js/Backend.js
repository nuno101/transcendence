class Backend {
    static async post(path, postdata) {
        const arg = {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(postdata)
        }
        const respone = await fetch(path, arg)

        if (!respone.ok){
            throw new Error((await respone.json()).error)
        }

        return await respone.json()
    }

    static async get(path) {
        const arg = {
            method: 'GET',
            credentials: 'include'
        }

        const respone = await fetch(path, arg)

        if (!respone.ok) {
            throw new Error((await respone.json()).error) 
        }

        return await respone.json()
    }
}

export default Backend
