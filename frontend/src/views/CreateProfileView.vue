<script setup>
import { useI18n } from 'vue-i18n';
</script>

<template>
  <div>
    <h1>{{useI18n().t('createprofileview.createprofile')}}</h1>
    <h3>{{useI18n().t('createprofileview.nickname')}}</h3>
    <p>(must be unique)</p>
    <h3>{{useI18n().t('createprofileview.uploadavatar')}}</h3>
    <p>(default option must be provided)</p>
    <router-link to="/">
      <button type="button" class="btn btn-success">{{useI18n().t('createprofileview.createaccount')}}</button>
    </router-link>  </div>
</template>

<style>
</style>
