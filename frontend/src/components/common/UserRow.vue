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
  }
});
</script>

<template>
    <td class="d-lg-none" :class="bgColor"></td>
    <td class="d-none d-lg-table-cell align-middle" :class="bgColor">
        <GetAvatar :id="props.user.id" :size="props.size" />
    </td>
    <td class="text-start align-middle" :class="bgColor">
        <OnlineStatus :status="props.user.status" :id="props.user.id" class="me-2"/>
        <router-link :to="`/users/${props.user.id}`">{{props.user.nickname}}</router-link>
    </td>
</template>