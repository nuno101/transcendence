<script setup>
// import HomeSelection from '../components/dashboard/DashboardChoice.vue';
import { useI18n } from 'vue-i18n';
</script>

<template>
  <div>
    <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
    <h1>{{useI18n().t('friendstatsview.profile')}}</h1>
    <h3>{{useI18n().t('friendstatsview.nickname')}} & {{useI18n().t('friendstatsview.avatar')}}</h3>
    <h1>{{useI18n().t('friendstatsview.statistics')}}</h1>
    <h3>{{useI18n().t('friendstatsview.matchhistory')}} (date, final result, opponent)</h3>
    <h3>{{useI18n().t('friendstatsview.winsandlosses')}} ratio or counter</h3>
    <h3>{{useI18n().t('friendstatsview.numberofgames')}}</h3>
  </div>
</template>

<style>
</style>