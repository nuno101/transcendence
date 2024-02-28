<script>
    export default {
        props: {
            message: Object
        },
    }
</script>

<template>
    <a>{{ message.id }} {{ message.created_at }} {{ message.author_id }} {{ message.content }}</a>
</template>