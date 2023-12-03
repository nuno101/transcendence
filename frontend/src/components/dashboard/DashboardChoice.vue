<script setup>
import { useI18n } from 'vue-i18n';
</script>

<template>
    <h1 class="text-primary">THIS IS THE {{useI18n().t('dashboardview.dashboard')}}</h1>
    <div>
        <router-link to="/friends">{{useI18n().t('dashboardview.friends')}}</router-link>
        <br>
        <router-link to="/game">{{useI18n().t('dashboardview.playponggame')}}</router-link>
        <br>
        <router-link to="/tournaments">{{useI18n().t('dashboardview.tournaments')}}</router-link>
    </div>
    <div>
        <router-link to="/profile">{{useI18n().t('dashboardview.profile')}}</router-link>
        <br>
        <router-link to="/settings">{{useI18n().t('dashboardview.settings')}}</router-link>
        <br>
        <router-link to="/">{{useI18n().t('dashboardview.logout')}}</router-link>
    </div>
</template>