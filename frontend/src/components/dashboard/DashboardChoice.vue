<script setup>
</script>

<template>
    <h1 class="text-primary">THIS IS THE HOME PAGE</h1>
    <div>
        <router-link to="/friends">Friends</router-link><br>
        <router-link to="/game">Play Pong Game</router-link><br>
        <router-link to="/tournaments">Tournaments</router-link><br>
    </div>
    <br>
    <div>
        <router-link to="/profile">Profile</router-link><br>
        <router-link to="/settings">Settings</router-link><br>
        <router-link to="/">Logout</router-link>
    </div>
</template>