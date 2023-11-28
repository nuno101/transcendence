<script setup>
  // import { useI18n } from 'vue-i18n';
</script>

// <script>
//   // POST REQUEST
//   import axios from 'axios';
//   export default {
//     data() {
//       return {
//         itemName: '',
//       };
//     },
//     methods: {
//       postData() {
//         // Make a POST request to your Django backend endpoint
//         axios.post('http://your-django-backend-api/your-endpoint/', {
//           name: this.itemName,
//         })
//           .then(response => {
//             // Handle the successful response
//             console.log('Item created:', response.data);
//           })
//           .catch(error => {
//             // Handle errors
//             console.error('Error creating item:', error);
//           });
//       },
//     },
//   };
// </script>

// BELONGS IN TEMPLATE TAG
//   <div>
//     <h2>Create New Item:</h2>
//     <form @submit.prevent="postData">
//       <label for="itemName">Item Name:</label>
//       <input type="text" v-model="itemName" required />
//       <button type="submit">Create</button>
//     </form>
//   </div>

<template>
  <div>
    <h1>42 API</h1>
    <h1>GOOGLE</h1>
    <h1>JUST MAIL & PWD</h1>
    <p>After registration with 42 API or Google --> <router-link to="/createprofile">create profile</router-link></p>
  </div>
</template>

<style>
</style>
