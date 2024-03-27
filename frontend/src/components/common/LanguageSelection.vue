<template>
	<div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle" style="z-index: 3;">
		<button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
			{{ selected }}
		</button>
		<ul class="dropdown-menu">
			<div v-for="lang in languages" :key="lang.title">
				<li @click="changeLocale(lang.language)" class="dropdown-item">{{ lang.title }}</li>
			</div>
		</ul>
	</div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import i18n from '../../plugins/i18n'

const selected = ref('')

const languages = ref([
	{ language: 'en', title: '🇺🇸 English' },
	{ language: 'es', title: '🇪🇸 Español' },
	{ language: 'fr', title: '🇫🇷 Français' },
	{ language: 'de', title: '🇩🇪 Deutsch' },
])

const changeLocale = (value) => {
	const selectedLocale = value
	selected.value = value
	console.log('Selected locale:', selectedLocale)
	// Verify that 'locale' is a valid locale string (e.g., 'en', 'es', etc.)
	if (languages.value.some(e => e.language === selectedLocale)) {
		i18n.global.locale.value = selectedLocale
		localStorage.setItem('selected', selectedLocale)
	} else {
		console.error('Invalid selectedLocale:', selectedLocale)
	}
}

onMounted(() => {
	const storedLang = localStorage.getItem('selected')
	if (storedLang) {
		selected.value = storedLang
		i18n.global.locale.value = storedLang
	} else {
		const defaultLang = 'en'
		selected.value = 'en'
		i18n.global.locale.value = defaultLang
		localStorage.setItem('selected', defaultLang)
	}
	console.log('Mounted phase - selectedLang in LanguageSelection:', selected.value)
})
</script>
