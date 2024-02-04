<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../../js/Backend';
import { ref } from 'vue';

const searchInput = ref('');
const searchStatus = ref(''); // Possible values: 'found', 'notFound', 'nothing'
const usersData = ref([]);
const foundUser = ref(null);

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

const sendRequest = async() => {
    try {
        await Backend.post(`/api/users/me/friends/requests`, {"username": `${foundUser.value.username}`});
    } catch (err) {
        console.error(err.message);
    }
    resetSearch();
    // SHOULD UPDATE PENDING REQUESTS DIRECTLY
};

const resetSearch = () => {
  searchStatus.value = '';
  searchInput.value = '';
};
</script>

<template>
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
            <!-- IF NOT FRIENDS ADD FRIEND BUTTON, IF FRIENDS "ALREADY FRIENDS" -->
            <button type="button" class="btn btn-outline-success ms-auto me-4" @click="sendRequest">add friend</button>
            <button type="button" class="btn-close me-2" aria-label="Close" @click="resetSearch">
            </button>
        </div>
    </div>
    <!-- <div v-else-if="searchStatus === 'notFound'">User not found!</div> -->
</template>

<style scoped>
</style>