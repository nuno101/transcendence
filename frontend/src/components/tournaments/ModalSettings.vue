
<script setup>
import { useI18n } from 'vue-i18n';
import { ref, onMounted, defineProps } from 'vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'
import router from '../../router';

//const closingTime = defineModal('closingTime')
//const selectedOption = defineModal('selectedOption')

</script>

<template>
				<div class="modal fade" id="RegistrationSetting" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="RegistrationSettingModal" aria-hidden="true">
					<div class="modal-dialog">
						<div class="modal-content">
							<div class="modal-header">
								<h1 class="modal-title fs-5" id="RegistrationSettingModal">Choose tYOhe registrHEYation settings</h1>
								<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
							</div>
							<div class="modal-body">
								<!-- Option 1: Close registration manually -->
								<div class="form-check">
            						<input class="form-check-input" type="radio" id="option1" name="registrationOption" value="option1" v-model="selectedOption">
            						<label class="form-check-label" for="option1">Close registration manually</label>
        						</div>

								<div class="form-check">
									<input class="form-check-input" type="radio" id="option2" name="registrationOption" value="option2" v-model="selectedOption" @change="updateClosingTime">
									<label class="form-check-label" for="option2">Set a closing time for registrations</label>
								</div>

								<div v-if="selectedOption === 'option2'">
									<label for="closingTime">Closing Time:</label>
									<input type="datetime-local" id="closingTime" v-model="closingTime">
								</div>

								<!-- Confirm and Cancel buttons -->
								<div class="mt-3">
									<button type="button" class="btn btn-primary" @click="confirm">Confirm</button>
									<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
								</div>	
							</div>
						</div>
					</div>
				</div>		


</template>