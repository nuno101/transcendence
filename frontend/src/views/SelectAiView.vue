<template>
	<div class="boxstyling">
		<div class="box rounded">
			<h1 class="fs-6 text-center text-uppercase fw-bold">Ai Settings</h1>
			<div class="row row-cols-1 row-cols-md-2 gy-4">
				<div class="col">
					<AiSettings @change="inputChange(1)" v-model:input="input[0]">{{ i18n.t('aisettings.leftplayer') }}</AiSettings>
				</div>
				<div class="col">
					<AiSettings @change="inputChange(0)" v-model:input="input[1]">{{ i18n.t('aisettings.rightplayer') }}</AiSettings>
				</div>
			</div>
			<div class="text-center mt-4">
				<button type="button" class="btn btn-outline-dark" @click="redirectToGame">{{ i18n.t('auth.startGame') }}</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import AiSettings from '../components/game/AiSettings.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const i18n = useI18n()
const input = ref([
	{
		type: 'human',
		inaccuracy: 50,
		border: true,
		center: true,
		opponent: true,
	},
	{
		type: 'ai',
		inaccuracy: 50,
		border: true,
		center: true,
		opponent: true,
	},
])

const inputChange = i => {
	if (input.value[0].type === 'human' && input.value[1].type === 'human') {
		input.value[i].type = 'ai'
	}
}

const redirectToGame = () => {
	const destination = { name: 'ai', query: {} }

	const side = ['l', 'r',]
	input.value.forEach((e, i) => {
		destination.query[side[i] + 'type'] = e.type
		if (e.type === 'human') return

		destination.query[side[i] + 'inaccuracy'] = e.inaccuracy - 50
		destination.query[side[i] + 'border'] = e.border
		destination.query[side[i] + 'center'] = e.center
		destination.query[side[i] + 'opponent'] = e.opponent
	})
	router.push(destination)
}
</script>
