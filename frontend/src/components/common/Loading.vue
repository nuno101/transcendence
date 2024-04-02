<template>
    <div class="d-flex align-items-center justify-content-center vh-100">
        <div class="spinner-border" role="status">
            <span class="visually-hidden">{{useI18n().t('loading')}}...</span>
        </div>
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n';
</script>