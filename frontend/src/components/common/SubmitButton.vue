<template>
    <button class="w-100 mb-2 btn btn-lg rounded-3 btn-primary" type="submit">
    <div v-if="loading">
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span role="status">Loading...</span>
    </div>
    <div v-else><slot></slot></div>
</button>
</template>

<script setup>
    defineProps({ loading: Boolean })
</script>
