import { ref } from 'vue';
import Backend from './Backend';

class Chat {
    static messages = ref([])
    static channels = ref([])
    static selected_channel = ref(null)

    static async createMessage(event) {
        console.log(event) // DEBUG -> TODO: remove
        Chat.messages.value.push(event.payload)

        // Update the channel's updated_at field
        let channel = Chat.channels.value.find(c => c.id === channel_id)
        channel.updated_at = value.created_at

        // Move the channel to the top of the list
        Chat.channels.value = Chat.channels.value.filter(c => c.id !== channel_id)
        Chat.channels.value.unshift(channel)
    }

    static async deleteMessage(event) {
        console.log(event) // DEBUG -> TODO: remove
        let message_id = event.payload.id
        Chat.messages.value = Chat.messages.value.filter(m => m.id !== message_id)
    }
}

export default Chat