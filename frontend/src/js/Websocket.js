import { ref } from "vue";
class Websocket {
  constructor(url, distributorStructure) {
    // FIXME: Replace ws with wss before evaluation
    this.ws = new WebSocket('ws://' + window.location.host + url);

    this.ws.addEventListener('open', () => {
      console.log('WebSocket connection opened');
    });

    this.ws.addEventListener('message', async (event) => {
      event = JSON.parse(event.data);
      console.log(event) // TODO: Debug -> remove

      for (const [key, value] of Object.entries(distributorStructure)) {
        if (event.event === key) {
          await value(event);
        }
      }
    });
  }

  sendWebSocketMessage(event, payload) {
    const message = JSON.stringify({ event, payload });
    this.ws.send(message);
  }
}

export default Websocket