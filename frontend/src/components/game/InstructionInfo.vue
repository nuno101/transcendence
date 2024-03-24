<script setup>
import { useI18n } from 'vue-i18n';
import { defineProps } from 'vue';

const props = defineProps(['firstplayer', 'secondplayer']);
</script>

<template>
	<div class="alert alert-primary" role="alert">
		{{useI18n().t('instruction.goal')}}
		<hr>
		<strong>{{ props.firstplayer || useI18n().t('instruction.leftplayer')}}</strong> {{useI18n().t('instruction.uses')}} <img width="25" src="../../assets/W_Key.svg"/>  {{useI18n().t('instruction.and')}} <img width="25" src="../../assets/S_Key.svg"/>  {{useI18n().t('instruction.toMoveThe')}} <strong>{{useI18n().t('instruction.leftPaddle')}}</strong><br/>
		<strong>{{ props.secondplayer || useI18n().t('instruction.rightplayer')}}</strong> {{useI18n().t('instruction.uses')}} <img width="25" src="../../assets/ArrowUp_Key.svg"/> {{useI18n().t('instruction.and')}} <img width="25" src="../../assets/ArrowDown_Key.svg"/> {{useI18n().t('instruction.toMoveThe')}} <strong>{{useI18n().t('instruction.rightPaddle')}}</strong>
		<hr>
		<img width="90" src="../../assets/Space_Key.svg"/> {{useI18n().t('instruction.startOrPause')}} {{useI18n().t('instruction.theGame')}}<br>
		<img width="25" src="../../assets/H_Key.svg"/>  {{useI18n().t('instruction.showOrHide')}} {{useI18n().t('instruction.theseInstructions')}}<br>
		<img width="25" src="../../assets/F_Key.svg"/>  {{useI18n().t('instruction.showOrHide')}} {{useI18n().t('instruction.fpsCounter')}}
		<!-- TODO remove -->
		<hr>
		<strong>during development</strong><br>
		press [q] to set scores [ 11 : ? ]<br>
		press [e] to set scores [ ? : 11 ]
	</div>
</template>

<style>
</style>
