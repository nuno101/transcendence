<script setup>
import { defineProps } from 'vue';
import formatTimestamp from '../../js/TimeFormat';

defineProps({
  channel: Object,
});
</script>

<template>
  <div class="channel-item list-group-item list-group-item-action py-3 lh-sm" @click="$emit('selected')">
    <div class="d-flex w-100 justify-content-between align-items-center">
      <h5 class="mb-1">{{ channel.name }}</h5>
    </div>
    <div class="d-flex justify-content-between align-items-center">
      <small>{{ formatTimestamp(channel.updated_at) }}</small>
    </div>
  </div>
</template>

<style scoped>
.channel-item {
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.channel-item:hover {
  background-color: #f8f9fa;
}
</style>
