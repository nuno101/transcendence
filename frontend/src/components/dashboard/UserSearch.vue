<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../../js/Backend';
import Avatar from '../../js/Avatar';
import Friends from '../../js/Friends';
import { ref, defineProps, watch } from 'vue';

const searchInput = ref('');
const searchStatus = ref(''); // Possible values: 'found', 'notFound', 'nothing'
const usersData = ref([]);
const foundUser = ref(null);
const avatar = ref('');
const avatarLoaded = ref(false);

const props = defineProps(['pendingRequests', 'friendRequests', 'friends',
        'pendingRequestsAvatar', 'friendRequestsAvatar', 'friendsAvatar']);

const fetchData = async () => {
  try {
    usersData.value = await Backend.get(`/api/users`);
    return usersData;
  } catch (err) {
    console.error(err.message);
  }
};

const searchUser = async (searchedUser) => {
  try {
    avatarLoaded.value = false;
    await fetchData();
    foundUser.value = usersData.value.find(user => user.nickname === searchedUser);
    if (foundUser.value) {
        avatar.value = await Avatar.getAvatarById(foundUser.value.id);
        searchStatus.value = 'found';
    } else {
        searchStatus.value = 'notFound';
    }
  } catch (error) {
    console.error(error.message);
  } finally {
      avatarLoaded.value = true;
  }
};

const userRelation = (searchedUser) => {
    if (props.friends.find(friend => friend.nickname === searchedUser))
        return('FRIENDS');
    else if (props.friendRequests.find(friend => friend.from_user.nickname === searchedUser))
        return('FRIENDREQ');
    else if (props.pendingRequests.find(friend => friend.to_user.nickname === searchedUser))
        return('PENDREQ');
    return('NOTHING');
};

const handleRequests = async(flag) => {
    try {
        if(flag === 'SENDREQ') {
            // USE NICKNAME !!!
            // DONT CHECK FOR USERS IN USER GET REQUEST --> POST DIRECTLY HANDLE RESPONSE
            const request = await Backend.post(`/api/users/me/friends/requests`, {"username": `${foundUser.value.username}`});
            if(request) {
                props.pendingRequests.push(request);
                props.pendingRequestsAvatar[foundUser.value.id] = avatar.value;
            }
        } else if(flag === 'ACCEPTREQ') {
            const request = props.friendRequests.find(request => request.from_user.username === foundUser.value.username);
            if (request)
                Friends.acceptRequest(props.friends, props.friendsAvatar, props.friendRequests, props.friendRequestsAvatar, request);
        } else if (flag === 'DECLINEREQ') {
            const request = props.friendRequests.find(request => request.from_user.username === foundUser.value.username);
            if (request)
                Friends.declineCancelDeleteRequest('DECLINEFRIENDREQ', props.friendRequests, props.friendRequestsAvatar, request);
        } else if (flag === 'CANCELREQ') {
            const request = props.pendingRequests.find(request => request.to_user.username === foundUser.value.username);
            if (request)
                Friends.declineCancelDeleteRequest('CANCELPENDREQ', props.pendingRequests, props.pendingRequestsAvatar, request);
        }
    } catch (err) {
        console.error(err.message);
    }
    resetSearch();
};

const resetSearch = () => {
  searchStatus.value = '';
  searchInput.value = '';
};

watch(searchInput, () => {
  searchStatus.value = '';
});
</script>

<template>
    <div>
    <div class="input-group">
        <input v-model="searchInput" type="search" class="form-control rounded-start" placeholder="Search nickname" aria-label="Search" aria-describedby="search-addon" />
        <button @click="searchUser(searchInput)" type="button" class="btn btn-outline-primary" data-mdb-ripple-init><i class="bi bi-search"></i></button>
    </div>
    <div v-if="searchStatus === 'found' && avatarLoaded === true">
        <div class="alert alert-success d-flex align-items-center p-1" role="alert">
            <img :src="avatar"
            alt="..."
            class="img-thumbnail rounded me-4"
            style="width: 50px; height: 50px; object-fit: cover;">
            {{ foundUser.nickname }}
            <div v-if="userRelation(searchInput) === 'FRIENDS'" class="ms-auto me-4 text-success">friends</div>
            <button v-else-if="userRelation(searchInput) === 'PENDREQ'" class="btn btn-outline-danger ms-auto me-4" @click="handleRequests('CANCELREQ')">cancel sent request</button>
            <div v-else-if="userRelation(searchInput) === 'FRIENDREQ'" class="ms-auto me-4">
                <button class="btn btn-outline-success me-2" @click="handleRequests('ACCEPTREQ')">accept</button>
                <button class="btn btn-outline-danger" @click="handleRequests('DECLINEREQ')">decline</button>
            </div>
            <button v-else-if="userRelation(searchInput) === 'NOTHING'" type="button" class="btn btn-outline-success ms-auto me-4" @click="handleRequests('SENDREQ')">add friend</button>
            <button type="button" class="btn-close me-2" aria-label="Close" @click="resetSearch"></button>
        </div>
    </div>
    <div v-else-if="searchStatus === 'notFound'">
        <div class="alert alert-danger d-flex align-items-center p-1" role="alert">
            User not found!
            <button type="button" class="btn-close ms-auto me-2" aria-label="Close" @click="resetSearch"></button>
        </div>
    </div>
    </div>
</template>

<style scoped>
</style>