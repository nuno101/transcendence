<!-- Translation for 'GAME OVER' is missing on purpose-->
<template>
    <div class="alert alert-primary" role="alert">
        <div class="text-center">
            <h1><strong>GAME OVER</strong></h1>
            {{ winner || i18n.t('instruction.' + (firstscore > secondscore ? 'leftplayer' : 'rightplayer')) }} {{ i18n.t('ponggameview.wonthegame') }}<br>
            [ {{ firstscore }} : {{ secondscore }} ]<hr>
        </div>
        {{ i18n.t('ponggameview.press') }}<img width="90" src="../../assets/img/Space_Key.svg" :alt="useI18n().t('instruction.spacebar')" :title="useI18n().t('instruction.spacebar')"/>{{ i18n.t('ponggameview.tocontinue') }}
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const i18n = useI18n()
const props = defineProps(['winner', 'firstscore', 'secondscore'])
</script>
