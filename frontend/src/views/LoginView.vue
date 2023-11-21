<template>
  <div>
    <h1>LOGIN</h1>
    <h3>42 API</h3>
    <p>or</p>
    <h3>GOOGLE</h3>
    <p>or</p>
    <h3>E-MAIL</h3>
    <input type="email" class="form-control" id="email">
    <h3>PASSWORD</h3>
    <input type="password" class="form-control" id="password">
    <br>
    <router-link to="/dashboard">
      <button type="button" class="btn btn-success">LOGIN</button>
    </router-link>
  </div>
</template>

<style>
</style>
