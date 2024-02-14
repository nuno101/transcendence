import Backend from './Backend';

class Friends {
    static acceptRequest = async (friends, friendsAvatar, friendRequests, friendRequestsAvatar, request) => {
        try {
            const acceptedRequest = await Backend.post(`/api/users/me/friends/requests/${request.id}`, {});
            friends.push({"id": `${request.from_user.id}`, "nickname": `${request.from_user.nickname}`});
            friendsAvatar[request.from_user.id] = friendRequestsAvatar[request.from_user.id];
            const indexToDelete = friendRequests.findIndex(friendreq => friendreq.id === request.id);
            if(indexToDelete !== -1){
              friendRequests.splice(indexToDelete, 1);
              console.log(friendRequestsAvatar);
              delete friendRequestsAvatar[request.from_user.id];
              console.log(friendRequestsAvatar);
            }
            console.log(acceptedRequest);
          } catch (err) {
              console.error(err.message);
          }
    };

    static declineCancelDeleteRequest = async(flag, requestArr, requestAvatar, request) => {
        try {
            // .value for FriendsView, without for UserSearch
            const arr = requestArr.value || requestArr; // Check if .value exists, use it if it does
            const avatar = requestAvatar.value || requestAvatar; // Check if .value exists, use it if it does
            if(flag === 'DELETEFRIEND')
                await Backend.delete(`/api/users/me/friends/${request.id}`, {});
            else if (flag === 'DECLINEFRIENDREQ' || flag === 'CANCELPENDREQ')
                await Backend.delete(`/api/users/me/friends/requests/${request.id}`, {});
            const indexToDelete = arr.findIndex(friendreq => friendreq.id === request.id);
            if(indexToDelete !== -1) {
                console.log(arr);
                arr.splice(indexToDelete, 1);
                if(flag === 'DELETEFRIEND')
                delete avatar[request.id];
                else if(flag === 'DECLINEFRIENDREQ')
                delete avatar[request.from_user.id];
                else if(flag === 'CANCELPENDREQ')
                delete avatar[request.to_user.id];
            }
        } catch (err) {
            console.error(err.message);
        }
    };
}

export default Friends
