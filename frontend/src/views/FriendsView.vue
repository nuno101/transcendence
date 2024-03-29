<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import Friends from '../js/Friends';
import UserSearch from '../components/dashboard/UserSearch.vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'
import { onMounted, ref } from 'vue';
import Loading from '../components/common/Loading.vue';
import UserRow from '../components/common/UserRow.vue';

const modalRequest = ref('');
const modalFunction = ref('');

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

const openModal = async(func, id) => {
	modalFunction.value = func;
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
			Friends.friendRequests.value = Friends.friendRequests.value.filter(friend => friend.id !== request.id);
          } catch (err) {
              console.error(err.message);
              alert(useI18n().te(`err.${err.message}`) ?  useI18n().t(`err.${err.message}`) : err.message);
          }
    };

const deleteFriend = async () => {
  await Backend.delete(`/api/users/me/friends/${modalRequest.value.id}`, {});
  Friends.friends.value = Friends.friends.value.filter(friend => friend.id !== modalRequest.value.id);
};

const declineFriendRequest = async () => {
  await Backend.delete(`/api/users/me/friends/requests/${modalRequest.value.id}`, {});
  Friends.friendRequests.value = Friends.friendRequests.value.filter(friend => friend.id !== modalRequest.value.id);
};

const cancelFriendRequest = async () => {
  await Backend.delete(`/api/users/me/friends/requests/${modalRequest.value.id}`, {});
  Friends.pendingRequests.value = Friends.pendingRequests.value.filter(friend => friend.id !== modalRequest.value.id);
};

const declineCancelDeleteRequest = async() => {
	try {
		await modalFunction.value(modalRequest.value);
		closeModal();
	} catch (err) {
		console.error(err.message);
		alert(useI18n().te(`err.${err.message}`) ?  useI18n().t(`err.${err.message}`) : err.message);
	}
};

onMounted(() => {
  fetchData();
	new bootstrap.Modal('#friendsModalToggle', { keyboard: true })
})
</script>

<template>
	<div class="boxstyling">
		<div class="box rounded">
			<UserSearch :pendingRequests="Friends.pendingRequests.value"/>
			<Loading v-if="!isLoaded"/>
			<div v-if="isLoaded" class="con mt-5">
					<div class="row">
						<div class="col-7">
							<div class="bigtable gamestable rounded img-thumbnail d-md-block">
							<table class="table m-0">
								<thead>
									<tr><th colspan="4" class="text-center">{{useI18n().t('friendsview.friends')}}</th></tr>
								</thead>
								<tbody v-if="Friends.friends.value && Friends.friends.value.length > 0">
									<tr v-for="(friend, index) in Friends.friends.value" :key="friend">
										<td class="bg-light text-center align-middle">{{index + 1}}</td>
										<UserRow :user="friend"/>
										<td class="bg-light text-end align-middle">
											<button type="button" class="btn btn-outline-danger" aria-label="Close" @click="openModal(deleteFriend, friend)">X</button>
										</td>
									</tr>
								</tbody>
								<tbody v-else class="text-center">{{useI18n().t('friendsview.noFriends')}}</tbody>
							</table>
						</div>
						</div>
						<div class="col-5">
								<div class="smalltable gamestable rounded img-thumbnail d-md-block">
										<table class="table table-hover m-0">
											<thead>
												<tr><th colspan="4" class="text-center">{{useI18n().t('friendsview.friendrequests')}}</th></tr>
											</thead>
										<tbody v-if="Friends.friendRequests.value.length > 0">
											<tr v-for="friend in Friends.friendRequests.value" :key="friend">
												<UserRow :user="friend.from_user"/>
												<td class="bg-light text-end align-middle d-none d-md-table-cell">
													<button class="btn btn-outline-success ms-auto me-2"
														@click="acceptRequest(friend)"
													>✓</button>
													<button class="btn btn-outline-danger" @click="openModal(declineFriendRequest, friend)">X</button>
												</td>
											</tr>
										</tbody>
										<tbody v-else class="text-center">{{useI18n().t('friendsview.noFriendRequests')}}</tbody>
									</table>
								</div>
								<div class="mt-2 mt-lg-4 smalltable gamestable rounded img-thumbnail d-md-block">
										<table class="table table-hover m-0">
											<thead>
												<tr><th colspan="3" class="text-center">{{useI18n().t('friendsview.pendingrequests')}}</th></tr>
											</thead>
										<tbody v-if="Friends.pendingRequests.value.length > 0">
											<tr v-for="friend in Friends.pendingRequests.value" :key="friend">
												<UserRow :user="friend.to_user"/>
												<td class="bg-light text-end align-middle d-none d-md-table-cell">
													<button class="btn ms-auto me-2 invisible"></button>
													<button class="btn btn-outline-danger" @click="openModal(cancelFriendRequest, friend)">X</button>
												</td>
											</tr>
										</tbody>
										<tbody v-else class="text-center">{{useI18n().t('friendsview.noPendingRequests')}}</tbody>
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
							<h6 v-if="modalFunction.name">{{ useI18n().t(`friendsview.${modalFunction.name}`) || ''}}</h6>
							<button class="btn btn-danger mt-2 me-2" @click="declineCancelDeleteRequest();">{{useI18n().t('confirm')}}</button>
							<button class="btn btn-secondary mt-2 ms-2" @click="closeModal">{{useI18n().t('cancel')}}</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>

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
