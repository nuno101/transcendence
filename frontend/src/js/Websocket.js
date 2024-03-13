import { ref } from "vue";
class Websocket {
  constructor(url, handlerStructure) {
    this.url = url
    this.handlerStructure = handlerStructure
    this.init()
  }

  init() { 
    // FIXME: Replace ws with wss before evaluation
    this.ws = new WebSocket('ws://' + window.location.host + this.url)

    this.ws.addEventListener('message', async (event) => {
      event = JSON.parse(event.data);

      for (const [key, value] of Object.entries(this.handlerStructure)) {
        if (event.event === key) {
          await value(event);
        }
      }
    });
  }

  send(event, payload) {
    const message = JSON.stringify({ event, payload });
    this.ws.send(message);
  }

  reload() {
    this.init()
  }
}

export default Websocket
