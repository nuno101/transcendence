<template>
    <div class="d-flex justify-content-center align-items-center">
        <video class="rounded" loop autoplay muted>
            <source :src="gifUrl" type="video/mp4">
            not supported
        </video>
    </div>
</template>

<script setup>
const gifUrls = [
    'https://media.tenor.com/_U6dCguctMcAAAPo/naza-bart.mp4',
    'https://media.tenor.com/HBJsDrF5ABQAAAPo/fml-my.mp4',
    'https://media.tenor.com/cv7t69yhNYwAAAPo/peace-out-bye.mp4',
    'https://media.tenor.com/5P7B09VEneEAAAPo/respect-pirate.mp4',
    'https://media.tenor.com/PG9agp6LazAAAAPo/back-to.mp4',
]
const gifUrl = gifUrls[Math.floor(Math.random() * gifUrls.length)]
</script>

<style scoped>
    video {
        width: 100%;
        max-width: 25rem;
        min-width: 10rem;
    }
</style>
