<template>
  <div class="jumping-ball">
    <svg
      width="100"
      height="100"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 100 100"
    >
      <circle cx="50" cy="50" r="15" fill="blue" />
    </svg>
  </div>
</template>

<script setup>
</script>

<style scoped>
/* Add styles for the jumping ball here if needed */
.jumping-ball {
  position: relative;
  animation: jump 1s infinite alternate;
}

@keyframes jump {
  to {
    transform: translateY(-20px);
  }
}
</style>