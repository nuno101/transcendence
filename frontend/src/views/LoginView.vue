<script>

import router from '../router/index.js';
import { PostData } from '../js/PostData.js';

export default {
  name: 'login',
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    LogIn() {
      PostData('http://localhost:8000/login', {"name": this.username, "password": this.password})
        .then(data => {
          console.log('login:', data.message)
          router.push('/dashboard')
        })
        .catch(err => {
          console.log('login:', err.message)
          alert('wrong password')
        })
    }
  }
}
</script>

<template>
  <div class="text-center">
    <div class="form-signin">
      <form @submit.prevent="LogIn">
        <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
    
        <div class="form-floating">
          <input type="text" class="form-control" id="floatingInput" placeholder="Username" v-model="username">
          <label for="floatingInput">Username</label>
        </div>
        <div class="form-floating">
          <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password">
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

<style>
  @import url('../assets/signin.css');
</style>



