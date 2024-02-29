<script setup>
import { useI18n } from 'vue-i18n';
import { onMounted, defineProps, ref, watch} from 'vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'

const props = defineProps(['status', 'id']);

onMounted(() => {
    if (props.status === 'online' || props.status === 'offline')
        new bootstrap.Tooltip(`#${props.id}`);
})

</script>

<template>
    <i v-if="props.status === 'online' || props.status === 'offline'" class="ms-2 bi bi-circle-fill align-middle"
        :class="{ 'text-secondary': props.status === 'offline', 'text-success': props.status === 'online' }"
        :id="props.id" data-bs-placement="top" :title="props.status"
    ></i>
</template>