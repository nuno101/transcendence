<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import Friends from '../js/Friends';
import UserSearch from '../components/dashboard/UserSearch.vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'
import { onMounted, ref } from 'vue';
import Loading from '../components/common/Loading.vue';
import UserRow from '../components/common/UserRow.vue';

const modalFlag = ref('');
const modalRequest = ref('');

const isLoaded = ref(false);


const fetchData = async () => {
  try {
    Friends.friends.value = await Backend.get(`/api/users/me/friends`);
    Friends.friendRequests.value = await Backend.get(`/api/users/me/friends/requests?type=received`);
    Friends.pendingRequests.value = await Backend.get(`/api/users/me/friends/requests?type=sent`);
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

const acceptRequest = async (request) => {
        try {
            const acceptedRequest = await Backend.post(`/api/users/me/friends/requests/${request.id}`, {});
            Friends.friends.value.push(acceptedRequest);
            const indexToDelete = Friends.friendRequests.value.findIndex(friendreq => friendreq.id === request.id);
            if(indexToDelete !== -1)
              Friends.friendRequests.value.splice(indexToDelete, 1);
          } catch (err) {
              console.error(err.message);
              alert(err.message);
          }
    };

const declineCancelDeleteRequest = async(flag, request) => {
	let requestArr;
	try {
		if(flag === 'DELETEFRIEND') {
			await Backend.delete(`/api/users/me/friends/${request.id}`, {});
			requestArr = Friends.friends.value;
		}
		else if (flag === 'DECLINEFRIENDREQ') {
			await Backend.delete(`/api/users/me/friends/requests/${request.id}`, {});
			requestArr = Friends.friendRequests.value;
		}
		else if (flag === 'CANCELPENDREQ') {
			await Backend.delete(`/api/users/me/friends/requests/${request.id}`, {});
			requestArr = Friends.pendingRequests.value;
		}

		const indexToDelete = requestArr.findIndex(friendreq => friendreq.id === request.id);
		if(indexToDelete !== -1) {
			requestArr.splice(indexToDelete, 1);
		}
		closeModal();
	} catch (err) {
		console.error(err.message);
		alert(err.message);
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
			<UserSearch :pendingRequests="Friends.pendingRequests.value"/>
			<Loading v-if="!isLoaded"/>
			<div v-if="isLoaded" class="con mt-5">
					<div class="row">
						<div class="col-7">
							<div class="bigtable gamestable rounded img-thumbnail d-md-block">
							<table class="table m-0">
								<thead class="table-dark">
									<tr><th colspan="4" class="text-center">{{useI18n().t('friendsview.listoffriends')}}</th></tr>
								</thead>
								<tbody v-if="Friends.friends.value && Friends.friends.value.length > 0">
									<tr v-for="(friend, index) in Friends.friends.value" :key="friend">
										<td class="bg-light text-center align-middle">{{index + 1}}</td>
										<UserRow :user="friend"/>
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
										<tbody v-if="Friends.friendRequests.value.length > 0">
											<tr v-for="friend in Friends.friendRequests.value" :key="friend">
												<UserRow :user="friend.from_user"/>
												<td class="bg-light text-end align-middle d-none d-md-table-cell">
													<button class="btn btn-outline-success ms-auto me-2"
														@click="acceptRequest(friend)"
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
										<tbody v-if="Friends.pendingRequests.value.length > 0">
											<tr v-for="friend in Friends.pendingRequests.value" :key="friend">
												<UserRow :user="friend.to_user"/>
												<td class="bg-light text-end align-middle d-none d-md-table-cell">
													<button class="btn ms-auto me-2 invisible"></button>
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
							<button class="btn btn-danger mt-2 me-2" @click="declineCancelDeleteRequest(modalFlag, modalRequest);">Confirm</button>
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
