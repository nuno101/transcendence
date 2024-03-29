
<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted, defineProps } from 'vue';
//import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'

const users = ref([])
const submit = ref(false);
const input = ref({ title: '', description: '' })
const showAlert = ref(false);
const currentUser = ref(false);

const fetchData = async () => {
  try {
    users.value = await Backend.get('/api/users');

    //FIXME do we need this?
	let current_user = await Backend.get(`/api/users/me`);
	//currentUser.value = current_user.username;
    return users.value;
  } catch (err) {
    console.error(err.message);
  }
};

onMounted(() => {
  fetchData();
})

</script>

<template>
    <div class="boxstyling">
		<div class="box rounded">
        <h1>{{useI18n().t('usersview.listofusers')}}</h1>
        <div>
            <table class="table table-striped table-hover">
                <thead>
                    <tr>
                    <th scope="col">{{useI18n().t('usersview.username')}}</th>
                    <th scope="col">{{useI18n().t('usersview.nickname')}}</th>
                    <th scope="col">{{useI18n().t('usersview.created_at')}}</th>
                    <th scope="col">{{useI18n().t('usersview.updated_at')}}</th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="user in users" :key="user.id">
                        <td>
                            <router-link :to="'/users/' + user.id">
                                {{ user.nickname }}
                            </router-link>
                        </td>
                        <td>{{ user.username }}</td>
                        <td>{{ user.created_at }}</td>
                        <td>{{ user.updated_at }}</td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
        </div>
	</div>

	<div style="margin-top: 20px;"></div>
    <div style="margin-top: 100px;"></div>
    </div>
</template>

<style>
/* MAKE SCROLLABLE */
</style>
