<script setup>
import { useI18n } from 'vue-i18n';
import { defineProps } from 'vue';

const props = defineProps(['firstplayer', 'secondplayer', 'ai']);

const svgW = `
	<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-down-square" viewBox="0 0 16 16">
		<text x="3" y="12" font-family="Arial" font-size="11" fill="currentColor">W</text>
		<path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm15 0a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1z"/>
	</svg>
`;

const svgS = `
	<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-down-square" viewBox="0 0 16 16">
		<text x="4" y="12" font-family="Arial" font-size="11" fill="currentColor">S</text>
		<path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm15 0a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1z"/>
	</svg>
`;

const svgSpace = `
	<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-down-square" viewBox="0 0 16 16">
		<path d="m 11.8 7.2 c -0.48 0 -0.8 0.32 -0.8 0.8 v 2.4 h -5.6 v -2.4 c 0 -0.48 -0.32 -0.8 -0.8 -0.8 s -0.8 0.32 -0.8 0.8 v 3.2 c 0 0.48 0.32 0.8 0.8 0.8 h 7.2 c 0.48 0 0.8 -0.32 0.8 -0.8 v -3.2 c 0 -0.48 -0.32 -0.8 -0.8 -0.8 z"></path>
		<path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm15 0a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1z"/>
	</svg>
`;

const svgH = `
	<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-down-square" viewBox="0 0 16 16">
		<text x="4.1" y="12" font-family="Arial" font-size="11" fill="currentColor">H</text>
		<path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm15 0a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1z"/>
	</svg>
`;

const svgF = `
	<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-down-square" viewBox="0 0 16 16">
		<text x="4.5" y="12" font-family="Arial" font-size="11" fill="currentColor">F</text>
		<path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm15 0a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1z"/>
	</svg>
`;

</script>

<template>
	<div class="alert alert-primary" role="alert">
		{{useI18n().t('instruction.goal')}}
		<div v-if="props.ai">
			<hr>
			<div v-if="props.firstplayer || props.secondplayer">
				<div v-if="props.firstplayer">
					<strong>{{useI18n().t('instruction.you')}}  </strong> {{useI18n().t('instruction.use')}} <span v-html="svgW"></span> {{useI18n().t('instruction.and')}} <span v-html="svgS"></span> {{useI18n().t('instruction.toMoveThe')}} <strong>{{useI18n().t('instruction.leftPaddle')}}</strong><br/>
				</div>
				<div v-if="props.secondplayer">
					<strong>{{useI18n().t('instruction.you')}}  </strong> {{useI18n().t('instruction.use')}} <i class="bi bi-caret-up-square"></i> {{useI18n().t('instruction.and')}} <i class="bi bi-caret-down-square"></i> {{useI18n().t('instruction.toMoveThe')}} <strong>{{useI18n().t('instruction.rightPaddle')}}</strong>
				</div>
				<hr>
			</div>
		</div>
		<div v-else>
			<hr>
			<strong>{{ props.firstplayer || useI18n().t('instruction.leftplayer')}}</strong> {{useI18n().t('instruction.uses')}} <span v-html="svgW"></span> {{useI18n().t('instruction.and')}} <span v-html="svgS"></span> {{useI18n().t('instruction.toMoveThe')}} <strong>{{useI18n().t('instruction.leftPaddle')}}</strong><br/>
			<strong>{{ props.secondplayer || useI18n().t('instruction.rightplayer')}}</strong> {{useI18n().t('instruction.uses')}} <i class="bi bi-caret-up-square"></i> {{useI18n().t('instruction.and')}} <i class="bi bi-caret-down-square"></i> {{useI18n().t('instruction.toMoveThe')}} <strong>{{useI18n().t('instruction.rightPaddle')}}</strong>
			<hr>
		</div>
		<span v-html="svgSpace"></span> {{useI18n().t('instruction.startOrPause')}} {{useI18n().t('instruction.theGame')}}<br>
		<span v-html="svgH"></span> {{useI18n().t('instruction.showOrHide')}} {{useI18n().t('instruction.theseInstructions')}}<br>
		<span v-html="svgF"></span> {{useI18n().t('instruction.showOrHide')}} {{useI18n().t('instruction.fpsCounter')}}
		<!-- TODO remove -->
		<hr>
		<strong>during development</strong><br>
		press [q] to set scores [ 11 : ? ]<br>
		press [e] to set scores [ ? : 11 ]
	</div>
</template>

<style>
</style>
