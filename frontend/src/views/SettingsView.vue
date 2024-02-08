<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted } from 'vue';

const user = ref([]);
const newNickname = ref('');

onMounted(() => {
  fetchData();
})

const fetchData = async () => {
  try {
    user.value = await Backend.get('/api/users/me');
  } catch (err) {
    console.error(err.message);
  }
};

const submitChanges = async() => {
  console.log("SUBMIT: " + newNickname.value);
  try {
    await Backend.patch(`/api/users/me`, {"nickname": `${newNickname.value}`});
  } catch (err) {
    console.error(err.message);
    console.log(err.response);
    // if (err.response && err.response.status === 400) {
    //         alert("Username is already taken. Please choose a different username.");
    //     } else {
    //         // Handle other errors
    //         alert("An error occurred while updating the username.");
    //     }
    // console.log(err.response.status);
    // STATUS 400 --> username already taken
  }  

  // IF SUCCESSFUL
  newNickname.value = '';
};

</script>

<template>
    <div class="cont">
      <div class="box">
        <div class="row">
            <div class="col-sm-4 mt-4">
                <div class="vstack gap-1">
                    <div class="avatar-circle text-center">
                        <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                            alt="..."
                            class="img-thumbnail rounded"
                            style="width: 100px; height: 100px; object-fit: cover;">
                    </div>
                    <div class="edit-button text-center">
                        <button class="">Update Avatar</button>
                    </div>
                </div>
            </div>
            <div class="col-sm-8 mt-sm-none mt-3">
              <div class="form-group row mt-3 align-items-center">
                  <label class="col-md-3 col-sm-4 col-xs-12 control-label">Nickname</label>
                  <div class="col-md-9 col-sm-8 col-xs-12">
                      <input type="text" class="form-control" :placeholder="user.nickname" v-model="newNickname">
                  </div>
              </div>
              <div class="form-group row mt-3">
                  <label class="col-md-3 col-sm-4 col-xs-12 control-label">Password</label>
                  <div class="col-md-9 col-sm-8 col-xs-12">
                      <!-- <input type="password" class="mt-1 form-control" placeholder="old password"> -->
                      <input type="password" class="mt-1 form-control" placeholder="new password">
                      <input type="password" class="mt-1 form-control" placeholder="confirm new password">
                  </div>
              </div>
              <div class="mt-5 text-center text-sm-start">
              <button type="button" class="btn btn-outline-primary" @click="submitChanges()">Update Profile</button>
              </div>
            </div>
        </div>
      </div>
    </div>
  <h1>{{useI18n().t('settingsview.editprofile')}}</h1>
  <h3>{{useI18n().t('settingsview.nickname')}}</h3>
  <p>(must be unique)</p>
  <h1>{{useI18n().t('settingsview.avatar')}}</h1>
  <h3>{{useI18n().t('settingsview.upload')}}/{{useI18n().t('settingsview.deletecurrent')}}</h3>
  <p>(default option must be provided)</p>
  <button type="button" class="btn btn-success">{{useI18n().t('settingsview.savechanges')}}</button>
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
