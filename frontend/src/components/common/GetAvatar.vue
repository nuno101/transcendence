<script setup>
import { onMounted, defineProps, ref} from 'vue';
import Backend from '../../js/Backend';

const props = defineProps({
  id: Number,
  size: {
    type: Number,
    default: 50
  }
});

const avatar = ref({});
const isLoaded = ref(false);

const getAvatarById = async (id) => {
    try {
        const avatar = await Backend.getAvatar(`/api/users/${id}/avatar`);
        return avatar;
    } catch (err) {
        console.error(err.message);
        return null;
    }
};

const fetchAvatar = async () => {
    try {
        avatar.value = await getAvatarById(props.id);
    } catch (error) {
      console.error(`Error fetching avatar for player:`, error.message);
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
        alt="..."
        class="img-thumbnail rounded"
        :style="{ width: props.size + 'px', height: props.size + 'px', objectFit: 'cover' }">
</template>