import Backend from './Backend';
import { ref } from 'vue';
import Notifications from './Notifications';
class Friends {
    static friends = ref([]);
    static friendRequests = ref([]);
    static pendingRequests = ref([]);

    // websockeet functions
    static async declineFriendRequest(data) {
        let url = window.location.pathname

        if (url.startsWith("/friends")) {
            const indexToDelete = Friends.pendingRequests.value.findIndex(friendreq => friendreq.id === data.payload.id);
            if(indexToDelete !== -1) {
                Friends.pendingRequests.value.splice(indexToDelete, 1);
            }
        }
        // else {
        //     await Notifications.post(data);
        // }
    }

    static async cancelFriendRequest(data) {
        let url = window.location.pathname

        if (url.startsWith("/friends")) {
            const indexToDelete = Friends.friendRequests.value.findIndex(friendreq => friendreq.id === data.payload.id);
            if(indexToDelete !== -1) {
                Friends.friendRequests.value.splice(indexToDelete, 1);
            }
        }
        // else {
        //     await Notifications.post(data);
        // }
    }

    static async removeFriend(data) {
        let url = window.location.pathname

        if (url.startsWith("/friends")) {
            const indexToDelete = Friends.friends.value.findIndex(friendreq => friendreq.id === data.payload.id);
            if(indexToDelete !== -1) {
                Friends.friends.value.splice(indexToDelete, 1);
            }
        }
        // else {
        //     await Notifications.post(data);
        // }
    }

    static async createFriendRequest(data) {
        let url = window.location.pathname

        if (url.startsWith("/friends")) {
            Friends.friendRequests.value.push(data.payload);
        } else {
            await Notifications.post(data);
        }
    }

    static async acceptFriendRequest(data) {
        let url = window.location.pathname

        if (url.startsWith("/friends")) {
            const indexToDelete = Friends.pendingRequests.value.findIndex(friendreq => friendreq.id === data.payload.id);
            if(indexToDelete !== -1) {
                Friends.friends.value.push(Friends.pendingRequests.value[indexToDelete].to_user); //what needs to be pushed here???
                Friends.pendingRequests.value.splice(indexToDelete, 1);
            }
        } else {
            await Notifications.post(data);
        }
    }
    
    // other functions
    
}

// Friends.js?t=1710021097442:54 {id: 310, from_user: {…}, to_user: {…}, created_at: '2024-03-09 21:52:17.373550+00:00'}

export default Friends
