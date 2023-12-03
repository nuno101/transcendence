<script setup>
// import HomeSelection from '../components/dashboard/DashboardChoice.vue';
import { useI18n } from 'vue-i18n';
</script>

<template>
  <div>
    <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
    <h1 class="display-1">{{useI18n().t('tournamentsview.tournaments')}}</h1>

    <button type="button" class="btn btn-primary">New</button>

  </div>
</template>

<style>
</style>
