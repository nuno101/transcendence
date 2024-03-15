<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import Backend from '../js/Backend';
import Chat from '../js/Chat';
import Channel from '../components/chat/Channel.vue';
import Message from '../components/chat/Message.vue';

const route = useRoute();

const channels = ref([])
const messageInput = ref('')
const targetNickname = ref('')
const createChannelError = ref('')
const sendMessageError = ref('')

onMounted(() => {
    loadChannels();

    // If the route has a channel_id parameter, load the messages for that channel
    // TODO rburgsta: Make work
    if (route.params.id) {
        console.log(route.params.id)
        let channel = Chat.channels.value.find(channel => channel.id === route.params.id)
        if (channel) {
            console.log(channel)
            loadMessages(channel)
        }
    }
})

function loadChannels() {
    let data = Backend.get('/api/users/me/channels')
    data.then(value => {
        Chat.channels.value = value
    }).catch(err => {
        console.log(err)
        Chat.channels.value = []
        // TODO: Display error message
    })
}

function loadMessages(channel) {
    try {
        let data = Backend.get(`/api/channels/${channel.id}/messages`)
        data.then(value => {
            Chat.messages.value = value
            Chat.selected_channel.value = channel
        }).catch(err => {
            console.log(err)
            Chat.messages.value = []
        })
    } catch (err) {
        console.log(err)
        Chat.messages.value = []
        // TODO: Display error message
    }
}

function createChannel() {
    let data = Backend.post(`/api/channels`, {
        nickname: targetNickname.value
    })
    data.then(value => {
        Chat.channels.value.unshift(value)
        createChannelError.value = ''
    }).catch(err => {
        createChannelError.value = err
    })
}

function sendMessage() {
    let channel_id = Chat.selected_channel.value.id
    let data = Backend.post(`/api/channels/${channel_id}/messages`, {
        content: messageInput.value
    })
    data.then(value => {
        messageInput.value = '';
        sendMessageError.value = ''
    }).catch(err => {
        sendMessageError.value = err
    })
}

function deleteMessage(message) {
    let data = Backend.delete(`/api/messages/${message.id}`)
    data.then(value => {
    }).catch(err => {
        console.log(err)
    })
}

</script>

<template>
    <div class="row mb-3">
        <div>
            <div class="input-group create-input-group">
                <input type="text" placeholder="Username of the user you want to DM" class="form-control"
                    v-model="targetNickname" @keyup.enter="createChannel" />
                <button class="btn btn-primary" @click="createChannel">Create</button>
            </div>
            <div v-if="createChannelError !== ''" class="alert alert-danger d-flex align-items-center p-1" role="alert">
                {{ createChannelError }}
            </div>
        </div>

        <!-- Sidebar with channels -->
        <ul class="col-md-3 channel-container list-group">
            <Channel v-for="channel in Chat.channels.value" :key="channel.id" :channel="channel"
                @selected="loadMessages(channel)" />
        </ul>

        <!-- Container for selected channels -->
        <div v-if="Chat.selected_channel.value" class="col-md-8">
            <div class="row">
                <div class="col-md-12">
                    <div class="message-container">
                        <Message v-for="message in Chat.messages.value" :key="message.id" :message="message"
                            @deleted="deleteMessage(message)" />
                    </div>
                    <div>
                        <div class="input-group send-input-group">
                            <input type="text" class="form-control" v-model="messageInput" @keyup.enter="sendMessage" />
                        </div>
                        <div v-if="sendMessageError !== ''" class="alert alert-danger d-flex align-items-center p-1"
                            role="alert">
                            {{ sendMessageError }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.channel-container {
    height: 70vh;
    overflow: auto;
    display: flex;
    flex: 0 0 auto;
}

.message-container {
    height: 70vh;
    overflow: auto;
    display: flex;
    flex: 0 0 auto;
    flex-direction: column-reverse;
}

.send-input-group {
    margin-top: 6px;
}
</style>
