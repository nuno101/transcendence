import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';

const app = createApp(App);

// Use the router
app.use(router);

// Mount the app to the DOM
app.mount('#app');