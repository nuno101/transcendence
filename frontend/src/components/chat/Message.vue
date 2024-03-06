<script setup>
import { defineProps, ref } from 'vue';
import formatTimestamp from '../../js/TimeFormat';
import GetAvatar from '../common/GetAvatar.vue';
import UserRow from '../common/GetAvatar.vue';

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
        <button class="btn btn-sm btn-danger" @click="$emit('deleted')">
          <i class="bi bi-trash"></i>
        </button>
      </div>
      <div class="card-body message-body">
        {{ message.content }}
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
