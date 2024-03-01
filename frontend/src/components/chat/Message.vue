<script setup>
import { defineProps } from 'vue';
import formatTimestamp from '../../js/TimeFormat';
import { ref } from 'vue';

defineProps({
  message: Object,
})

</script>

<template>
  <div class="message">
    <div class="card">
      <div class="card-header message-header d-flex justify-content-between align-items-center">
        <div>
          <strong class="message-author">{{ message.author.username }}</strong> 
          <small class="text-muted">{{ formatTimestamp(message.created_at) }}</small>
        </div>
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
.message {
  margin-bottom: 10px;
}

.message-author {
  margin-right: 10px;
}
</style>
