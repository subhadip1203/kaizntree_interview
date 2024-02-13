

<template>
    <main>
        <div class="auth">
            
            <p class="status" v-if="status == 'Pending'"> Processing ...... </p>
            <p class="status" v-if="status == 'Successful'"> Succesful, go to <router-link to="/login"> Login page </router-link>  ...... </p>
            <p class="status" v-if="status == 'falied'"> Falied ...... </p>
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
            status: 'Pending',
        }
    },
    computed: {

    },
    methods: {

    },
    mounted: async function () {
        this.status = 'Pending'
        try {
            const token = new URL(location.href).searchParams.get('token')
            if (token) {
                const response = await axios.get(`${config.backendUrl}/auth/verify-email/?token=`+token);
                console.log(response)
                if (response.status == 200) {
                    this.status = 'Successful'
                } else{
                    this.status = 'falied'
                }
            }else{
                this.status = 'falied'
            }

        } catch (err) {
            console.log(err)
        }
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