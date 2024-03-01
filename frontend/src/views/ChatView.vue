<script setup>
import { ref, onMounted } from 'vue';
import Backend from '../js/Backend';
import Channel from '../components/chat/Channel.vue';
import Message from '../components/chat/Message.vue';
import { useRoute } from 'vue-router';

const route = useRoute();

const messages = ref([])
const channels = ref([])
const selected_channel = ref(null)
const messageInput = ref('')

onMounted(() => {
    loadChannels();
    
    // If the route has a channel_id parameter, load the messages for that channel
    if (route.params.id) {
        console.log(route.params.id)
        let channel = channels.value.find(channel => channel.id === route.params.id)
        if (channel) {
            console.log(channel)
            loadMessages(channel)
        }
    }
})

function loadChannels() {
    // TODO: Error checking
    let data = Backend.get('/api/users/me/channels')
    data.then(value => {
        channels.value = value
    }).catch(err => {
        console.log(err)
        channels.value = []
        // TODO: Display error message
    })
}

function loadMessages(channel) {
    try {
        let data = Backend.get(`/api/channels/${channel.id}/messages`)
        data.then(value => {
            messages.value = value.reverse()
            selected_channel.value = channel
        }).catch(err => {
            console.log(err)
            messages.value = []
        })
    } catch (err) {
        console.log(err)
        messages.value = []
        // TODO: Display error message
    }
}

function sendMessage() {
    let channel_id = selected_channel.value.id
    // TODO: error handling
    let data = Backend.post(`/api/channels/${channel_id}/messages`, {
        content: messageInput.value
    })
    data.then(value => {
        console.log(value)
        messages.value.push(value)

        // Update the channel's updated_at field
        let channel = channels.value.find(c => c.id === channel_id)
        channel.updated_at = value.created_at
        
        // Move the channel to the top of the list
        channels.value = channels.value.filter(c => c.id !== channel_id)
        channels.value.unshift(channel)

        // Clear the input field after sending message
        messageInput.value = '';
    }).catch(err => {
        console.log(err)
    })
}

function deleteMessage(message) {
    let data = Backend.delete(`/api/messages/${message.id}`)
    data.then(value => {
        console.log(value)
        messages.value = messages.value.filter(m => m.id !== message.id)
    }).catch(err => {
        console.log(err)
    })
}

</script>

<template>
    <div class="d-flex">
        <!-- Sidebar with channels -->
        <div class="d-flex flex-column align-items-stretch flex-shrink-0 bg-light">
            <div class="list-group list-group-flush border-bottom scrollarea">
                <Channel v-for="channel in channels" :key="channel.id" :channel="channel"
                    @selected="loadMessages(channel)" />
            </div>
        </div>

        <!-- Main area with messages (will not grow larger than height of site) and is scrollable -->
        <div class="d-flex flex-column flex-grow-1 ms-3">
            <div class="flex-grow-1 overflow-auto">
                <Message v-for="message in messages" :key="message.id" :message="message" 
                    @deleted="deleteMessage(message)" />
            </div>
            <div class="input-group">
                <input type="text" class="form-control" v-model="messageInput" @keyup.enter="sendMessage" />
                <button class="btn btn-primary" @click="sendMessage">Send</button>
            </div>
        </div>

        <!-- Right sidebar with user list -->
        <div v-if="selected_channel" class="d-flex flex-column align-items-stretch flex-shrink-0 bg-light">
            <div class="list-group list-group-flush border-bottom scrollarea">
                <div v-for="user in selected_channel.members" :key="user.id" class="list-group-item list-group-item-action py-3 lh-sm">
                    <div class="d-flex w-100 justify-content-between align-items-center">
                        <h5 class="mb-1">{{ user.username }}</h5>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
