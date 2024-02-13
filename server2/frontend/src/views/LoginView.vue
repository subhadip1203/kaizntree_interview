

<template>
  <main>
    <div class="auth">
      <form class="authform" @submit.prevent="loginFormSubmit">
        <img class="logo" src="../assets/logo.png">
        <div class="text-centre">
          <h3>Login Page</h3>
        </div>

        <input class="inputItem" type="email" placeholder="email" v-model="email" required>
        <input class="inputItem" type="password" placeholder="password" v-model="password" required>

        <div class="button_inline">
          <router-link to="/signup">
            <button type="button"> Create Account </button>
          </router-link>

          <button type="submit"> Login </button>
        </div>

      </form>

      <p class="status" v-if="status == 'login-successful'"> Login successful </p>

    </div>

  </main>
</template>


<script>
import axios from 'axios';
import { RouterLink } from 'vue-router'
import { config } from '../config'
export default {
  data() {
    return {
      email: '',
      password: '',
      status: '',
    }
  },
  computed: {

  },
  methods: {
    loginFormSubmit: async function () {
      this.status = ''
      if (this.email && this.password) {
        const postdata = {
          username: this.email,
          password: this.password
        }
        const response = await axios.post(`${config.backendUrl}/auth/login/`, postdata);
        if (response.status == 200 && response.data.access_token.length > 10) {
          this.status = 'login-successful'
          sessionStorage.setItem("accessToken", response.data.access_token);
          this.$router.push({ path: '/' })
        }
      }
    }

  },
  mounted() {

  },
}


</script>

<style scoped>
.auth {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
  width: 100%
}

.authform {
  display: flex;
  flex-direction: column;
}

.text-centre {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.inputItem {
  margin-top: 15px;
}

.button_inline {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-top: 15px;
}

button {
  height: 30px;
}

.logo {
  width: 220px;
  height: 55px;
}

.status {
  margin-top: 13px;
  color: green;
}
</style>