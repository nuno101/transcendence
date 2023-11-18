<script setup>
  import { useI18n } from 'vue-i18n';
</script>

<template>
  <div>
      <router-link to="/registration">{{ useI18n().t('register') }}</router-link>
      <br>
      <router-link to="/login">Already have an account?</router-link>
  </div>
      <p>use URL "/dashboard" to enter the home page or click <router-link to="/dashboard">here</router-link></p>
</template>