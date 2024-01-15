<script>
import { ref } from 'vue';
import { useI18n } from 'vue-i18n';

export default {
  props: {
    updateData: Function
  },
  setup(props){
    const i18n = useI18n();
    const submit = ref(false);
    const openModal = ref(false);
    const formData = ref({
      "title": "",
      "description": "",
      "creator_id": "1"
    });
    
    const submitForm = () => {
        // Handle the form submission here, e.g., send the data to a server
        openModal.value = false;
        // console.log('Form submitted with data:', formData.value);
        // console.log('Request Payload:', JSON.stringify(formData.value));
        submit.value = true;
        props.updateData();
    };

    return {
      openModal,
      formData,
      submitForm,
      submit,
      i18n,
      useI18n
    }
  }
}

</script>

<template>
  <div>
    <button type="button" class="btn btn-primary" @click="openModal = !openModal">Add new tournament</button>
    <div v-show="openModal" class="modal-content">
        <form @submit.prevent="submitForm">
            <div class="form-group">
                <label for="title">Title of {{useI18n().t('tournamentsview.tournaments')}}</label>
                <input type="text" class="form-control" id="title" placeholder="Enter title" v-model="formData.title" required>
            </div>
            <div class="form-group">
                <label for="description">Description of Tournament</label>
                <input class="form-control" id="description" placeholder="Enter description" v-model="formData.description" required>
            </div>
            <br/>
            <div>
                <button type="button" class="btn btn-danger" @click="openModal = false">Cancel</button>
                <button type="submit" class="btn btn-success" @click="submitForm">Add Tournament</button>
            </div>   
            <PostRequest v-if="submit" :apiPath="'/api/tournaments/'" :data='formData'></PostRequest>
        </form>
    </div>
  </div>

</template>

<style>

</style>
