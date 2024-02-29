<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import Avatar from '../js/Avatar';
import Friends from '../js/Friends';
import UserSearch from '../components/dashboard/UserSearch.vue';
import OnlineStatus from '../components/dashboard/OnlineStatus.vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'
import { onMounted, ref } from 'vue';
import Loading from '../components/common/Loading.vue';

const friends = ref([]);
const friendsAvatar = ref([]);
const friendRequests = ref([]);
const friendRequestsAvatar = ref([]);
const pendingRequests = ref([]);
const pendingRequestsAvatar = ref([]);

const modalFlag = ref('');
const modalRequest = ref('');

const isLoaded = ref(false);


const fetchData = async () => {
  try {
    friends.value = await Backend.get(`/api/users/me/friends`);
    friendRequests.value = await Backend.get(`/api/users/me/friends/requests?type=received`);
    pendingRequests.value = await Backend.get(`/api/users/me/friends/requests?type=sent`);
	for (const friend of friends.value) {
		const avatarUrl = await Avatar.getAvatarById(friend.id);
		friendsAvatar.value[friend.id] = avatarUrl;
	}
	for (const f of friendRequests.value) {
		const avatarUrl = await Avatar.getAvatarById(f.from_user.id);
		friendRequestsAvatar.value[f.from_user.id] = avatarUrl;
	}
	for (const p of pendingRequests.value) {
		const avatarUrl = await Avatar.getAvatarById(p.to_user.id);
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
	modalRequest.value = id;
	bootstrap.Modal.getInstance("#friendsModalToggle").show();
};

const closeModal = async() => {
	bootstrap.Modal.getInstance("#friendsModalToggle").hide();
};

const delData = async(flag, req) => {
	if(flag === 'DELETEFRIEND')
		Friends.declineCancelDeleteRequest(flag, friends, friendsAvatar, req);
	if(flag === 'DECLINEFRIENDREQ')
		Friends.declineCancelDeleteRequest(flag, friendRequests, friendRequestsAvatar, req);
		if(flag === 'CANCELPENDREQ')
		Friends.declineCancelDeleteRequest(flag, pendingRequests, pendingRequestsAvatar, req);
	closeModal();
};

onMounted(() => {
  fetchData();
	new bootstrap.Modal('#friendsModalToggle', { keyboard: true })
})
</script>

<template>
	<div class="cont">
		<div class="box">
			<UserSearch :pendingRequests="pendingRequests" :pendingRequestsAvatar="pendingRequestsAvatar"/>
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
											<OnlineStatus :status="friend.status" :id="friend.id" class="me-2"/>
											<router-link :to="`/users/${friend.id}`">{{friend.nickname}}</router-link>
										</td>
										<td class="bg-light text-end align-middle">
											<button type="button" class="btn btn-outline-danger" aria-label="Close" @click="openModal('DELETEFRIEND', friend)">X</button>
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
												<td class="bg-light align-middle">
													<router-link :to="`/users/${friend.from_user.id}`">{{friend.from_user.nickname}}</router-link>
												</td>
												<td class="bg-light text-end align-middle d-none d-md-table-cell">
													<button class="btn btn-outline-success ms-auto me-2"
														@click="Friends.acceptRequest(friends, friendsAvatar, friendRequests, friendRequestsAvatar, friend)"
													>✓</button>
													<button class="btn btn-outline-danger" @click="openModal('DECLINEFRIENDREQ', friend)">X</button>
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
												<td class="bg-light align-middle">
													<router-link :to="`/users/${friend.to_user.id}`">{{friend.to_user.nickname}}</router-link>
												</td>
												<td class="bg-light text-end align-middle d-none d-md-table-cell">
													<button class="btn btn-outline-danger" @click="openModal('CANCELPENDREQ', friend)">X</button>
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
							<h6 v-if="modalFlag === 'DELETEFRIEND'">Are you sure you want to delete this friend?</h6>
							<h6 v-if="modalFlag === 'DECLINEFRIENDREQ'">Are you sure you want to decline this friend request?</h6>
							<h6 v-if="modalFlag === 'CANCELPENDREQ'">Are you sure you want to withdraw this friend request?</h6>
							<button class="btn btn-danger mt-2 me-2" @click="delData(modalFlag, modalRequest);">Confirm</button>
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
