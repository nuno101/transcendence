<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import UserSearch from '../components/dashboard/UserSearch.vue';
import { onMounted, ref } from 'vue';

const friends = ref({});
const friendRequests = ref({});
const pendingRequests = ref({});

const fetchData = async () => {
  try {
    friends.value = await Backend.get(`/api/users/me/friends`);
    friendRequests.value = await Backend.get(`/api/users/me/friends/requests?type=received`);
    pendingRequests.value = await Backend.get(`/api/users/me/friends/requests?type=sent`);
  } catch (err) {
    console.error(err.message);
  }
};

const delData = async(flag, id) => {
  let indexToDelete = -1;
  try {
    if (flag === 'FRIEND') {
      await Backend.delete(`/api/users/me/friends/${id}`);
      indexToDelete = friends.value.findIndex(friend => friend.id === id);
      if(indexToDelete !== -1)
        friends.value.splice(indexToDelete, 1);
    }
    else if (flag === 'FRIENDREQ') {
      await Backend.delete(`/api/users/me/friends/requests/${id}`);
      indexToDelete = friendRequests.value.findIndex(friendreq => friendreq.id === id);
      if(indexToDelete !== -1)
        friendRequests.value.splice(indexToDelete, 1);
    }
    else if (flag === 'PENDREQ'){
      await Backend.delete(`/api/users/me/friends/requests/${id}`);
      indexToDelete = pendingRequests.value.findIndex(pendreq => pendreq.id === id);
      if(indexToDelete !== -1)
        pendingRequests.value.splice(indexToDelete, 1);
    }
  } catch(err){
    console.log(err.message);
  }
};

const acceptRequest = async(requestid, username, userid) => {
    try {
      const acceptedRequest = await Backend.post(`/api/users/me/friends/requests/${requestid}`, {});
      friends.value.push({"id": `${userid}`, "username": `${username}`});
      const indexToDelete = friendRequests.value.findIndex(friendreq => friendreq.id === requestid);
      if(indexToDelete !== -1)
          friendRequests.value.splice(indexToDelete, 1);
      console.log(acceptedRequest);
    } catch (err) {
        console.error(err.message);
    }
};

onMounted(() => {
  fetchData();
})
</script>

<template>
    <div class="cont">
      <div class="box">
        <UserSearch :pendingRequests="pendingRequests" :friends="friends" :friendRequests="friendRequests"/>
        <div class="con mt-5">
            <div class="row">
              <div class="col-7">
                <div class="bigtable gamestable rounded img-thumbnail d-md-block">
                <table class="table m-0">
                  <thead class="table-dark">
                    <tr><th colspan="4" class="text-center">{{useI18n().t('friendsview.listoffriends')}}</th></tr>
                  </thead>
                  <tbody v-if="friends && friends.length > 0">
                    <tr v-for="(friend, index) in friends" :key="friend">
                      <td class="bg-light text-center align-middle">{{index + 1}}</td>
                      <td class="bg-light d-none d-lg-table-cell">
                        <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                          alt="..."
                          class="img-thumbnail rounded"
                          style="width: 50px; height: 50px; object-fit: cover;"
                        />
                      </td>
                      <td class="bg-light text-start align-middle">
                        <router-link :to="`/friends/${friend.username}`">{{friend.username}}</router-link>
                      </td>
                      <td class="bg-light text-end align-middle">
                        <button type="button" class="btn btn-outline-danger" aria-label="Close" @click="delData('FRIEND', friend.id)">X</button>
                      </td>
                    </tr>
                  </tbody>
                  <tbody v-else class="text-center">NO FRIENDS</tbody>
                </table>
              </div>
              </div>
              <div class="col-5">
                  <div class="smalltable gamestable rounded img-thumbnail d-md-block">
                     <table class="table table-hover m-0">
                        <thead class="table-dark">
                          <tr><th colspan="4" class="text-center">{{useI18n().t('friendsview.friendrequests')}}</th></tr>
                        </thead>
                      <tbody v-if="friendRequests.length > 0">
                        <tr v-for="friend in friendRequests" :key="friend">
                          <td class="bg-light d-none d-lg-table-cell">
                            <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                              alt="..."
                              class="img-thumbnail rounded"
                              style="width: 50px; height: 50px; object-fit: cover;">
                          </td>
                          <td class="bg-light align-middle">{{friend.from_user.username}}</td>
                          <td class="bg-light text-end align-middle d-none d-md-table-cell">
                            <button class="btn btn-outline-success ms-auto me-2" @click="acceptRequest(friend.id, friend.from_user.username, friend.from_user.id)">✓</button>
                            <button class="btn btn-outline-danger" @click="delData('FRIENDREQ', friend.id)">X</button>
                          </td>
                        </tr>
                      </tbody>
                      <tbody v-else class="text-center">No {{useI18n().t('friendsview.friendrequests')}}</tbody>
                    </table>
                  </div>
                  <div class="mt-2 mt-lg-4 smalltable gamestable rounded img-thumbnail d-md-block">
                     <table class="table table-hover m-0">
                        <thead class="table-dark">
                          <tr><th colspan="3" class="text-center">{{useI18n().t('friendsview.pendingrequests')}}</th></tr>
                        </thead>
                      <tbody v-if="pendingRequests.length > 0">
                        <tr v-for="friend in pendingRequests" :key="friend">
                          <td class="bg-light d-none d-lg-table-cell">
                            <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
                              alt="..."
                              class="img-thumbnail rounded"
                              style="width: 50px; height: 50px; object-fit: cover;">
                          </td>
                          <td class="bg-light align-middle">{{friend.to_user.username}}</td>
                          <td class="bg-light text-end align-middle d-none d-md-table-cell">
                            <button class="btn btn-outline-danger" @click="delData('PENDREQ', friend.id)">X</button>
                          </td>
                        </tr>
                      </tbody>
                      <tbody v-else class="text-center">No {{useI18n().t('friendsview.pendingrequests')}}</tbody>
                    </table>
                  </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  <div>
    <router-link to="friends/stats">friends stats example</router-link>
  </div>
</template>

<style scoped>

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

th {
  position: sticky;
  top: 0;
  z-index: 1;
}

.gamestable {
  overflow-y: scroll;
  padding: 0;
}

.bigtable {
  height: 378px;
}

.smalltable {
  height: 177px;
}

@media (max-width: 991.98px) {
  .bigtable {
    height: 258px;
  }
  .smalltable {
    height: 125px;
  }
}

/* small --> sm */
@media (max-width: 768px) {
  th {
    font-size: smaller;
  }
}
</style>
