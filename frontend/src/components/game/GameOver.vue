<!-- Translation for 'GAME OVER' is missing on purpose-->
<template>
    <div class="alert alert-primary" role="alert">
        <div class="text-center">
            <h1><strong>GAME OVER</strong></h1>
            <div v-if="props.ai">
                <div v-if="props.winner">
                    {{ i18n.t('ponggameview.youwonthegame') }}<br>
                </div>
                <div v-else>
                    {{ i18n.t('ponggameview.ai') }} {{ i18n.t('ponggameview.wonthegame') }}<br>
                </div>
            </div>
            <div v-else>
                {{ winner || i18n.t('instruction.' + (firstscore > secondscore ? 'leftplayer' : 'rightplayer')) }} {{ i18n.t('ponggameview.wonthegame') }}<br>
            </div>
            [ {{ firstscore }} : {{ secondscore }} ]<hr>
        </div>
        {{ i18n.t('ponggameview.press') }}<img width="90" src="../../assets/img/Space_Key.svg" :alt="useI18n().t('instruction.spacebar')" :title="useI18n().t('instruction.spacebar')"/>{{ i18n.t('ponggameview.tocontinue') }}
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const i18n = useI18n()
const props = defineProps(['winner', 'firstscore', 'secondscore', 'ai'])
</script>
