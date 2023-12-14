<script setup>
import { useI18n } from 'vue-i18n';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const users = ref([]);  // Initialize as a reactive ref
const nicknameInput = ref('');
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
});

const checkUser = () => {
  const existingUser = users.value.find(user => user.name === nicknameInput.value);
  console.log(existingUser);
  console.log(nicknameInput);
  if (existingUser){
    console.log('Nickname is not unique');
    errorMessage.value = 'Nickname is already taken. Please choose a different nickname.';
  } else {
    console.log('Nickname is unique');
    // POST TO /USERS
    router.push('/');
  }
};
</script>

<template>
  <div>
    <h1>{{useI18n().t('createprofileview.createprofile')}}</h1>
    <h3>{{useI18n().t('createprofileview.nickname')}}</h3>
    <input type="text" class="form-control" v-model="nicknameInput" id="nickname">
    <p>(must be unique)</p>
    <h3>{{useI18n().t('createprofileview.uploadavatar')}}</h3>
    <p>(default option must be provided)</p>
    <div class="mb-3">
      <label for="formFile" class="form-label">Upload your avatar</label>
      <input class="form-control" type="file" id="formFile" accept="image/*">
    </div>
    <button @click="checkUser" type="button" class="btn btn-success">{{useI18n().t('createprofileview.createaccount')}}</button>
    <div v-if="errorMessage" class="alert alert-danger mt-3" role="alert">
      {{ errorMessage }}
    </div>
  </div>
</template>

<style>
</style>
