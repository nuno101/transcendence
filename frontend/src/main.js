import { createApp } from 'vue';
import App from './App.vue';
import PostRequest from './components/common/PostRequest.vue';
import GetRequest from './components/common/GetRequest.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle'
import i18n from './plugins/i18n';

const app = createApp(App);

app.component('PostRequest', PostRequest);
app.component('GetRequest', GetRequest);
// Use the router
app.use(router);

// Use i18n for languages
app.use(i18n);

// Mount the app to the DOM
app.mount('#app');
