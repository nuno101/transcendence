<script setup>
import { useI18n } from 'vue-i18n';
import { ref } from 'vue';
import PostRequest from '../common/PostRequest.vue';

const openModal = ref(false);
const submittable = ref(false);
const formData = ref({
  "title": "",
  "description": "",
  "creator_id": "1"
});

const submitForm = () => {
    // Handle the form submission here, e.g., send the data to a server
    openModal.value = false;
    console.log('Form submitted with data:', formData.value);
    console.log('Request Payload:', JSON.stringify(formData.value));
    submittable.value = false;
};

</script>

<template>
<!-- POST:
{"title": "tournament3", "description": "Root user", "creator_id": "1"} -->
  <div>
    <button type="button" class="btn btn-primary" @click="openModal = !openModal">Add new tournament</button>
    <div v-if="openModal === true" class="modal-content">
        <form @submit.prevent="submitForm">
            <div class="form-group">
                <label for="title">Title of Tournament</label>
                <input type="text" class="form-control" id="title" placeholder="Enter title" v-model="formData.title" required>
            </div>
            <div class="form-group">
                <label for="description">Description of Tournament</label>
                <input class="form-control" id="description" placeholder="Enter description" v-model="formData.description" required>
            </div>
            <br>
            <div>
                <button type="button" class="btn btn-danger" @click="openModal = false">Cancel</button>
                <button type="submit" class="btn btn-success" @click="submittable = true">Add Tournament</button>
            </div>   
            <PostRequest v-if="submittable" :apiPath="'/api/tournaments/'" :data='formData'></PostRequest>
        </form>
    </div>
    <!-- MODAL NOT WORKING -->
    <!-- <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">Add new tournament</button> -->
    <!-- <div class="modal" id="exampleModal" tabindex="-1" role="dialog">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
            </div>
        </div>
    </div> -->
  </div>

</template>

<style>
.modal-content {
  background-color: #fff; /* White background for modal content */
  padding: 20px;
  border-radius: 5px; /* Add rounded corners */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); /* Add a subtle shadow */
}
</style>
