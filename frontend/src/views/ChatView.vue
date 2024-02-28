<script>
import Backend from '../js/Backend';
import Channel from '../components/chat/Channel.vue';
import Message from '../components/chat/Message.vue';

export default {
    components: {
        Channel,
        Message,
    },

    data() {
        return {
            messages: [],
            channels: []
        }
    },

    methods: {
        loadChannels() {
            let channels = Backend.get('/api/users/me/channels')
            channels.then(value => {
                this.channels = value
            }).catch(err => {
                console.log(err)
                this.channels = []
                // TODO: Display error message
            })
        },

        loadMessages(channel_id) {
            try {
                let messages = Backend.get(`/api/channels/${channel_id}/messages`)
                messages.then(value => {
                    this.messages = value
                }).catch(err => {
                    console.log(err)
                    this.messages = []
                })
            } catch (err) {
                console.log(err)
                this.messages = []
                // TODO: Display error message
            }
        }
    },

    mounted() {
        this.loadChannels()
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