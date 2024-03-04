<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import Backend from '../js/Backend';
import Chat from '../js/Chat';
import Channel from '../components/chat/Channel.vue';
import Message from '../components/chat/Message.vue';
import UserRow from '../components/common/UserRow.vue';

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
    <div class="row mb-3 ">
        <!-- Sidebar with channels -->
        <div class="col-md-2">
            <div class="">
                <Channel v-for="channel in channels" :key="channel.id" :channel="channel"
                    @selected="loadMessages(channel)" />
            </div>
        </div>

        <!-- Container for selected channels -->
        <div v-if="selected_channel" class="col-md-8">
            <div class="row">
                <div class="col-md-8">
                    <div class="message-container">
                    <Message v-for="message in messages" :key="message.id" :message="message"
                        @deleted="deleteMessage(message)" /></div>
                    <div class="input-group">
                        <input type="text" class="form-control" v-model="messageInput" @keyup.enter="sendMessage" />
                        <button class="btn btn-primary" @click="sendMessage">Send</button>
                    </div>
                </div>
                <div class="col-md-2 flex">
                    <tr v-for="user in selected_channel.members">
                        <UserRow :user="user" />
                    </tr>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.message-container {
    height: 85vh;
    overflow-y: scroll;
}
</style>