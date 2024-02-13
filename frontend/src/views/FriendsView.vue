<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import Helpers from '../js/Helpers';
import UserSearch from '../components/dashboard/UserSearch.vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'
import { onMounted, ref } from 'vue';
import Loading from '../components/common/Loading.vue';

const friends = ref({});
const friendsAvatar = ref({});
const friendRequests = ref({});
const friendRequestsAvatar = ref({});
const pendingRequests = ref({});
const pendingRequestsAvatar = ref({});

const modalFlag = ref('');
const modalId = ref('');

const isLoaded = ref(false);


const fetchData = async () => {
  try {
    friends.value = await Backend.get(`/api/users/me/friends`);
    friendRequests.value = await Backend.get(`/api/users/me/friends/requests?type=received`);
    pendingRequests.value = await Backend.get(`/api/users/me/friends/requests?type=sent`);
    console.log(pendingRequests.value);
	for (const friend of friends.value) {
		const avatarUrl = await Helpers.getAvatarById(friend.id);
		friendsAvatar.value[friend.id] = avatarUrl;
	}
	for (const f of friendRequests.value) {
		const avatarUrl = await Helpers.getAvatarById(f.from_user.id);
		friendRequestsAvatar.value[f.from_user.id] = avatarUrl;
	}
	for (const p of pendingRequests.value) {
		const avatarUrl = await Helpers.getAvatarById(p.to_user.id);
		pendingRequestsAvatar.value[p.to_user.id] = avatarUrl;
	}
  } catch (err) {
    console.error(err.message);
  } finally {
	  isLoaded.value = true;
  }
};

const openModal = async(flag, id) => {
	modalFlag.value = flag;
	modalId.value = id;
	bootstrap.Modal.getInstance("#friendsModalToggle").show();
};

const closeModal = async() => {
	bootstrap.Modal.getInstance("#friendsModalToggle").hide();
};

const delData = async(flag, id) => {
  let indexToDelete = -1;
  try {
    if (flag === 'FRIEND') {
      await Backend.delete(`/api/users/me/friends/${id}`);
      indexToDelete = friends.value.findIndex(friend => friend.id === id);
      if(indexToDelete !== -1)
        friends.value.splice(indexToDelete, 1);
		delete friendsAvatar.value[id];
    }
    else if (flag === 'FRIENDREQ') {
      await Backend.delete(`/api/users/me/friends/requests/${id}`);
      indexToDelete = friendRequests.value.findIndex(friendreq => friendreq.id === id);
      if(indexToDelete !== -1){
		friendRequests.value.splice(indexToDelete, 1);
		delete friendRequestsAvatar.value[id];
	  }
    }
    else if (flag === 'PENDREQ'){
      await Backend.delete(`/api/users/me/friends/requests/${id}`);
      indexToDelete = pendingRequests.value.findIndex(pendreq => pendreq.id === id);
      if(indexToDelete !== -1)
        pendingRequests.value.splice(indexToDelete, 1);
		delete pendingRequests.value[id];
    }
  } catch(err){
    console.log(err.message);
  }
	closeModal();
};

const acceptRequest = async(requestid, username, userid) => {
    try {
      const acceptedRequest = await Backend.post(`/api/users/me/friends/requests/${requestid}`, {});
      friends.value.push({"id": `${userid}`, "nickname": `${username}`});
	  friendsAvatar.value[userid] = friendRequestsAvatar.value[userid];
      const indexToDelete = friendRequests.value.findIndex(friendreq => friendreq.id === requestid);
      if(indexToDelete !== -1){
		friendRequests.value.splice(indexToDelete, 1);
		console.log(friendRequestsAvatar.value);
		delete friendRequestsAvatar.value[userid];
		console.log(friendRequestsAvatar.value);
	  }
      console.log(acceptedRequest);
    } catch (err) {
        console.error(err.message);
    }
};

onMounted(() => {
  fetchData();
	new bootstrap.Modal('#friendsModalToggle', { keyboard: true })
})
</script>

<template>
	<div class="cont">
		<div class="box">
			<UserSearch :pendingRequests="pendingRequests" :friends="friends" :friendRequests="friendRequests"
				:pendingRequestsAvatar="pendingRequestsAvatar" :friendRequestsAvatar="friendRequestsAvatar" :friendsAvatar="friendsAvatar"/>
			<Loading v-if="!isLoaded"/>
			<div v-if="isLoaded" class="con mt-5">
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
											<img :src="friendsAvatar[friend.id]"
												alt="..."
												class="img-thumbnail rounded"
												style="width: 50px; height: 50px; object-fit: cover;"
											/>
										</td>
										<td class="bg-light text-start align-middle">
											<router-link :to="`/friends/${friend.nickname}`">{{friend.nickname}}</router-link>
										</td>
										<td class="bg-light text-end align-middle">
											<!-- <button type="button" class="btn btn-outline-danger" aria-label="Close" @click="delData('FRIEND', friend.id)">X</button> -->
											<button type="button" class="btn btn-outline-danger" aria-label="Close" @click="openModal('FRIEND', friend.id)">X</button>
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
													<img :src="friendRequestsAvatar[friend.from_user.id]"
														alt="..."
														class="img-thumbnail rounded"
														style="width: 50px; height: 50px; object-fit: cover;">
												</td>
												<td class="bg-light align-middle">{{friend.from_user.nickname}}</td>
												<td class="bg-light text-end align-middle d-none d-md-table-cell">
													<button class="btn btn-outline-success ms-auto me-2" @click="acceptRequest(friend.id, friend.from_user.nickname, friend.from_user.id)">✓</button>
													<button class="btn btn-outline-danger" @click="openModal('FRIENDREQ', friend.id)">X</button>
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
													<img :src="pendingRequestsAvatar[friend.to_user.id]"
														alt="..."
														class="img-thumbnail rounded"
														style="width: 50px; height: 50px; object-fit: cover;">
												</td>
												<td class="bg-light align-middle">{{friend.to_user.nickname}}</td>
												<td class="bg-light text-end align-middle d-none d-md-table-cell">
													<button class="btn btn-outline-danger" @click="openModal('PENDREQ', friend.id)">X</button>
												</td>
											</tr>
										</tbody>
										<tbody v-else class="text-center">No {{useI18n().t('friendsview.pendingrequests')}}</tbody>
									</table>
								</div>
						</div>
					</div>
				</div>
			<!-- MODAL -->
			<div class="modal fade" id="friendsModalToggle" aria-hidden="true">
				<div class="modal-dialog" role="document">
					<div class="modal-content rounded-4 shadow">
						<div class="modal-body p-3 text-center">
							<h6 v-if="modalFlag === 'FRIEND'">Are you sure you want to delete this friend?</h6>
							<h6 v-if="modalFlag === 'FRIENDREQ'">Are you sure you want to decline this friend request?</h6>
							<h6 v-if="modalFlag === 'PENDREQ'">Are you sure you want to withdraw this friend request?</h6>
							<button class="btn btn-danger mt-2 me-2" @click="delData(modalFlag, modalId)">Confirm</button>
							<button class="btn btn-secondary mt-2 ms-2" @click="closeModal">Cancel</button>
						</div>
					</div>
				</div>
			</div>
		</div>
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
