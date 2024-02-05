<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../../js/Backend';
import { ref, defineProps, watch } from 'vue';

const searchInput = ref('');
const searchStatus = ref(''); // Possible values: 'found', 'notFound', 'nothing'
const usersData = ref([]);
const foundUser = ref(null);

const props = defineProps(['pendingRequests', 'friendRequests', 'friends']);

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
    await fetchData();
    foundUser.value = usersData.value.find(user => user.username === searchedUser);
    if (foundUser.value) {
        searchStatus.value = 'found';
        console.log("FOUNDUSER.value: " + foundUser.value.username);
    } else {
        searchStatus.value = 'notFound';
    }
  } catch (error) {
    console.error(error.message);
  }
};

const userRelation = (searchedUser) => {
    console.log(props.friendRequests);
    console.log("PENDING: " + props.pendingRequests);
    console.log(props.friends);

    if (props.friends.find(friend => friend.username === searchedUser))
        return('FRIENDS');
    else if (props.friendRequests.find(friend => friend.from_user.username === searchedUser))
        return('FRIENDREQ');
    else if (props.pendingRequests.find(friend => friend.to_user.username === searchedUser))
        return('PENDREQ');
    return('NOTHING');
};

const sendRequest = async() => {
    try {
        console.log(foundUser.value.username);
        const newRequest = await Backend.post(`/api/users/me/friends/requests`, {"username": `${foundUser.value.username}`});
        console.log(newRequest)
        props.pendingRequests.push(newRequest);
    } catch (err) {
        console.error(err.message);
    }
    resetSearch();
};

const acceptRequest = async() => {
    try {
        const requestId = props.friendRequests.find(request => request.from_user.username === foundUser.value.username)?.id;
        if (requestId) {
            const acceptedRequest = await Backend.post(`/api/users/me/friends/requests/${requestId}`, {});
            props.friends.push({"id": `${requestId}`, "username": `${foundUser.value.username}`});
            const indexToDelete = props.friendRequests.findIndex(friendreq => friendreq.id === requestId);
            if(indexToDelete !== -1)
                props.friendRequests.splice(indexToDelete, 1);
            console.log(acceptedRequest);
        }
    } catch (err) {
        console.error(err.message);
    }
    resetSearch();
};

const declineRequest = async() => {
    try {
        const requestId = props.friendRequests.find(request => request.from_user.username === foundUser.value.username)?.id;
        if (requestId) {
            const declinedRequest = await Backend.delete(`/api/users/me/friends/requests/${requestId}`, {});
            const indexToDelete = props.friendRequests.findIndex(friendreq => friendreq.id === requestId);
            if(indexToDelete !== -1)
                props.friendRequests.splice(indexToDelete, 1);
            console.log(declinedRequest);
        }
    } catch (err) {
        console.error(err.message);
    }
    resetSearch();
};

const cancelRequest = async() => {
    try {
        const requestId = props.pendingRequests.find(request => request.to_user.username === foundUser.value.username)?.id;
        if (requestId) {
            const cancelledRequest = await Backend.delete(`/api/users/me/friends/requests/${requestId}`, {});
            const indexToDelete = props.pendingRequests.findIndex(friendreq => friendreq.id === requestId);
            if(indexToDelete !== -1)
                props.pendingRequests.splice(indexToDelete, 1);
            console.log(cancelledRequest);
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
        <input v-model="searchInput" type="search" class="form-control rounded-start" placeholder="Search user" aria-label="Search" aria-describedby="search-addon" />
        <button @click="searchUser(searchInput)" type="button" class="btn btn-outline-primary" data-mdb-ripple-init>search</button>
    </div>
    <div v-if="searchStatus === 'found'">
        <div class="alert alert-success d-flex align-items-center p-1" role="alert">
            <img src="https://dogs-tiger.de/cdn/shop/articles/Magazin_1.png?v=1691506995"
            alt="..."
            class="img-thumbnail rounded me-4"
            style="width: 50px; height: 50px; object-fit: cover;">
            {{ foundUser.username }}
            <!-- IF NOT FRIENDS ADD FRIEND BUTTON -->
            <div v-if="userRelation(searchInput) === 'FRIENDS'" class="ms-auto me-4 text-success">friends</div>
            <button v-else-if="userRelation(searchInput) === 'PENDREQ'" class="btn btn-outline-danger ms-auto me-4" @click="cancelRequest">cancel sent request</button>
            <div v-else-if="userRelation(searchInput) === 'FRIENDREQ'" class="ms-auto me-4">
                <button class="btn btn-outline-success me-2" @click="acceptRequest">accept</button>
                <button class="btn btn-outline-danger" @click="declineRequest">decline</button>
            </div>
            <button v-else-if="userRelation(searchInput) === 'NOTHING'" type="button" class="btn btn-outline-success ms-auto me-4" @click="sendRequest">add friend</button>
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