<template>
  <div class="text-center">
    <div class="form-signin">
      <form @submit.prevent="LogIn">
        <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
    
        <div class="form-floating">
          <input type="text" class="form-control" id="floatingInput" placeholder="Username" v-model="input.username">
          <label for="floatingInput">Username</label>
        </div>
        <div class="form-floating">
          <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="input.password">
          <label for="floatingPassword">Password</label>
        </div>
    
        <div class="checkbox mb-3">
          <label>
            <input type="checkbox" value="remember-me"> Remember me
          </label>
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
      </form>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue'
import Backend from '../js/Backend'

const input = ref({username: '', password: ''})

const LogIn = async () => {
  try {
    let data = await Backend.post('/api/login', input.value)
    console.log(data)
  } catch (err) {
    console.log(err.message)
  }

  try {
    let data = await Backend.get('/api/tournaments')
    console.log(data)
  } catch (err) {
    console.log(err.message)
  }
}
</script>

<style>
  @import url('../assets/signin.css');
</style>



