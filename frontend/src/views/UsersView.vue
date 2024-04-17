
<script setup>
import { useI18n } from 'vue-i18n';
import Backend from '../js/Backend';
import { ref, onMounted } from 'vue';
import { globalUser } from '../main';
import UserRow from '../components/common/UserRow.vue';

const users = ref([])

const fetchData = async () => {
	try {
		users.value = await Backend.get('/api/users');
		users.value = users.value.filter(user => user.id !== globalUser.value.id);
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
			<h6 class="text-center fw-bold text-uppercase">{{useI18n().t('usersview.listofusers')}}</h6>
			<div class="rounded img-thumbnail d-md-block usertable">
				<table class="table m-0 table-striped table-hover">
					<thead>
						<tr class="align-middle">
							<th colspan="2">{{useI18n().t('usersview.nickname')}}</th>
							<th>{{useI18n().t('usersview.username')}}</th>
							<th class="d-none d-md-table-cell">{{useI18n().t('usersview.created_at')}}</th>
							<th class="d-none d-md-table-cell">{{useI18n().t('usersview.updated_at')}}</th>
						</tr>
					</thead>
					<tbody>
						<tr v-for="user in users" :key="user.id" class="align-middle">
							<UserRow :user="user" bgColor=""/>
							<td>{{ user.username }}</td>
							<td class="d-none d-md-table-cell">{{ user.created_at }}</td>
							<td class="d-none d-md-table-cell">{{ user.updated_at }}</td>
						</tr>
					</tbody>
				</table>
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

.usertable {
	flex: 1;
	padding: 0;
	overflow-y: auto;
	height: max(calc(100vh - var(--header-height) - 88px - 100px), 170px);
}
</style>
