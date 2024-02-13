

<template>
    <main>
        <div class="auth">
            <form class="authform" @submit.prevent="signupFormSubmit">
                <img class="logo" src="../assets/logo.png">
                <div class="text-centre">
                    <h3>Signup Page</h3>
                </div>

                <input class="inputItem" type="email" placeholder="email" v-model="email" required>
                <input class="inputItem" type="password" placeholder="password" v-model="password" required>

                <div class="button_inline">
                    <router-link to="/login">
                        <button type="button"> Login </button>
                    </router-link>

                    <button type="submit"> Create Account</button>
                </div>

            </form>

            <p class="status" v-if="status== 'successful-email-link' "> Registration successful , check Email for verification link</p>

        </div>

    </main>
</template>
  
  
<script>
import axios from 'axios';
import { RouterLink } from 'vue-router'
import {config} from '../config'
export default {
    data() {
        return {
            email: '',
            password: '',
            status : '',
        }
    },
    computed: {

    },
    methods: {
        signupFormSubmit: async function () {
            this.status = ''
            if (this.email && this.password) {
                const postdata = {
                    email: this.email,
                    password: this.password
                }
                const response = await axios.post(`${config.backendUrl}/auth/signup/`, postdata);
                if(response.status == 201 && response.data.message =='Verification email sent' ){
                    this.status = 'successful-email-link'
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