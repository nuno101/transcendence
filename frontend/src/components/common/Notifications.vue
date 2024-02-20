<template>
<div class="dropdown">
    <button type="button" 
        class="btn btn-outline-light px-2"
        data-bs-toggle="dropdown"
        aria-expanded="false"
        @click="toggleDropdown"
    >
        <i class="bi bi-bell-fill"></i>
        <span v-if="Notifications.messages.value.length > 0 && dropdownShown > 0"
            class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger text-light">
            {{dropdownShown}}<span class="visually-hidden">unread messages</span>
            <audio ref="notificationSoundRef" :src="`../../assets/audio/notification.mp3`" preload="none" muted="muted"></audio>
        </span>
    </button>
    <ul class="dropdown-menu" @click="toggleDropdown">
        <li class="text-center" v-if="storedNotifications.length <= 0 && Notifications.messages.value.length <= 0">No notifications</li>
        <li v-for="(item, index) in Notifications.messages.value.slice().reverse()" :key="index">
          <div class="text-center">{{ item }}</div>
          <div v-if="storedNotifications.length > 0" class="dropdown-divider"></div>
        </li>
        <li v-for="(item, index) in storedNotifications.slice().reverse()" :key="index">
            <div class="text-center">{{ item.content }}</div>
            <div v-if="index !== storedNotifications.length - 1" class="dropdown-divider"></div>
        </li>
    </ul>
</div>
</template>

<script setup>
import Backend from "../../js/Backend"
import Notifications from "../../js/Notifications"
import notificationSound from '../../assets/audio/notification.mp3'
import { ref } from 'vue'
import { watch, onMounted } from "vue"

let dropdownShown = ref(0);
const storedNotifications = ref([]);
const isLoaded = ref(false);
const notificationSoundRef = ref(null);

onMounted(() => {
  fetchData();
})

const fetchData = async () => {
  try {
    isLoaded.value = false;
    storedNotifications.value = await Backend.get('/api/users/me/notifications');
    console.log(storedNotifications.value);
  } catch (err) {
    console.error(err.message);
  } finally {
    isLoaded.value = true;
  }
};

watch(() => Notifications.messages.value, () => {
  dropdownShown.value++;
  if (dropdownShown.value > 0) {
    playNotificationSound();
  }
});

function toggleDropdown() {
  dropdownShown.value = 0;
}

function playNotificationSound() {
  console.log(notificationSoundRef.value);
  console.log(notificationSoundRef);
  const audio = new Audio (notificationSound);
  audio.muted = true;
    audio.play().catch((error) => {
      console.error('Error playing audio:', error);
    });
  // if (audio) {
  //   console.log("PLAYED");
  // }
  // else
  //   console.log("NOT PLAYED");
}
</script>

<style scoped>

.dropdown-menu {
  max-height: 196px;
  overflow-y: auto;
}

</style>
