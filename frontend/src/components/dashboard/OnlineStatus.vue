<script setup>
import { useI18n } from 'vue-i18n';
import { onMounted, defineProps, watch} from 'vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'

const props = defineProps(['status', 'id']);
const { t, locale } = useI18n();

onMounted(() => {
    if (props.status === 'online' || props.status === 'offline')
        new bootstrap.Tooltip(`#${props.id}`);
        updateTooltip();
})

const updateTooltip = () => {
    if (props.status === 'online' || props.status === 'offline') {
        document.getElementById(props.id)
            .setAttribute('data-bs-original-title', t(props.status));
    }
}

watch(locale, () => {
    updateTooltip();
});
</script>

<template>
    <i v-if="props.status === 'online' || props.status === 'offline'"
        class="ms-2 bi bi-circle-fill align-middle"
        :class="{ 'text-secondary': props.status === 'offline', 'text-success': props.status === 'online' }"
        :id="props.id"
        data-bs-placement="top"
    ></i>
</template>
