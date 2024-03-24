<!-- Translation for 'GAME OVER' is missing on purpose-->
<template>
    <div class="alert alert-primary" role="alert">
        <div class="text-center">
            <h1>GAME OVER</h1>
            {{ winner || i18n.t('instruction.' + (firstscore > secondscore ? 'leftplayer' : 'rightplayer')) }} {{ i18n.t('ponggameview.wonthegame') }}<br>
            [ {{ firstscore }} : {{ secondscore }} ]
            <hr>
        </div>
        {{ i18n.t('ponggameview.press') }}<span v-html="svgSpace"></span>{{ i18n.t('ponggameview.tocontinue') }}
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const i18n = useI18n()
const props = defineProps(['winner', 'firstscore', 'secondscore'])

const svgSpace = `
	<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-down-square" viewBox="0 0 16 16">
		<path d="m 11.8 7.2 c -0.48 0 -0.8 0.32 -0.8 0.8 v 2.4 h -5.6 v -2.4 c 0 -0.48 -0.32 -0.8 -0.8 -0.8 s -0.8 0.32 -0.8 0.8 v 3.2 c 0 0.48 0.32 0.8 0.8 0.8 h 7.2 c 0.48 0 0.8 -0.32 0.8 -0.8 v -3.2 c 0 -0.48 -0.32 -0.8 -0.8 -0.8 z"></path>
		<path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm15 0a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1z"/>
	</svg>
`;
</script>
