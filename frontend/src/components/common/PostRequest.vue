<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';

const postData = ref(null);
const props = defineProps(['apiPath', 'data']);

const sendData = async() => {
    try {
        const response = await axios.post(props.apiPath, props.data);
        console.log(response.data);
        postData.value = response.data;
    } catch (error) {
        console.error('Error sending data: ', error);
        postData.value = null;
    }
}

onMounted(() => {
  sendData(); // Automatically send data when the component is mounted
});
</script>

<template>
</template>