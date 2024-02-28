<script>
    export default {
        props: {
            channel: Object
        },
    }
</script>

<template>
    <a class="<a list-group-item list-group-item-action py-3 lh-sm>" @click="$emit('channelSelected')">
        <div class="d-flex w-100 align-items-center justify-content-between">
            <strong class="mb-1">
                {{ channel.name }}
            </strong>
        </div>
        <div class="col-10 mb-1 small">
            {{ channel.updated_at }}
        </div>
    </a>
</template>