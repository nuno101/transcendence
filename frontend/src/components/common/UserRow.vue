<script setup>
import { defineProps } from 'vue';
import GetAvatar from '../common/GetAvatar.vue';
import OnlineStatus from '../dashboard/OnlineStatus.vue';

const props = defineProps({
  user: Object,
  size: {
    type: Number,
    default: 50
  },
  bgColor: {
    type: String,
    default: "bg-light"
  },
  linkColor: {
    type: String,
    default: ""
  },
  avatarStyle: {
    type: String,
    default: "d-none d-lg-table-cell align-middle text-end"
  }
});
</script>

<template>
  <td class="d-lg-none" :class="bgColor"></td>
  <td :class="[avatarStyle, bgColor]">
    <GetAvatar :id="props.user.id" :size="props.size" />
  </td>
  <td class="text-start align-middle" :class="bgColor">
    <OnlineStatus :status="props.user.status" :id="props.user.id" class="me-2" />
    <router-link :class="linkColor" :to="`/users/${props.user.id}`">{{ props.user.nickname }}</router-link>
  </td>
</template>
