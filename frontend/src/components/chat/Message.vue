<script setup>
import { defineProps } from 'vue';
import formatTimestamp from '../../js/TimeFormat';
import GetAvatar from '../common/GetAvatar.vue';
import { globalUser } from '../../main';

defineProps({
  message: Object,
})

</script>

<template>
  <div class="message">
    <div class="card">
      <div class="card-header message-header d-flex justify-content-between align-items-center">
        <div>
          <GetAvatar :id="message.author.id" :size=35 class="avatar"/>
          <router-link class="message-author" :to="'/users/' + message.author.id">{{ message.author.username }}</router-link>
          <small class="text-muted">{{ formatTimestamp(message.created_at) }}</small>
        </div>
        <!-- TODO: Only display if message belongs to currently logged in user-->
        <button v-if="globalUser.id === message.author.id" class="btn btn-sm btn-danger" @click="$emit('deleted')">
          <i class="bi bi-trash"></i>
        </button>
      </div>
      <div v-if='message.content !== "TODO: I invite you to play a game with me"' class="card-body message-body">
        {{ message.content }}
      </div>
      <div v-else class="card-body message-body">
        <button class="btn btn-primary">Join game invite</button>
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
