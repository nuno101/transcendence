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
	<div class="cont">
		<Loading v-if="!isLoaded"/>
		<div v-if="isLoaded && user.id" class="box">
			<div class="con mt-5">
				<div class="row">
					<div class="col-6">
						<div class="bg-danger rounded-pill">
							<div class="ms-4 p-2 ps-0 text-white d-flex justify-content-between">
								<div class="p-0">{{useI18n().t('userstats.defeats')}}</div>
								<div class="text-end pe-5">{{ DefeatGames.length }}</div>
							</div>
						</div>
					</div>
					<div class="col-6"> 
						<div class="bg-success rounded-pill">
							<div class="me-4 p-2 pe-0 text-white d-flex justify-content-between">
				  				<div class="ps-5">{{ WinGames.length }}</div>
				  				<div class="text-end">{{useI18n().t('userstats.wins')}}</div>
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
			  		<div class="col-md-2 d-none d-md-block">
						<div class="bar-chart rounded">
				  			<div class="bar defeat-bar rounded" :style="{height: `${defeatsRatio}%`}"></div>
				  			<div class="bar wins-bar rounded" :style="{height: `${winsRatio}%`}"></div>
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

.curved-bg {
	position: relative;
	background: #007bff;
}

.bar-chart {
	display: flex;
	justify-content: center;
	align-items: end;
	background-color: #f0f0f0;
	height: 270px;
}

.bar {
	width: 50px;
	border: 1px solid #fff;
}
.defeat-bar {
	background-color: red;
}

.wins-bar {
	background-color: green;
}

.gamestable {
	max-height: 270px;
	overflow-y: scroll;
	padding: 0;
}

.avatar-circle {
  top: 210px;
}

@media (max-width: 991.98px) {
  .gamestable, .bar-chart {
	height: 164px;
  }
  .avatar-circle {
	top: 245px;
  }
}

@media (max-width: 768px) {
  .gamestable, .bar-chart {
	height: 280px;
  }
  .avatar-circle {
	top: 255px;
  }
}
</style>
