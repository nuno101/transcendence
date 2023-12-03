<script setup>
  import { useI18n } from 'vue-i18n';
</script>

<template>
  <div class="d-flex align-items-center justify-content-center vh-100">
    <div class="text-center">
      <router-link to="/registration">{{useI18n().t('homeview.register')}}</router-link>
      <br>
      <router-link to="/login">{{useI18n().t('homeview.alreadyhaveanaccount')}}</router-link>
      <p>use URL "/dashboard" to enter the home page or click <router-link to="/dashboard">here</router-link></p>
    </div>
  </div>
</template>