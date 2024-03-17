<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted } from 'vue';
import Loading from '../components/common/Loading.vue';
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
    if(input.value.nickname !== ''){
      const tmpUser = JSON.parse(localStorage.getItem('globalUser'));
      tmpUser.nickname = globalUser.value.nickname = input.value.nickname;
      localStorage.setItem('globalUser', JSON.stringify(tmpUser));
      input.value.nickname = '';
    }
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
    updateErrorMessage.value = err;
  }    
};

const changeAvatar = async(event) => {
  const file = event.target.files[0];
  if(file){
    inputavatar.value = file;
    useravatar.value = URL.createObjectURL(file);
  }
};
</script>

<template>
    <div class="cont">
      <Loading v-if="!isLoaded"/>
      <div v-if="isLoaded && globalUser !== null" class="box">
        <div class="row">
            <div class="col-sm-4 mt-4">
                <div class="vstack gap-1">
                    <div class="avatar-circle text-center mt-2">
                        <img id="Image"
                            :src="useravatar"
                            alt="..."
                            class="img-thumbnail rounded"
                            style="width: 100px; height: 100px; object-fit: cover;">
                    </div>
                    <div class="text-center">
                        <div class="btn-group">
                            <label class="btn btn-outline-dark btn-sm rounded fs-md-6" for="avatar">
                                Change avatar
                            </label>
                            <input type="file" class="form-control d-none" id="avatar" @change="changeAvatar($event, 'Image')" />
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-sm-8 mt-sm-none mt-3">
              <div class="form-group row mt-3 align-items-center">
                  <label class="col-md-3 col-sm-4 col-xs-12 control-label">Username</label>
                  <div class="col-md-9 col-sm-8 col-xs-12">
                      <input type="text" class="form-control" :placeholder="globalUser.username" disabled>
                  </div>
              </div>
              <div class="form-group row mt-3 align-items-center">
                  <label class="col-md-3 col-sm-4 col-xs-12 control-label">Nickname</label>
                  <div class="col-md-9 col-sm-8 col-xs-12">
                      <input type="text" class="form-control" :placeholder="globalUser.nickname" v-model="input.nickname">
                  </div>
              </div>
              <div class="form-group row mt-3 align-items-center">
                  <label class="col-md-3 col-sm-4 col-xs-12 control-label">Password</label>
                  <div class="col-md-9 col-sm-8 col-xs-12">
                      <input type="password" class="mt-1 form-control" placeholder="new password" v-model="input.password">
                      <input type="password" class="mt-1 form-control" placeholder="confirm new password" v-model="password2">
                      <div v-if="input.password !== password2" class="p-2 mt-1 alert alert-danger" role="alert">
                        Passwords do not match
                      </div>
                  </div>
              </div>
              <div class="mt-5 text-center text-sm-start">
              <button type="button" class="btn btn-outline-primary" @click="submitChanges" :disabled="input.password !== password2">Update Profile</button>
              <div v-if="updateErrorMessage !== ''" class="p-2 mt-1 alert alert-danger" role="alert">
                 {{ updateErrorMessage }}
              </div>
              <!-- ADD SUCCESS MESSAGE? -->
              </div>
            </div>
        </div>
      </div>
    </div>
</template>

<style>
.cont {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  margin-top: 50px;
  height: 100vh;
  width: 100%;
}

.box {
  box-sizing: border-box;
  margin: 0;
  width: 80%;
  padding: 10px 20px;
  padding-bottom: 20px;
  background-color: white;
}
</style>
