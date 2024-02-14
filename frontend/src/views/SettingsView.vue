<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted } from 'vue';
import Loading from '../components/common/Loading.vue';

const input = ref({ nickname: '', password: '' })
const password2 = ref('');
const user = ref([]);
const useravatar = ref([]);
let isUnique = ref(true);
let successful = ref(0); // 0 nothing changed, 1 nickname, 2 password, 3 both
const isLoaded = ref(false);

onMounted(() => {
  fetchData();
})

const fetchData = async () => {
  try {
    isLoaded.value = false;
    user.value = await Backend.get('/api/users/me');
    useravatar.value = await Backend.getAvatar(`/api/users/${user.value.id}/avatar`);
  } catch (err) {
    console.error(err.message);
  } finally {
    isLoaded.value = true;
  }
};

const submitChanges = async() => {
  // REQUESTS CHANGE AVATAR
  // LOOP iterieren, welche ausgeführt werden sollen
  // POST --> 
  try {
    successful.value = 0;
    if(input.value.password !== '' && input.value.nickname !== '') {
      await Backend.patch(`/api/users/me`, {"nickname": `${input.value.nickname}`, "password": `${input.value.password}`});
      user.value.nickname =  input.value.nickname;
      password2.value = input.value.password = input.value.nickname = '';
      isUnique.value = true;
      successful.value = 3;
    } else if (input.value.nickname !== ''){
      await Backend.patch(`/api/users/me`, {"nickname": `${input.value.nickname}`});
      user.value.nickname =  input.value.nickname;
      input.value.nickname = '';
      isUnique.value = true;
      successful.value = 1;
    } else if (input.value.password !== '') {
      await Backend.patch(`/api/users/me`, {"password": `${input.value.password}`});
      password2.value = input.value.password = '';
      successful.value = 2;
    }
  } catch (err) {
    console.log(err.message);
    if (err.message === "Bad Request")
      isUnique.value = false;
  }    
};

const changeAvatar = async(event) => {
  const file = event.target.files[0];
  const formData = new FormData();
  formData.append('avatar', file);
  
  try {
    await Backend.postAvatar('/api/users/me/avatar', formData);
    useravatar.value = await Backend.getAvatar(`/api/users/${user.value.id}/avatar`);
  } catch (err) {
    console.error(err.message);
  }
};
</script>

<template>
    <div class="cont">
      <Loading v-if="!isLoaded"/>
      <div v-if="isLoaded" class="box">
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
                      <input type="text" class="form-control" :placeholder="user.username" disabled>
                  </div>
              </div>
              <div class="form-group row mt-3 align-items-center">
                  <label class="col-md-3 col-sm-4 col-xs-12 control-label">Nickname</label>
                  <div class="col-md-9 col-sm-8 col-xs-12">
                      <input type="text" class="form-control" :placeholder="user.nickname" v-model="input.nickname">
                      <div v-if="!isUnique" class="p-2 mt-1 alert alert-danger" role="alert">
                        Nickname is already taken
                      </div>
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
              <button type="button" class="btn btn-outline-primary" @click="submitChanges()" :disabled="input.password !== password2">Update Profile</button>
              <div v-if="successful > 0" class="p-2 mt-1 alert alert-success" role="alert">
                Successful change of {{ successful === 1 ? "nickname" : successful === 2 ? "password" : "nickname and password" }}
              </div>
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
