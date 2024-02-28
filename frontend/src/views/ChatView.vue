<script setup>
import { ref, onMounted } from 'vue';
import Backend from '../js/Backend';
import Channel from '../components/chat/Channel.vue';
import Message from '../components/chat/Message.vue';

const messages = ref([])
const channels = ref([])

onMounted(() => {
    loadChannels();
})

function loadChannels() {
    let data = Backend.get('/api/users/me/channels')
    data.then(value => {
        channels.value = value
    }).catch(err => {
        console.log(err)
        channels.value = []
        // TODO: Display error message
    })
}

function loadMessages(channel_id) {
    try {
        let data = Backend.get(`/api/channels/${channel_id}/messages`)
        data.then(value => {
            messages.value = value
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

</script>

<template>
    <div class="d-flex flex-nowrap">
        <div class="d-flex flex-column align-items-stretch flex-shrink-0 bg-body-tertiary">
            <div class="list-group list-group-flush border-bottom scrollarea">
                <Channel v-for="channel in channels" :channel="channel" @channel-selected="loadMessages(channel.id)" />
            </div>
        </div>
        <div style="display: flex; flex-direction: column;">
            <Message v-for="message in messages" :message="message" />
        </div>
    </div>
</template>