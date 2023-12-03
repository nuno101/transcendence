<script setup>
// import HomeSelection from '../components/dashboard/DashboardChoice.vue';
import { useI18n } from 'vue-i18n';
</script>

<template>
  <div>
    <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
    <h1>{{useI18n().t('friendsview.listoffriends')}}</h1>
    <h3>{{useI18n().t('friendsview.friendrequests')}}</h3>
    <h3>{{useI18n().t('friendsview.pendingrequests')}}</h3>
    <router-link to="friends/stats">friends stats example</router-link>
  </div>
</template>

<style>
</style>