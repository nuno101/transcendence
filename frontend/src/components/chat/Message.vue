<script setup>
import { defineProps } from 'vue';
import formatTimestamp from '../../js/TimeFormat';
import GetAvatar from '../common/GetAvatar.vue';
import { globalUser } from '../../main';
import Backend from '../../js/Backend'

const props = defineProps({
  message: Object,
})

async function acceptInvite() {
  let channel_id = props.message.channel_id
  console.log("Hellop")
  try {
    await Backend.post(`/api/channels/${channel_id}/messages`, {
      content: "invite-accept"
    })
    console.log("Hellop")
  } catch (err) {
    // TODO: Visual error handling?
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
          <router-link class="message-author" :to="'/users/' + message.author.id">{{ message.author.username
            }}</router-link>
          <small class="text-muted">{{ formatTimestamp(message.created_at) }}</small>
        </div>
        <!-- TODO: Only display if message belongs to currently logged in user-->
        <button v-if="globalUser.id === message.author.id" class="btn btn-sm btn-danger" @click="$emit('deleted')">
          <i class="bi bi-trash"></i>
        </button>
      </div>
      <div class="card-body message-body">
        <div v-if='message.content === "game-invite"' >
          <div v-if="globalUser.id === message.author.id" class="alert alert-success d-flex align-items-center p-1 mb-0">Invite sent</div>
          <button v-else class="btn btn-primary" @click="acceptInvite">{{ message.author.nickname }} invited you to play
            a game (click to accept and go to the other pc)</button>
        </div>
        <div v-else-if='message.content === "invite-accept"' class="alert alert-success d-flex align-items-center p-1 mb-0">
          <div v-if="globalUser.id === message.author.id">You accepted the invite</div>
          <div v-else>{{ message.author.nickname }} accepted your invite</div>
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
