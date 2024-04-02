<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted } from 'vue';
import Loading from '../components/common/Loading.vue';
import GetAvatar from '../components/common/GetAvatar.vue';
import { globalUser } from '../main';

const input = ref({ nickname: '', password: ''});
const inputavatar = ref('');
const password2 = ref('');
const useravatar = ref([]);
const isLoaded = ref(false);
let updateErrorMessage = ref('');

onMounted(() => {
	fetchData();
})

const fetchData = async () => {
	try {
		isLoaded.value = false;
		if(globalUser.value !== null)
			useravatar.value = await Backend.getAvatar(`/api/users/${globalUser.value.id}/avatar`);
	} catch (err) {
		console.error(err.message);
	} finally {
		isLoaded.value = true;
	}
};

const submitChanges = async() => {
	try {
		let requestBody = {};
		for (const [key, value] of Object.entries(input.value)){
			if (value !== '')
			requestBody[key] = value;
		}

		if(requestBody !== {})
			await Backend.patch(`/api/users/me`, requestBody);
		if(input.value.nickname !== '') globalUser.value.nickname = input.value.nickname; input.value.nickname = '';
		if(input.value.password !== '') password2.value = input.value.password = '';

		if(inputavatar.value !== ''){
			const formData = new FormData();
			formData.append('avatar', inputavatar.value);

			await Backend.postAvatar('/api/users/me/avatar', formData);
			useravatar.value = await Backend.getAvatar(`/api/users/${globalUser.value.id}/avatar`);
			inputavatar.value = '';
		}
		updateErrorMessage.value = '';
	} catch (err) {
		console.error(err.message);
		updateErrorMessage.value = err.message;
	}    
};

const changeAvatar = async(event) => {
	const file = event.target.files[0];
	if(file){
		if(file.size > 1048576) {
			updateErrorMessage.value = "Avatar is too large";
		} else {
			inputavatar.value = file;
			useravatar.value = URL.createObjectURL(file);
		}
	}
};
</script>

<template>
	<div class="boxstyling">
		<Loading v-if="!isLoaded"/>
		<div v-if="isLoaded && globalUser !== null" class="box rounded scrollbox">
  			<h6 class="text-center fw-bold text-uppercase">{{useI18n().t('header.settings')}}</h6>
			<div class="row">
				<div class="col-sm-4 mt-sm-2">
					<div class="vstack gap-1">
						<div class="text-center mt-2">
							<GetAvatar class="d-sm-none" :id="globalUser.id"/>
							<GetAvatar class="d-none d-sm-inline" :id="globalUser.id" size="100"/>
						</div>
						<div class="text-center">
							<div class="btn-group">
								<label class="btn btn-outline-dark btn-sm rounded fs-md-6" for="avatar">
									{{useI18n().t('settings.changeAvatar')}}
								</label>
								<input type="file" class="form-control d-none" id="avatar" @change="changeAvatar($event, 'Image')" />
							</div>
						</div>
					</div>
				</div>
				<div class="col-sm-8">
					<div class="row">
						<div class="col-6 col-sm-12">
							<div class="form-group row mt-3 align-items-center">
								<label class="col-md-4 col-sm-12 control-label">{{useI18n().t('username')}}</label>
								<div class="col-md-8  col-sm-12">
									<input type="text" class="form-control" :placeholder="globalUser.username" disabled>
								</div>
							</div>
						</div>
						<div class="col-6 col-sm-12">
							<div class="form-group row mt-3 align-items-center">
								<label class="col-md-4 col-sm-12 control-label">{{useI18n().t('nickname')}}</label>
								<div class="col-md-8  col-sm-12">
									<input type="text" class="form-control" :placeholder="globalUser.nickname" v-model="input.nickname">
								</div>
							</div>
						</div>
					</div>
					<div class="form-group row mt-2 mt-sm-3 align-items-center">
						<label class="col-md-4 col-sm-12 control-label">{{useI18n().t('password')}}</label>
						<div class="col-md-8  col-sm-12">
							<input type="password" class="mt-1 form-control" :placeholder="useI18n().t('settings.newPassword')" v-model="input.password">
							<input type="password" class="mt-1 form-control" :placeholder="useI18n().t('settings.confirmNewPassword')" v-model="password2">
							<div v-if="input.password !== password2" class="p-2 mt-1 alert alert-danger" role="alert">
								{{useI18n().t('settings.passwordsDoNotMatch')}}
							</div>
						</div>
					</div>
					<div class=" mt-2 mt-sm-4 text-center text-sm-start">
						<button type="button" class="btn btn-outline-primary" @click="submitChanges" :disabled="input.password !== password2">{{useI18n().t('settings.saveChanges')}}</button>
						<div v-if="updateErrorMessage !== ''" class="p-2 mb-0 mt-1 alert alert-danger" role="alert">
							{{ useI18n().te(`err.${updateErrorMessage}`) ? useI18n().t(`err.${updateErrorMessage}`) :  updateErrorMessage}}
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style>
</style>
