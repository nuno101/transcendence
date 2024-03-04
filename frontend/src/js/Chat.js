import { ref } from 'vue';
import Backend from './Backend';

class Chat {
    static async createMessage(event) {
        console.log(event)
    }

    static async deleteMessage(event) {
        console.log(event)
    }
}

export default Chat