<script setup>
// import HomeSelection from '../components/dashboard/DashboardChoice.vue';
import { useI18n } from 'vue-i18n';
import GetRequest from '../components/common/GetRequest.vue';
import PostRequest from '../components/common/PostRequest.vue';
import { ref, onMounted } from 'vue';

const data = ref(null);

onMounted(() => {
  data.value = GetRequest.data; //triggers getRequest component to fetch data
});
</script>

<template>
  <div>
    <GetRequest :apiPath="'/api/tournaments/'"></GetRequest>
    <PostRequest
      :apiPath="'/api/tournaments/'"
      :data='`{"title": "tournament5", "description": "Root user", "creator_id": "1"}`'>
    </PostRequest>
    <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
    <h1 class="display-1">{{useI18n().t('tournamentsview.tournaments')}}</h1>

    <!-- <button type="button" class="btn btn-primary">New</button> -->

  </div>
</template>

<style>
</style>
