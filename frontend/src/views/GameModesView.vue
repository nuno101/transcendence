<script setup>
// import HomeSelection from '../components/dashboard/DashboardChoice.vue';
import { useI18n } from 'vue-i18n';
</script>

<template>
  <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
  <br>
  <router-link to="/game/online">{{useI18n().t('gamemodesview.online')}}</router-link>
  <br>
  <router-link to="/game/onsite">{{useI18n().t('gamemodesview.onsite')}}</router-link>
</template>

<style>
</style>
