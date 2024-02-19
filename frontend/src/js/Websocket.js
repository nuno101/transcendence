import { ref } from "vue";
class MyWebSocket {
    static ws;
    static m = ref([]);

    static initializeWebSocket() {
        // FIXME: Secure websocket (wss://)
      this.ws = new WebSocket('ws://' + window.location.host + '/api/ws/notification');
        // this.ws.onopen
        // this.ws.onmessage
      this.ws.addEventListener('open', () => {
        console.log('WebSocket connection opened');
      });
  
      this.ws.addEventListener('message', (event) => {
        // console.log('Message from server:', event.data);
        this.m.value = [...this.m.value, event.data];
        // console.log(this.m.value);
      });
    }
  
    static sendWebSocketMessage(event, payload) {
      const message = JSON.stringify({ event, payload });
      this.ws.send(message);
    }
  }

export default MyWebSocket
