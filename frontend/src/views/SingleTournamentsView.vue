<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted } from 'vue';

const tournaments = ref([])
const submit = ref(false);
const openModal = ref(false);
const input = defineModel();
input.value = {title: '', description: '', creator_id: '1'};

const fetchData = async () => {
  try {
    tournaments.value = await Backend.get('/api/tournaments/<int:tournament_id>');
    console.log(tournaments.value); // Log the response data to the console
    return tournaments.value;  // Return the data to be used in the template
  } catch (err) {
    console.error(err.message);
  }
};

onMounted(() => {
  fetchData();
})
</script>

<template>
</template>

<style>
</style>
