<script setup>
import { useI18n } from 'vue-i18n';
import GetRequest from '../common/GetRequest.vue';
import { ref } from 'vue';

const data = ref({});

const updatedData = (newData) => {
  data.value = newData;
};

// You can also watch for changes in data
    // watch(data, (newData) => {
    //   console.log('Data changed in parent component:', newData);
    // });
// GetRequest.fetchData("'/api/tournaments");
</script>

<template>
  <div>
    <GetRequest :apiPath="'/api/tournaments/'" @update:data="updatedData"></GetRequest>
    <table class="table table-hover">
        <thead>
            <tr>
              <th scope="col">{{useI18n().t('tournamentsview.tournaments')}}</th>
              <th scope="col">Description</th>
              <th scope="col">Status</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="tournament in data.tournaments" :key="tournament.id">
                <td>{{tournament.title}}</td>
                <td>{{tournament.description}}</td>
                <td v-if="tournament.status === 'registration_open'">
                  <button type="button" class="btn btn-outline-success btn-sm">Register</button>
                </td>
                <td v-else-if="tournament.status === 'registration_closed'">
                    registration closed
                </td>
                <td v-else-if="tournament.status === 'cancelled'">
                    cancelled
                </td>
                <td v-else>
                    {{tournament.status}}
                </td>
            </tr>
        </tbody>
    </table>
    <!-- <router-link to="/dashboard">{{useI18n().t('gobacktodashboard')}}</router-link> -->

    <!-- <button type="button" class="btn btn-primary">New</button> -->

  </div>
</template>

<style>
</style>
