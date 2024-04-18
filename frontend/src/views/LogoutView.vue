<template>
    <div class="d-flex justify-content-center">
        <video class="rounded w-100 logout-video" loop autoplay muted>
            <source :src="gifUrl" type="video/mp4">
            {{ i18n.t('logout.videonotsupported') }}
        </video>
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { globalUser } from '../main'
import Backend from '../js/Backend'
import { onMounted } from 'vue'

onMounted(async () => {
    if (!globalUser.value) return
    try {
		await Backend.post('/api/logout', {})
	} catch (err) {
		console.error(err.message)
	}
    globalUser.value = null
})

const i18n = useI18n()
const gifUrls = [
    'whyyyy-why.mp4',
    'hi.mp4',
    'goodbye-bye-bye.mp4',
    'naza-bart.mp4',
    'fml-my.mp4',
    'peace-out-bye.mp4',
    'respect-pirate.mp4',
    'back-to.mp4',
]
const gifUrl = '/src/assets/video/' + gifUrls[Math.floor(Math.random() * gifUrls.length)]
</script>

<style scoped>
    .logout-video {
        max-width: 25rem;
        min-width: 10rem;
    }
</style>
