<template>
	<div class="border rounded overflow-scroll">
		<table class="table mb-0">
			<thead>
				<tr>
					<th class="text-center text-nowrap"><slot></slot></th>
				</tr>
			</thead>
			<tbody>
				<div class="m-3">
					<select v-model="input.type" class="form-select" aria-label="Default select example">
						<option value="ai">{{ i18n.t('aisettings.ai') }}</option>
						<option value="human">{{ i18n.t('aisettings.human') }}</option>
					</select>
					<div v-if="input.type === 'ai'" class="p-0">
						<h2 class="fs-6 mb-1 mt-3">{{ i18n.t('aisettings.includeincalculations') }}</h2>
						<div class="form-check form-switch mb-2">
							<input v-model="input.border" class="form-check-input" type="checkbox" role="switch" id="border">
							<label class="form-check-label" for="border">{{ i18n.t('aisettings.border') }}</label>
						</div>
						<div class="form-check form-switch mb-2">
							<input v-model="input.opponent" class="form-check-input" type="checkbox" role="switch" id="opponent">
							<label class="form-check-label" for="opponent">{{ i18n.t('aisettings.opponent') }}</label>
						</div>
						<div class="form-check form-switch mb-2">
							<input v-model="input.center" class="form-check-input" type="checkbox" role="switch" id="center">
							<label class="form-check-label" for="center">{{ i18n.t('aisettings.center') }}</label>
						</div>
						<figure class="figure mb-0">
							<label for="customRange1" class="form-label">
								{{ i18n.t('aisettings.inaccuracy') }}:<br>
								{{ parseFloat((input.inaccuracy / 50 - 1).toFixed(2)) }}
							</label>
							<input v-model="input.inaccuracy" type="range" class="form-range" id="customRange1">
							<figcaption class="figure-caption ms-3">
								{{ i18n.t('aisettings.explenation') }}<br>
								<strong>{{ i18n.t("aisettings.tip")}}: </strong>{{ i18n.t('aisettings.tipvalue') }}
							</figcaption>
						</figure>
					</div>
				</div>
			</tbody>
	  	</table>
	</div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const i18n = useI18n()
const input = defineModel('input')
</script>
