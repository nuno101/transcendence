import Backend from './Backend';

class Friends {
    static acceptRequest = async (friends, friendRequests, request) => {
        try {
            const acceptedRequest = await Backend.post(`/api/users/me/friends/requests/${request.id}`, {});
            friends.push(acceptedRequest);
            const indexToDelete = friendRequests.findIndex(friendreq => friendreq.id === request.id);
            if(indexToDelete !== -1)
              friendRequests.splice(indexToDelete, 1);
          } catch (err) {
              console.error(err.message);
              alert(err.message);
          }
    };

    static declineCancelDeleteRequest = async(flag, requestArr, request) => {
        try {
            if(flag === 'DELETEFRIEND')
                await Backend.delete(`/api/users/me/friends/${request.id}`, {});
            else if (flag === 'DECLINEFRIENDREQ' || flag === 'CANCELPENDREQ')
                await Backend.delete(`/api/users/me/friends/requests/${request.id}`, {});
            const indexToDelete = requestArr.value.findIndex(friendreq => friendreq.id === request.id);
            if(indexToDelete !== -1) {
                requestArr.value.splice(indexToDelete, 1);
            }
        } catch (err) {
            console.error(err.message);
            alert(err.message);
        }
    };
}

export default Friends
