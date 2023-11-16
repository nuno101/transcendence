<script setup>
  import { useI18n } from 'vue-i18n';
</script>

<template>
  <div>
      <h1>{{ useI18n().t('register') }}</h1>
      <!-- <h3>Already have an account?</h3>
      <p>use URL "/homepage" to enter the home page or click <a href="/homepage">here</a></p> -->
  </div>
</template>