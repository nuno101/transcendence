<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';

const data = ref(null);
const props = defineProps(['apiPath']);

const fetchData = async (path) => {
  try {
    const response = await axios.get(path);
    console.log(response.data); // Log the response data to the console
    data.value = response.data;  // Set the data to be used in the template
  } catch (error) {
    console.error('Error fetching data: ', error);
    data.value = null;
  }
};

onMounted(() => {
  fetchData(props.apiPath); // Fetch data using the provided API path
});
</script>

<template>
</template>