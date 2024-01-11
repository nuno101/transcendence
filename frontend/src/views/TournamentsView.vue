<script setup>
import { useI18n } from 'vue-i18n';
// import PostRequest from '../components/common/PostRequest.vue';
import TournamentsTable from '../components/dashboard/TournamentsTable.vue';
import AddTournament from '../components/dashboard/AddTournament.vue';
// import { ref, onMounted } from 'vue';

// const data = ref(null);

// onMounted(() => {
//   data.value = GetRequest.data; //triggers getRequest component to fetch data
// });

// const formData = {
//   "title": "testtournament",
//   "description": "renadom descri",
//   "creator_id": "1"
// };
</script>

<template>
  <div>
    <!-- <GetRequest :apiPath="'/api/tournaments/'"></GetRequest> -->
    <!-- <PostRequest
      :apiPath="'/api/tournaments/'"
      :data='formData'>
    </PostRequest> -->
    <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link>
    <TournamentsTable />
    <AddTournament />
  </div>
</template>

<style>
</style>
