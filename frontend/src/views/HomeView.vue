<script setup>
import AuthChoice from '../components/auth/AuthChoice.vue';
import Loading from '../components/common/Loading.vue'
import { ref } from 'vue'

const loaded = ref(false)

const foo = async () => {
  await new Promise(resolve => setTimeout(resolve, 2000));
  loaded.value = true
}
foo()

</script>

<template>
  <main>
    <AuthChoice v-if="loaded" />
    <Loading v-else />
  </main>
</template>

<style></style>