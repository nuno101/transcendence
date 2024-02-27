import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle' // suffix .min.js is causing bugs for modals
import 'bootstrap-icons/font/bootstrap-icons.css'
import Websocket from './js/Websocket';
import Notifications from './js/Notifications';
import i18n from './plugins/i18n';

export const globalWS = new Websocket('/api/ws/events', Notifications.setupEventListener);

const app = createApp(App);

// Use the router
app.use(router);

// Use i18n for languages
app.use(i18n);

// Mount the app to the DOM
app.mount('#app');
