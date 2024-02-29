<script setup>
import { useI18n } from 'vue-i18n';
import { getCurrentInstance, onMounted, defineProps, ref} from 'vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'

const instance = getCurrentInstance();
const props = defineProps(['status']);

const reference = ref(null);

onMounted(() => {
    // if(props.status === 'online')
        new bootstrap.Tooltip(reference.value);
    // else if(props.status === 'offline')
    //     new bootstrap.Tooltip(offRef.value);
})

</script>

<template>
    <!-- <i v-if="props.status === 'online'" class="ms-2 bi bi-circle-fill align-middle text-success"
        data-bs-toggle="tooltip" data-bs-placement="top"
        title="online" :ref="reference"
    ></i>
    <i v-if="props.status === 'offline'" class="ms-2 bi bi-circle-fill align-middle text-secondary"
    data-bs-toggle="tooltip" data-bs-placement="top"
    title="offline" :ref="reference"
    ></i> -->
</template>