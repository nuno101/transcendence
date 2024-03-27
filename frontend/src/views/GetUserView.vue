<template>
	<div class="position-absolute top-50 start-50 translate-middle">
		<div class="spinner-border" role="status">
			<span class="visually-hidden">{{useI18n().t('loading')}}...</span>
		</div>
	</div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { globalUser } from '../main'
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Backend from '../js/Backend'

const route = useRoute()
const router = useRouter()

onMounted(async () => {
	try {
		globalUser.value = await Backend.get('/api/users/me')
	} catch (err) {
		console.error(err.message)
		// TRANSLATE
		globalUser.value = null
	}
	router.replace(decodeURIComponent(route.query.continue))
})
</script>
