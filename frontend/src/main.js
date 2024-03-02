import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle' // suffix .min.js is causing bugs for modals
import 'bootstrap-icons/font/bootstrap-icons.css'
import Websocket from './js/Websocket';
import i18n from './plugins/i18n';


// TODO: Move to appropriate files and create event handler for each event
import Notifications from './js/Notifications'

// TODO: Add structure to define a function/event handler for each event that is being
// by the websocket event handler

async function mainHandler(event) {
    console.log(event)

    // TODO: Use Structure here to decide which function to forward the event to


    // TODO: Instead of checking here if the page reload message should be displayed move this
    // functionality into the event handlers for specific events and sites
    // Post Event if event happens not on current page
    if(!Notifications.checkPageAndEvents(window.location.pathname, JSON.parse(event.data).event))
        await Notifications.postNotification(event.data);
}
// ----------------------------------------------------------------------------------------------------

export const globalWS = new Websocket('/api/ws/events', mainHandler);

const app = createApp(App);

// Use the router
app.use(router);

// Use i18n for languages
app.use(i18n);

// Mount the app to the DOM
app.mount('#app');
