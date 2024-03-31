import { createApp, ref } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle' // suffix .min.js is causing bugs for modals
import 'bootstrap-icons/font/bootstrap-icons.css'
import Websocket from './js/Websocket'
import i18n from './plugins/i18n'
import Chat from './js/Chat'
import Friends from './js/Friends'
import "../src/assets/main.css";

export const globalUser = ref(undefined)

// cCONF: Structure where all event handlers are defined for the global event websocket
const handlersEvent = {
    "create_channel": Chat.createChannel,
    "delete_channel": Chat.deleteChannel,
    "create_message": Chat.createMessage,
    "delete_message": Chat.deleteMessage,
    "create_friend_request" : Friends.createFriendRequest,
    "accept_friend_request" : Friends.acceptFriendRequest,
    "cancel_friend_request" : Friends.cancelFriendRequest,
    "decline_friend_request" : Friends.declineFriendRequest,
    "remove_friend" : Friends.removeFriend
}

// The websocket that will handle all global events
export const globalWS = new Websocket('/api/ws/events', handlersEvent)

const app = createApp(App)

// Use the router
app.use(router)

// Use i18n for languages
app.use(i18n)

// Mount the app to the DOM
app.mount('#app')
