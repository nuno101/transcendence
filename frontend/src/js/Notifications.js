import { useI18n } from 'vue-i18n';
import { ref } from 'vue';
import Backend from './Backend';

const parser = {
    "create_message": newMessage,
    "create_friend_request" : newFriendRequest,
    "accept_friend_request" : newFriend,
}

// cCONF: Parser function to generate custom dynamic notification for 
//        different websocket events
// ----------------------------------------------------------------------------

// useI18n().t('settings.nickname')
async function newMessage(data) {
    return {
        type: data.event,
        content: "newMessage"
    }
}

async function newFriendRequest(data) {
    return {
        type: data.event,
        content: "newFriendRequest"
    }
}

async function newFriend(data) {
    return {
        type: data.event,
        content: "newFriends"
    }
}
// ----------------------------------------------------------------------------

async function generateNotification(event) {
    for (const [key, value] of Object.entries(parser)) {
        if (event.event === key) {
            return await value(event);
        }
    }
    return "Parser for event type missing"
}

class Notifications {
    static messages = ref([]);
    static reloadrequired = ref(false);

    static async post(event) {
        let body = await generateNotification(event)

        try {
            const response = await Backend.post('/api/users/me/notifications', body);
            this.messages.value = [...this.messages.value, response];
        } catch (err) {
            console.error(err.message);
            // TODO: ADD ERROR ALERT
        }
    }
} 
export default Notifications