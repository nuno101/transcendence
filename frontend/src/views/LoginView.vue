<script setup>
import { useI18n } from 'vue-i18n';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const users = ref([]);  // Initialize as a reactive ref
const nicknameInput = ref('');
const passwordInput = ref('');
const errorMessage = ref('');
const router = useRouter();

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
  nicknameInput.value = '';
  passwordInput.value = '';
});

const checkUser = () => {
  const existingUser = users.value.find(user => user.name === nicknameInput.value);
  console.log(existingUser);
  console.log(nicknameInput);
  if (existingUser){
    console.log('User is registered');
    // CHECK PASSWORD HERE!
    // const isPasswordTrue = existingUser.password === passwordInput.value;
    // if(isPasswordTrue) {
    //   console.log('Successful login');
      router.push('/dashboard');
    // }
    // else {
    //   console.log('Wrong password!');
    //   errorMessage.value = 'Wrong password, please try again!';
    // }
  } else {
    console.log('User is not registered!');
    errorMessage.value = 'You are not registered, please create your Account first!';
  }
};
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
    <h3>{{useI18n().t('loginview.nickname')}}</h3>
    <input type="text" class="form-control" v-model="nicknameInput" id="nickname">
    <h3>{{useI18n().t('loginview.password')}}</h3>
    <input type="password" class="form-control" v-model="passwordInput" id="password">
    <br>
      <!-- <button @click="checkUser" type="button" class="btn btn-success">{{useI18n().t('loginview.login')}}</button>
    <div v-if="errorMessage" class="alert alert-danger mt-3" role="alert">
      {{ errorMessage }}
    </div> -->
    <router-link to="/dashboard">
      <button type="button" class="btn btn-success">{{useI18n().t('loginview.login')}}</button>
    </router-link>
  </div>
</template>

<style>
</style>



