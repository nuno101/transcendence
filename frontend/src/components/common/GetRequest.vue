<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';


export default {
  props: {
    apiPath: String
  },
  setup(props, {emit}){
    const data = ref({});

    const fetchData = async (path) => {
      try {
        const response = await axios.get(path);
        console.log(response.data); // Log the response data to the console
        data.value = response.data;  // Set the data to be used in the template
        emit('update:data', data.value);
      } catch (error) {
        console.error('Error fetching data: ', error);
        data.value = null;
      }
    };

    onMounted(() => {
      fetchData(props.apiPath); // Fetch data using the provided API path
    });

    return {
      data
    };
  }
};
</script>

<template>
</template>