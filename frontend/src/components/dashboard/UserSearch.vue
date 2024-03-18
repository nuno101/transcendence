<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../../js/Backend';
import { ref, defineProps, watch } from 'vue';

const searchInput = ref('');
let updateErrorMessage = ref('');


const props = defineProps(['pendingRequests']);

const addFriend = async(nickname) => {
    try {
        const request = await Backend.post(`/api/users/me/friends/requests`, {"nickname": `${nickname}`});
        if(request) {
            props.pendingRequests.push(request);
            resetSearch();
        }
        updateErrorMessage.value = '';
    } catch (err) {
        console.error(err.message);
        updateErrorMessage.value = err;
    }
};

const resetSearch = () => {
  searchInput.value = '';
};

watch(searchInput, () => {
});
</script>

<template>
    <div>
        <div class="input-group">
            <input v-model="searchInput" type="search" class="form-control rounded-start" :placeholder="useI18n().t('friendsview.searchNickname')" aria-label="Search" aria-describedby="search-addon" />
            <button @click="addFriend(searchInput)" type="button" class="btn btn-outline-primary" data-mdb-ripple-init><i class="bi bi-person-add"></i></button>
        </div>
        <div v-if="updateErrorMessage !== ''" class="alert alert-danger d-flex align-items-center p-1" role="alert">
            {{ updateErrorMessage }}
        </div>
    </div>
</template>

<style scoped>
</style>