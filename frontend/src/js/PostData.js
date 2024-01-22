export const PostData = async (posturl, postdata) => {
    const response = await fetch(posturl, {
      method: 'POST',
    //   credentials: 'include',
      body: JSON.stringify(postdata)
    })
    
    if(response.status !== 200) {
      throw new Error('error');
    }

    const data = await response.json();

    return data;
  }