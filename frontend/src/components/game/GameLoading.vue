<template>
    <div class="alert alert-primary" role="alert">
        <div class="text-center d-flex align-items-center">
            <div class="pe-3">{{ i18n.t(message) }}</div>
            <div class="spinner-border spinner-border-sm" role="status">
                <span class="visually-hidden">{{i18n.t('loading')}}...</span>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const props = defineProps(['message'])
const i18n = useI18n()
</script>
