<script setup>
import { onMounted, defineProps, ref} from 'vue';
import { useI18n } from 'vue-i18n'
import Backend from '../../js/Backend';

const i18n = useI18n()

const props = defineProps({
  id: Number,
  size: {
    type: Number,
    default: 50
  }
});

const avatar = ref({});
const isLoaded = ref(false);

const fetchAvatar = async () => {
    try {
      avatar.value = await Backend.getAvatar(`/api/users/${props.id}/avatar`);
    } catch (error) {
      console.error(error.message);
    } finally {
    isLoaded.value = true;
  }
};

onMounted(() => {
    fetchAvatar();
})
</script>

<template>
  <img v-if="isLoaded" :src="avatar"
    :alt="i18n.t('avatar')"
    class="img-thumbnail rounded"
    :style="{ width: props.size + 'px', height: props.size + 'px', objectFit: 'cover' }"
  >
</template>