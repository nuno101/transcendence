import { ref } from 'vue';
import Backend from './Backend';
class Notifications {
    static messages = ref([]);
    static reloadrequired = ref(false);
    static setupEventListener(ws) {
        ws.ws.addEventListener('message', async (event) => {
            ws.m.value = [...ws.m.value, event.data];
            // Post Event if event happens not on current page
            if(!Notifications.checkPageAndEvents(window.location.pathname, JSON.parse(event.data).event))
                await Notifications.postEvent(event.data);
        });
    }

    /*
        1. event on current page --> alert reload page!, implement event
            "FRIEND" --> FriendsView.vue
            UPDATE_USER (nickname, avatar) --> FriendsView, FriendsStatsView, ...?
    */

    /*
        2. event on other page --> notification:
            - create_friend_request "X sent you a friend request"
            - accept_friend_request "X accepted your friend request"
    */
    static async postEvent(eventData) {
        let requestBody = {};
        requestBody.type = JSON.parse(eventData).event;
        requestBody.content = this.getMessageOfEvent(eventData);

        try {
            if(requestBody.content && requestBody !== ""){
                const response = await Backend.post('/api/users/me/notifications', requestBody);
                this.messages.value = [...this.messages.value, response];
            }
            requestBody.type = requestBody.content = "";
        } catch (err) {
            console.error(err.message);
            // FIXME: ADD ERROR ALERT
        }
    }

    static getMessageOfEvent(eventData) {
        const message = {
            create_friend_request : (JSON.parse(eventData).payload.from_user?.nickname || "") + " sent you a friend request",
            accept_friend_request : (JSON.parse(eventData).payload.to_user?.nickname || "") + " accepted your friend request",
        }
        return message[JSON.parse(eventData).event] || "";
    }

    static checkPageAndEvents(url, event) {
        if (url === '/friends' && ['accept_friend_request', 'create_friend_request', 'decline_friend_request', 'cancel_friend_request', 'remove_friend'].includes(event)) {
            this.reloadrequired.value = true;
            return true;
        }
        return false;
    }
} 
export default Notifications
// if websocket closes --> message> u r offline, ...

// DELETE NOTIFICATIONS!!!