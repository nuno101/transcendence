<template>
    <div class="modal fade" id="playerAuthToggle" aria-hidden="true" aria-labelledby="playerAuthToggleLabel" tabindex="-1">
        <div class="modal-dialog" role="document">
            <div class="modal-content rounded-4 shadow">
            <div class="modal-header p-5 pb-4 border-bottom-0">
                <h1 class="fw-bold mb-0 fs-2"  id="playerAuthToggleLabel">Second Player Authentication</h1>
                <button @click="closeModal" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body p-5 pt-0">
                <div v-for="alert in alerts" :class="alert.type">
                  <div>{{ alert.message }}</div>
                  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" @click="closeModal"></button>
                </div>
                <form @submit.prevent="authenticate" class="">
                <div class="form-floating mb-3">
                    <input v-model="input.username" type="text" class="form-control rounded-3" id="AuthUsername" placeholder="username">
                    <label for="AuthUsername">Username</label>
                </div>
                <div class="form-floating mb-3">
                    <input v-model="input.password" type="password" class="form-control rounded-3" id="AuthPassword" placeholder="Password">
                    <label for="AuthPassword">Password</label>
                </div>
                <SubmitButton :loading="loading">Authenticate</SubmitButton>
                </form>
            </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import Backend from '../../js/Backend'
import SubmitButton from '../common/SubmitButton.vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'

const isAuthenticated = defineModel('isAuthenticated');
const shouldOpenModal = defineModel('shouldOpenModal');
const input = { username: '', password: '' }
const alerts = ref([])
const loading = ref(false)

const openModal = () => {
	bootstrap.Modal.getInstance("#playerAuthToggle").show();
};

const closeModal = () => {
	bootstrap.Modal.getInstance("#playerAuthToggle").hide();
    shouldOpenModal.value = false;
};

onMounted(() => {
    new bootstrap.Modal('#playerAuthToggle', { keyboard: true })
    openModal();
})

const authenticate = async () => {
  try {
    alerts.value = []
    // const response = await Backend.post('/api/login', input)
    isAuthenticated.value = true;
    closeModal();
  } catch (err) {
    alerts.value.push({
      message: err.message,
      type: { 'alert': true, 'alert-danger': true, 'alert-dismissible': true }
    })
  }
}
</script>
