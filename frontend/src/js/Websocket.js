import { ref } from "vue";
class Websocket {
    constructor(url, eventhandler) {
      this.ws = new WebSocket('ws://' + window.location.host + url);
      this.m = ref([]);

      this.ws.addEventListener('open', () => {
        console.log('WebSocket connection opened');
      });

      eventhandler(this);
    }

    sendWebSocketMessage(event, payload) {
      const message = JSON.stringify({ event, payload });
      this.ws.send(message);
    }
  }

export default Websocket