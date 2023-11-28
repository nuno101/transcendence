<script setup>
// import HomeSelection from '../components/dashboard/DashboardChoice.vue';
import { useI18n } from 'vue-i18n';
</script>

<template>
  <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
  <h1>Onsite game</h1>
  <h3>Second player authentication</h3>
</template>

<style>
</style>
