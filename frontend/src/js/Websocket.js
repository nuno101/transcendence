class Websocket {
    static ws;

    static initializeWebSocket() {
        // FIXME: Secure websocket (wss://)
      this.ws = new WebSocket('ws://' + window.location.host + '/api/ws/notification');
        // this.ws.onopen
        // this.ws.onmessage
      this.ws.addEventListener('open', () => {
        console.log('WebSocket connection opened');
      });
  
      this.ws.addEventListener('message', (event) => {
        console.log('Message from server:', event.data);
        // Handle WebSocket messages and dispatch actions if using Vuex
      });
    }
  
    static sendWebSocketMessage(event, payload) {
      const message = JSON.stringify({ event, payload });
      this.ws.send(message);
    }
  }

export default Websocket
