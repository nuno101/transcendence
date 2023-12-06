<script setup>
import { useI18n } from 'vue-i18n';
import axios from 'axios';
import { onMounted, ref } from 'vue';

const users = ref([]);  // Initialize as a reactive ref
const fetchData = async () => {
  try {
    const response = await axios.get('/api/users');
    console.log(response.data); // Log the response data to the console
    users.value = response.data.users; // Fill users variable with values  
    return response.data;  // Return the data to be used in the template
  } catch (error) {
    console.error('Error fetching data:', error);
    return null;
  }
};
onMounted(() => {
  fetchData();  // Call fetchData when the component is mounted
});
</script>

<template>
  <div>
    <h1>{{useI18n().t('loginview.login')}}</h1>
    <!-- PRINTING ALL USERS TO PAGE ON BROWSER -->
    <!-- <div v-for="user in users" :key="user.id">
      <h2>User Information:</h2>
      <p><strong>ID:</strong> {{ user.id }}</p>
      <p><strong>Name:</strong> {{ user.name }}</p>
      <p><strong>Fullname:</strong> {{ user.fullname }}</p>
    </div> -->
    <h3>42 API</h3>
    <p>or</p>
    <h3>GOOGLE</h3>
    <p>or</p>
    <h3>{{useI18n().t('loginview.email')}}</h3>
    <input type="email" class="form-control" id="email">
    <h3>{{useI18n().t('loginview.password')}}</h3>
    <input type="password" class="form-control" id="password">
    <br>
    <router-link to="/dashboard">
      <button type="button" class="btn btn-success">{{useI18n().t('loginview.login')}}</button>
    </router-link>
  </div>
</template>

<style>
</style>

