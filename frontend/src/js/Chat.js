import { ref } from 'vue';
import Backend from './Backend';
import Notifications from './Notifications';

class Chat {
    static messages = ref([])
    static channels = ref([])
    static selected_channel = ref(null)

    // cCONF: ChatView websocket event handler functions
    // ----------------------------------------------------------------------------

    static createChannel = async (data) => {
        let channel = data.payload

        this.channels.value.unshift(channel)
    }

    static deleteChannel = async (data) => {
        let channel_id = data.payload.id

        this.channels.value = this.channels.value.filter(c => c.id !== channel_id)
    }

    static createMessage = async (data) => {
        let url = window.location.pathname

        if (url.startsWith("/chat")) {
            let message = data.payload
            let channel_id = message.channel_id

            let selected_channel = this.selected_channel.value
            if (selected_channel && selected_channel.id == channel_id) {
                this.messages.value.unshift(data.payload)
            }

            // Update the channel's updated_at field
            let channel = this.channels.value.find(c => c.id === channel_id)
            channel.updated_at = data.payload.created_at

            // Move the channel to the top of the list
            this.channels.value = this.channels.value.filter(c => c.id !== channel_id)
            this.channels.value.unshift(channel)
        } else {
            await Notifications.post(data);
        }
    }

    static deleteMessage = async (data) => {
        let url = window.location.pathname

        if (url.startsWith("/chat")) {
            let message_id = data.payload.id
            this.messages.value = this.messages.value.filter(m => m.id !== message_id)
        }
    }

    // ----------------------------------------------------------------------------

    
}

export default Chat