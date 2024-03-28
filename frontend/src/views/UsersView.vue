
<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted } from 'vue';
import { globalUser } from '../main';
//import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'

const users = ref([])

const fetchData = async () => {
	try {
		users.value = await Backend.get('/api/users');
		users.value = users.value.filter(user => user.id !== globalUser.value.id);
		return users.value;
	} catch (err) {
		console.error(err.message);
		// ADD ALERT?
	}
};

onMounted(() => {
	fetchData();
})

</script>

<template>
	<div>
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
</template>

<style>
</style>
