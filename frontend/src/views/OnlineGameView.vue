<script setup>
import { useI18n } from 'vue-i18n';
</script>

<template>
  <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
  <h1>ONLINE</h1>
  <h3>{{useI18n().t('onlinegameview.inviteuser')}}</h3>
  <h3>{{useI18n().t('onlinegameview.findopponent')}}</h3>
</template>


<style>
/* Add your styles here if needed */
</style>