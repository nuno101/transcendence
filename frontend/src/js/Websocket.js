import { ref } from "vue";
class Websocket {
    constructor(url, eventhandler) {
      // FIXME: Replace ws with wss before evaluation
      this.ws = new WebSocket('ws://' + window.location.host + url);
      this.m = ref([]); // TODO: Where is this used? is this needed?

      this.ws.addEventListener('open', () => {
        console.log('WebSocket connection opened');
      });

      this.ws.addEventListener('message', async (event) => {
        eventhandler(event)
      });
    }

    sendWebSocketMessage(event, payload) {
      const message = JSON.stringify({ event, payload });
      this.ws.send(message);
    }
  }

export default Websocket