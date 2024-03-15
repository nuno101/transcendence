<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import Backend from '../js/Backend';
import Chat from '../js/Chat';
import { globalUser } from '../main';
import Channel from '../components/chat/Channel.vue';
import Message from '../components/chat/Message.vue';
import UserRow from '../components/common/UserRow.vue'
import GetAvatar from '../components/common/GetAvatar.vue'
const route = useRoute();

const channels = ref([])
const messageInput = ref('')
const targetNickname = ref('')
const createChannelError = ref('')
const messageError = ref('')

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

async function loadChannels() {
    try {
        let data = await Backend.get('/api/users/me/channels')
        Chat.channels.value = data
    } catch (err) {
        console.log(err)
        Chat.channels.value = []
        // TODO: Display error message
    }
}

async function loadMessages(channel) {
    try {
        let data = await Backend.get(`/api/channels/${channel.id}/messages`)
        Chat.messages.value = data
        Chat.selected_channel.value = channel
    } catch (err) {
        console.log(err)
        Chat.messages.value = []
        // TODO: Display error message
    }
}

async function createChannel() {
    try {
        let data = await Backend.post(`/api/channels`, {
            nickname: targetNickname.value
        })
        Chat.channels.value.unshift(data)
        createChannelError.value = ''
    } catch (err) {
        createChannelError.value = err
    }
}

async function sendMessage() {
    let channel_id = Chat.selected_channel.value.id
    try {
        let data = await Backend.post(`/api/channels/${channel_id}/messages`, {
            content: messageInput.value
        })
        messageInput.value = '';
        messageError.value = ''
    } catch (err) {
        messageError.value = err
    }
}

async function deleteMessage(message) {
    try {
        let data = await Backend.delete(`/api/messages/${message.id}`)
    } catch (err) {
        messageError.value = err
    }
}

function getChannelMember() {
    if (Chat.selected_channel.value.members[0].id == globalUser.value.id) {
        return Chat.selected_channel.value.members[1]
    }
    return Chat.selected_channel.value.members[0]
}

</script>

<template>
    <div class="row mb-3">

        <!-- Sidebar with channels -->
        <div class="col-md-3">
            <div class="mb-2">
                <div class="input-group">
                    <input type="text" placeholder="DM user nickname" class="form-control" v-model="targetNickname"
                        @keyup.enter="createChannel" />
                    <button class="btn btn-primary" @click="createChannel">Create</button>
                </div>
                <div v-if="createChannelError !== ''" class="alert alert-danger d-flex align-items-center p-1"
                    role="alert">
                    {{ createChannelError }}
                </div>
            </div>
            <ul class="channel-container list-group">
                <Channel v-for="channel in Chat.channels.value" :key="channel.id" :channel="channel"
                    :selected="channel === Chat.selected_channel.value" @selected="loadMessages(channel)" />
            </ul>
        </div>

        <!-- Container for selected channels -->
        <div v-if="Chat.selected_channel.value" class="col-md-9">
            <div>
                <GetAvatar :id="getChannelMember().id" :size=45 class="avatar" />
                <router-link class="message-author" :to="'/users/' + getChannelMember().id">{{
                        getChannelMember().username
                    }}</router-link>
            </div>
            <div class="message-container">
                <Message v-for="message in Chat.messages.value" :key="message.id" :message="message"
                    @deleted="deleteMessage(message)" />
            </div>
            <div class="mt-2">
                <div class="input-group">
                    <input type="text" class="form-control" v-model="messageInput" @keyup.enter="sendMessage" />
                </div>
                <div v-if="messageError !== ''" class="alert alert-danger d-flex align-items-center p-1" role="alert">
                    {{ messageError }}
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.avatar {
    margin-right: 10px;
}

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
</style>
