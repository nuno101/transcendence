class Backend {
    static async post(path, postdata) {
        const arg = {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(postdata)
        }
        const respone = await fetch(path, arg)

        if (!respone.ok) throw new Error(respone.statusText)

        return await respone.json()
    }

    static async get(path) {
        const arg = {
            method: 'GET',
            credentials: 'include'
        }

        const respone = await fetch(path, arg)

        if (!respone.ok) throw new Error(respone.statusText)

        return await respone.json()
    }

    static async delete(path) {
        const arg = {
            method: 'DELETE',
            credentials: 'include'
        };

        const respone = await fetch(path, arg)
        // RESPONE IS EMPTY IN DELETE CASE
        // if (!respone.ok) throw new Error(respone.statusText);
        // return await respone.json()
    }
}

export default Backend