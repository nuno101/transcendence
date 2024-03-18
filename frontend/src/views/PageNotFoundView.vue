<script setup>
import { useI18n } from 'vue-i18n';
</script>

<template>
    <h1>{{ useI18n().t('notfound.pageNotFound') }}</h1>
    <p>
        {{ useI18n().t('notfound.thisPageIsntAvailable') }} <router-link to="/">home</router-link>
    </p>
</template>

<style>
</style>