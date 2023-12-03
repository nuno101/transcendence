<script setup>
// import HomeSelection from '../components/dashboard/DashboardChoice.vue';
import { useI18n } from 'vue-i18n';
</script>

<template>
  <div class="home">
    <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
    <h1>{{useI18n().t('profileview.myprofile')}}</h1>
    <h3>{{useI18n().t('profileview.nickname')}} & {{useI18n().t('profileview.avatar')}}</h3>
    <h1>{{useI18n().t('profileview.statistics')}}</h1>
    <h3>{{useI18n().t('profileview.matchhistory')}} (date, final result, opponent)</h3>
    <h3>{{useI18n().t('profileview.winsandlosses')}} ratio or counter</h3>
    <h3>{{useI18n().t('profileview.numberofgames')}}</h3>
  </div>
</template>

<style>
</style>
