<script setup>
  import { useI18n } from 'vue-i18n';
</script>

// <script>
//   // GET REQUEST
//   import axios from 'axios';
//   export default {
//     data() {
//       return {
//         data: [],
//       };
//     },
//     mounted() {
//       // Make a GET request to your Django backend endpoint
//       // axios.get('http://your-django-backend-api/login')
//       axios.get('/login')
//         .then(response => {
//           // Handle the successful response
//           this.data = response.data;
//           console.log(this.data);
//         })
//         .catch(error => {
//           // Handle errors
//           console.error('Error fetching data:', error);
//         });
//     },
//   };
// </script>

<template>
  <div>
    <h1>{{useI18n().t('loginview.login')}}</h1>
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
