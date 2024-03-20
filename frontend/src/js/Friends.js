import { ref } from 'vue';
import Notifications from './Notifications';
class Friends {
    static friends = ref([]);
    static friendRequests = ref([]);
    static pendingRequests = ref([]);

    static async declineFriendRequest(data) {
        let url = window.location.pathname

        if (url.startsWith("/friends"))
            Friends.pendingRequests.value = Friends.pendingRequests.value.filter(friendreq => friendreq.id !== data.payload.id);
    }

    static async cancelFriendRequest(data) {
        let url = window.location.pathname

        if (url.startsWith("/friends"))
            Friends.friendRequests.value = Friends.friendRequests.value.filter(friendreq => friendreq.id !== data.payload.id);
    }

    static async removeFriend(data) {
        let url = window.location.pathname

        if (url.startsWith("/friends"))
            Friends.friends.value = Friends.friends.value.filter(friend => friend.id !== data.payload.id);
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
            Friends.friends.value.push(Friends.pendingRequests.value.find(friend => friend.id === data.payload.id)?.to_user);
            Friends.pendingRequests.value = Friends.pendingRequests.value.filter(friend => friend.id !== data.payload.id);
        } else {
            await Notifications.post(data);
        }
    }    
}

export default Friends
