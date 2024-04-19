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
		<div v-if="isLoaded && user.id" class="box rounded">
			<div class="row align-items-center">
                <div class="col bg-danger rounded-pill rounded-end-0 pt-2 " style="height:40px;">
                    <div class="text-white d-flex" style="width: 100%;">
                        <div class="p-0 d-none d-sm-flex" style="width: 50%;">{{useI18n().t('userstats.defeats')}}</div>
                        <div class="text-end pe-5" style="width: 50%;">{{ DefeatGames.length }}</div>
                    </div>
                </div>
                <GetAvatar class="col-auto p-0" :id="user.id" :size="100" />
                <div class="col bg-success rounded-pill rounded-start-0 pt-2 " style="height:40px;"> 
                    <div class="text-white d-flex" style="width: 100%;">
                        <div class="d-none d-sm-flex ps-5" style="width: 50%;">{{ WinGames.length }}</div>
                        <div class="d-none d-sm-block text-end" style="width: 50%;">{{useI18n().t('userstats.wins')}}</div>
                        <div class="text-end pe-3 d-sm-none" style="width: 100%;">{{ WinGames.length }}</div>
                    </div>
                </div>
            </div>
			<div class="text-center">
				<div class="bg-dark px-4 pb-1 text-white d-inline-block rounded-bottom">
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
</template>

<style scoped>
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
</style>
