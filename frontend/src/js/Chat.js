import { ref } from 'vue';
import Backend from './Backend';

class Chat {
    static messages = ref([])
    static channels = ref([])
    static selected_channel = ref(null)

    static async createMessage(event) {
        console.log(event) // DEBUG -> TODO: remove
    }

    static async deleteMessage(event) {
        console.log(event) // DEBUG -> TODO: remove
    }
}

export default Chat