<script setup>
import { useI18n } from 'vue-i18n'
import { defineProps } from 'vue';
import formatTimestamp from '../../js/TimeFormat';
import GetAvatar from '../common/GetAvatar.vue';
import { globalUser } from '../../main';
import Backend from '../../js/Backend'

const i18n = useI18n()
const props = defineProps({
  message: Object,
})

async function acceptInvite() {
  let channel_id = props.message.channel_id
  try {
    await Backend.post(`/api/channels/${channel_id}/messages`, {
      content: "invite-accept"
    })
  } catch (err) {
    console.error(err)
  }
}
</script>

<template>
  <div class="message">
    <div class="card">
      <div class="card-header message-header d-flex justify-content-between align-items-center">
        <div>
          <GetAvatar :id="message.author.id" :size=35 class="avatar" />
          <router-link class="message-author" :to="'/users/' + message.author.id">{{ message.author.nickname
            }}</router-link>
          <small class="text-muted">{{ formatTimestamp(message.created_at) }}</small>
        </div>
        <button v-if="globalUser.id === message.author.id" class="btn btn-sm btn-danger" @click="$emit('deleted')">
          <i class="bi bi-trash"></i>
        </button>
      </div>
      <div class="card-body message-body">
        <div v-if='message.content === "game-invite"' >
          <div v-if="globalUser.id === message.author.id" class="alert alert-success d-flex align-items-center p-1 mb-0">{{i18n.t('chatview.inviteSent')}}</div>
          <button v-else class="btn btn-primary" @click="acceptInvite">{{ message.author.nickname }} {{i18n.t('chatview.invitedYouToPlay')}}</button>
        </div>
        <div v-else-if='message.content === "invite-accept"' class="alert alert-success d-flex align-items-center p-1 mb-0">
          <div v-if="globalUser.id === message.author.id"> {{i18n.t('chatview.youAcceptedTheInvite')}}</div>
          <div v-else>{{ message.author.nickname }}  {{i18n.t('chatview.acceptedYourInvite')}}</div>
        </div>
        <div v-else>
          {{ message.content }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.avatar {
  margin-right: 10px;
}

.message {
  margin-bottom: 10px;
}

.message-header {
  padding: 5px 10px;
}

.message-author {
  margin-right: 10px;
}

.message-body {
  padding: 5px 10px;
}
</style>
