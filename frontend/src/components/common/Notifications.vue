<template>
<div class="dropdown">
    <button type="button" 
        class="btn btn-outline-light px-2"
        data-bs-toggle="dropdown"
        aria-expanded="false"
        @click="toggleDropdown"
    >
        <i class="bi bi-bell-fill"></i>
        <span v-if="filteredEvents.length > 0 && !dropdownShown"
            class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger text-light">
            {{filteredEvents.length}}<span class="visually-hidden">unread messages</span>
        </span>
    </button>
    <ul class="dropdown-menu" @click="toggleDropdown">
      <li v-for="(item, index) in filteredEvents" :key="index">
        <div class="text-center">{{ JSON.parse(item).payload.content }}</div>
        <div v-if="index !== filteredEvents.length - 1" class="dropdown-divider"></div>
      </li>
      <!-- ALTE EVENTS -->
    </ul>
</div>
</template>

<script setup>
import Backend from "../../js/Backend"
import { ref, computed } from 'vue'
import { watch, onMounted } from "vue"
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle'
import MyWebSocket from "../../js/Websocket"

let dropdownShown = ref(false);

watch(() => MyWebSocket.m.value, () => {
  // Do something here
  console.log(MyWebSocket.m.value);
});

const filteredEvents = computed(() => {
  return MyWebSocket.m.value.filter(item => {
    const parsedItem = JSON.parse(item);
    return parsedItem.event === 'create_notification';
  });
});

// neue anhängen, alten vom Endpoint nach dem 1. Refresh
// pro event neue funktion
// wenn auf gleicher Seite --> reload required alert (?)
function toggleDropdown() {
  dropdownShown.value = !dropdownShown.value;
}

</script>

<style scoped>
</style>
