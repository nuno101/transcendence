import { ref } from "vue";
import Backend from './Backend';
import Notifications from './Notifications';
class Websocket {
    constructor(url) {
      // FIXME: Replace ws with wss before evaluation
      this.ws = new WebSocket('ws://' + window.location.host + url);
      this.m = ref([]);

      this.ws.addEventListener('open', () => {
        console.log('WebSocket connection opened');
      });

      // variable die funktion hält
      const eventListeners = {
        '/api/ws/events': Notifications.setupEventListener,
        // Add more URLs and event listener functions as needed
      };

      const setupEventListener = eventListeners[url];
      if (setupEventListener) {
          setupEventListener(this);
      } else {
        console.log("NO EVENT LISTENER FOUND");
      }
    }

    sendWebSocketMessage(event, payload) {
      const message = JSON.stringify({ event, payload });
      this.ws.send(message);
    }
  }

export default Websocket