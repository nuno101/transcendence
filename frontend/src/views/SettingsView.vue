<script setup>
// import HomeSelection from '../components/dashboard/DashboardChoice.vue';
import { useI18n } from 'vue-i18n';
</script>

<template>
  <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
  <h1>{{useI18n().t('settingsview.editprofile')}}</h1>
  <h3>{{useI18n().t('settingsview.nickname')}}</h3>
  <p>(must be unique)</p>
  <h1>{{useI18n().t('settingsview.avatar')}}</h1>
  <h3>{{useI18n().t('settingsview.upload')}}/{{useI18n().t('settingsview.deletecurrent')}}</h3>
  <p>(default option must be provided)</p>
  <button type="button" class="btn btn-success">{{useI18n().t('settingsview.savechanges')}}</button>
</template>

<style>
</style>
