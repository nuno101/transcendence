<template>
    <div class="alert alert-primary fs-1" role="alert">
        <strong>{{ i18n.t('ponggameview.paused') }}</strong>
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
const i18n = useI18n()
</script>
