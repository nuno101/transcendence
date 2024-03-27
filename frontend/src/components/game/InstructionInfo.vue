<script setup>
import { useI18n } from 'vue-i18n';
import { defineProps } from 'vue';

const props = defineProps(['firstplayer', 'secondplayer', 'ai']);
</script>

<template>
	<div class="alert alert-primary" role="alert">
		{{useI18n().t('instruction.goal')}}<hr>
		<div v-if="props.ai">
			<div v-if="props.firstplayer || props.secondplayer">
				<div v-if="props.firstplayer">
					<strong>{{useI18n().t('instruction.you')}}  </strong> {{useI18n().t('instruction.use')}} <img width="25" src="../../assets/img/W_Key.svg" :alt="useI18n().t('instruction.wkey')" :title="useI18n().t('instruction.wkey')"/>  {{useI18n().t('instruction.and')}} <img width="25" src="../../assets/img/S_Key.svg" :alt="useI18n().t('instruction.skey')" :title="useI18n().t('instruction.skey')"/> {{useI18n().t('instruction.toMoveThe')}} <strong>{{useI18n().t('instruction.leftPaddle')}}</strong><br/>
				</div>
				<div v-if="props.secondplayer">
					<strong>{{useI18n().t('instruction.you')}}  </strong> {{useI18n().t('instruction.use')}} <img width="25" src="../../assets/img/ArrowUp_Key.svg" :alt="useI18n().t('instruction.arrowup')" :title="useI18n().t('instruction.arrowup')"/> {{useI18n().t('instruction.and')}} <img width="25" src="../../assets/img/ArrowDown_Key.svg" :alt="useI18n().t('instruction.arrowdown')" :title="useI18n().t('instruction.arrowdown')"/> {{useI18n().t('instruction.toMoveThe')}} <strong>{{useI18n().t('instruction.rightPaddle')}}</strong>
				</div>
				<hr>
			</div>
		</div>
		<div v-else>
			<strong>{{ props.firstplayer || useI18n().t('instruction.leftplayer')}}</strong> {{useI18n().t('instruction.uses')}} <img width="25" src="../../assets/img/W_Key.svg" :alt="useI18n().t('instruction.wkey')" :title="useI18n().t('instruction.wkey')"/>  {{useI18n().t('instruction.and')}} <img width="25" src="../../assets/img/S_Key.svg" :alt="useI18n().t('instruction.skey')" :title="useI18n().t('instruction.skey')"/>  {{useI18n().t('instruction.toMoveThe')}} <strong>{{useI18n().t('instruction.leftPaddle')}}</strong><br/>
			<strong>{{ props.secondplayer || useI18n().t('instruction.rightplayer')}}</strong> {{useI18n().t('instruction.uses')}} <img width="25" src="../../assets/img/ArrowUp_Key.svg" :alt="useI18n().t('instruction.arrowup')" :title="useI18n().t('instruction.arrowup')"/> {{useI18n().t('instruction.and')}} <img width="25" src="../../assets/img/ArrowDown_Key.svg" :alt="useI18n().t('instruction.arrowdown')" :title="useI18n().t('instruction.arrowdown')"/> {{useI18n().t('instruction.toMoveThe')}} <strong>{{useI18n().t('instruction.rightPaddle')}}</strong>
			<hr>
		</div>
		<img width="90" src="../../assets/img/Space_Key.svg" :alt="useI18n().t('instruction.spacebar')" :title="useI18n().t('instruction.spacebar')"/> {{useI18n().t('instruction.startOrPause')}} {{useI18n().t('instruction.theGame')}}<br>
		<img width="25" src="../../assets/img/H_Key.svg"  :alt="useI18n().t('instruction.hkey')" :title="useI18n().t('instruction.hkey')"/>  {{useI18n().t('instruction.showOrHide')}} {{useI18n().t('instruction.theseInstructions')}}<br>
		<img width="25" src="../../assets/img/F_Key.svg"  :alt="useI18n().t('instruction.fkey')" :title="useI18n().t('instruction.fkey')"/>  {{useI18n().t('instruction.showOrHide')}} {{useI18n().t('instruction.fpsCounter')}}
		<!-- TODO remove -->
		<hr>
		<strong>during development</strong><br>
		press [q] to set scores [ 11 : ? ]<br>
		press [e] to set scores [ ? : 11 ]
	</div>
</template>

<style>
</style>
