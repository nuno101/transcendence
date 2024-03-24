<template>
    <div class="alert alert-danger" role="alert">
        <strong>{{ i18n.t('ponggameview.unexpectederror') }}:&nbsp;</strong>{{ message }}<br>
        <div v-if="during"><strong>{{ i18n.t('ponggameview.accuredduring') }}:&nbsp;</strong>{{ i18n.t(during) }}</div>
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const props = defineProps(['message', 'during'])
const i18n = useI18n()
</script>
