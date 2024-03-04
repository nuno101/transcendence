<script setup>
import { defineProps } from 'vue';
import GetAvatar from '../common/GetAvatar.vue';
import OnlineStatus from '../dashboard/OnlineStatus.vue';

const props = defineProps({
  user: Object,
  size: {
    type: Number,
    default: 50
  }
});
</script>

<template>
    <td class="bg-light d-none d-lg-table-cell align-middle">
        <GetAvatar :id="props.user.id" :size="props.size" />
    </td>
    <td class="bg-light text-start align-middle">
        <OnlineStatus :status="props.user.status" :id="props.user.id" class="me-2"/>
        <router-link :to="`/users/${props.user.id}`">{{props.user.nickname}}</router-link>
    </td>
</template>