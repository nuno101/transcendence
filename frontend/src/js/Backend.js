class Backend {
    static async post(path, postdata) {
        const arg = {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json' // Specify the content type as JSON
            },
            body: JSON.stringify(postdata)
        }
        const respone = await fetch(path, arg)

        if(!respone.ok){
            let error = (await respone.json()).error;
            // OBJECT EXAMPLE: {username: ["User with this Username already exists."]}
            // STRING EXAMPLE:Friend request already sents
            if(typeof error === 'string')
                throw new Error(error);

            const propertyNames = Object.keys(error);
            let messages = '';
            for(let i = 0; i < propertyNames.length; i++)
                messages += ('\n' + error[propertyNames[i]][0]);

            throw new Error(messages);
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

    static async patch(path, patchData) {
        const arg = {
            method: 'PATCH',
			headers: {
				'Content-Type': 'application/json',
			  },
            credentials: 'include',
            body: JSON.stringify(patchData),
        };
        const respone = await fetch(path, arg);

        if (!respone.ok) {
            throw new Error((await respone.json()).error);
        }

        return await respone.json();
    }

    static async delete(path) {
        const arg = {
            method: 'DELETE',
            credentials: 'include'
        };
        const respone = await fetch(path, arg)
        
        if (!respone.ok) {
            throw new Error((await respone.json()).error) 
        }
    }

    // AVATAR FUNCTIONS
    static async getAvatar(path) {
        const arg = {
            method: 'GET',
            credentials: 'include'
        }

        const respone = await fetch(path, arg)
        
        // FOR AVATAR: If redirected, return the redirection URL
        if (respone.redirected) {
            return respone.url;
        }

        if (!respone.ok) {
            throw new Error((await respone.json()).error) 
        }

        return await respone.json()
    }

    static async postAvatar(path, postdata) {
        const arg = {
            method: 'POST',
            credentials: 'include',
            body: postdata
        }
        const respone = await fetch(path, arg)

        if (!respone.ok){
            throw new Error((await respone.json()).error)
        }

        return await respone.json()
    }
}

export default Backend
