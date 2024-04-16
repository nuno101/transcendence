<script setup>
import { useI18n } from 'vue-i18n';
import { ref, watch, onMounted, computed} from 'vue';
import Backend from '../js/Backend';
import Loading from '../components/common/Loading.vue';
import { useRoute } from 'vue-router';
import GetAvatar from '../components/common/GetAvatar.vue';
import StatsTable from '../components/dashboard/StatsTable.vue';
import router from '../router'

//  GENERAL
const total = ref(null);
const defeatsRatio = ref(null);
const winsRatio = ref(null);

// INDIVIDUAL FRIEND
const userId = ref('');
const user = ref({});
const route = useRoute();
const games = ref([]);

const isLoaded = ref(false);
// defineModel --> wait until all avatars are rendered?

const resetState = () => {
	total.value = null;
	defeatsRatio.value = null;
	winsRatio.value = null;
	userId.value = '';
	user.value = {};
	games.value = {};
	isLoaded.value = false;
};

onMounted(() => {
	userId.value = route.params.id;
	fetchData();
});

watch(() => route.params.id, () => {
	resetState();
	userId.value = route.params.id;
	fetchData();
});

const fetchData = async() => {
	try {
		user.value = await Backend.get(`/api/users/${userId.value}`);
		games.value = await Backend.get(`/api/users/${userId.value}/games`);
		total.value = DefeatGames.value.length + WinGames.value.length;
		defeatsRatio.value = (DefeatGames.value.length / total.value) * 100;
		winsRatio.value = (WinGames.value.length / total.value) * 100;
	} catch (err) {
		router.push({ name: 'pathnotfound' });
		console.error(err.message);
	} finally {
		isLoaded.value = true;
	}
};

const isWin = (game) => {
	if(game.player1.id === Number(userId.value) &&
		game.player1_score >= game.player2_score)
		return true;
	else if (game.player2.id === Number(userId.value) &&
		game.player1_score <= game.player2_score)
		return true;
	return (false);
};

const WinGames = computed(() => {
	return games.value.filter(game => isWin(game));
});

const DefeatGames = computed(() => {
	return games.value.filter(game => !isWin(game));
});
</script>

<template>
	<div class="boxstyling">
		<Loading v-if="!isLoaded"/>
		<div v-if="isLoaded && user.id" class="box rounded" style="overflow:hidden;">
			<div class="con mt-5">
				<div class="row">
					<div class="col-6">
						<div class="bg-danger rounded-pill">
							<div class="ms-4 p-2 ps-0 text-white d-flex justify-content-between">
								<div class="p-0 d-none d-sm-flex">{{useI18n().t('userstats.defeats')}}</div>
								<div class="text-end pe-5">{{ DefeatGames.length }}</div>
							</div>
						</div>
					</div>
					<div class="col-6"> 
						<div class="bg-success rounded-pill">
							<div class="me-4 p-2 pe-0 text-white d-flex justify-content-between">
								<div class="ps-5 d-none d-sm-flex">{{ WinGames.length }}</div>
								<div class="text-end d-none d-sm-flex">{{useI18n().t('userstats.wins')}}</div>
								<div class="ms-auto d-sm-none">{{ WinGames.length }}</div>
							</div>
						</div>
					</div>
				</div>
				<div class="avatar-circle position-absolute start-50 translate-middle">
					<GetAvatar class="float-start" :id="user.id" :size="100" />
				</div>
				<div class="text-center">
					<div class="name bg-dark pe-4 ps-4 pt-3 pb-1 text-white d-inline-block rounded-bottom">
						{{ user.nickname }}
					</div>
				</div>
				<div class="row mt-4">
					<StatsTable :id="Number(userId)" :games="games" :flag="'DEFEATS'" />
					<div class="col-lg-2 d-none d-lg-block border">
						<div class="bar-chart rounded text-white">
							<div class="bar defeat-bar rounded" :style="{height: `${defeatsRatio}%`}">
								<span v-if="defeatsRatio" class="d-flex align-items-center justify-content-center"><strong>{{defeatsRatio.toFixed(0)}}%</strong></span>
							</div>
							<div class="bar wins-bar rounded" :style="{height: `${winsRatio}%`}">
								<span v-if="winsRatio"class="d-flex align-items-center justify-content-center"><strong>{{winsRatio.toFixed(0)}}%</strong></span>
							</div>
						</div>
					</div>
					<StatsTable :id="Number(userId)" :games="games" :flag="'WINS'" />
					<StatsTable :id="Number(userId)" :games="games" :flag="'GAMES'" />
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
.curved-bg {
	position: relative;
	background: #007bff;
}

.bar-chart {
	display: flex;
	justify-content: center;
	background-color: #f0f0f0;
	align-items: end;
	height: 100%;
}

.bar {
	flex: 1;
	width: 50px;
	border: 1px solid #fff;
}

.defeat-bar {
	background-color: red;
}

.wins-bar {
	background-color: green;
}

.avatar-circle {
  top: 200px;
}

@media (max-width: 991.98px) {
  .avatar-circle {
	top: 238px;
  }
}

@media (max-width: 768px) {
  .avatar-circle {
	top: 285px;
  }
}
</style>
