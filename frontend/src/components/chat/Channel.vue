<script setup>
import { defineProps } from 'vue';
import formatTimestamp from '../../js/TimeFormat';
import { globalUser } from '../../main';

const props = defineProps({
  channel: Object,
  selected: Boolean
});
</script>

<template>
  <li :class="{ 'active': selected }" class="channel-item list-group-item list-group-item-action py-3 lh-sm"
    @click="$emit('selected')">
    <div class="d-flex w-100 justify-content-between align-items-center">
      <h1 class="mb-1 fs-5">{{ props.channel.members[0].username = globalUser.username ?
        props.channel.members[1].nickname : props.channel.members[0].nickname }}</h1>
    </div>
    <div class="d-flex justify-content-between align-items-center">
      <small>{{ formatTimestamp(props.channel.updated_at) }}</small>
    </div>
  </li>
</template>

<style scoped>
.channel-item {
  cursor: pointer;
}
</style>
