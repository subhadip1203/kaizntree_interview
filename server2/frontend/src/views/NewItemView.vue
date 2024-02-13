

<template>
  <div class="container">
    <div class="sidebar">
      <SidebarMenu />
    </div>

    <div style="display: flex; flex-direction: column; padding: 10px ; width: 100%;">
      <div class="heading">
        <div>
          <h2> Add New Product Category</h2>
        </div>

        <div style="margin-right: 5px;">
          <div> Total Category </div>
        </div>

      </div>

      <div class="itemBox">

        <form @submit.prevent="createItemSubmit">
          Item Name
          <input type="text" v-model="name" required />

          Item SKU
          <input type="text" v-model="sku" required />

          Item Category
          <select v-model="category" required>
            <option value="">-- Select Item Category --</option>
            <option v-for="cat in existing_categories" :value="cat.id">{{ cat.name }}</option>
          </select>

          Item Tags (Example : tag1 , tag2)
          <input type="text" v-model="tags" required />

          Item Actual stocks
          <input type="text" v-model="instock" required />

          Item Available stocks
          <input type="text" v-model="available_stock" required />

          <button type="submit">Create</button>
        </form>

        <p v-if="status == 'processing'"> processing .......</p>
        <p v-if="status == 'successfuly added'" style="color:green"> New Item added successfully</p>
      </div>

    </div>

  </div>
</template>


<script>
import axios from 'axios';
import SidebarMenu from '../components/SidebarMenu.vue'
import { config } from '../config'

export default {
  components: {
    SidebarMenu,
  },
  data() {
    return {
      existing_categories: [],
      accessToken: '',
      name: '',
      sku: '',
      category: '',
      tags: '',
      instock: '',
      available_stock: '',
      status: ''
    };
  },
  methods: {
    createItemSubmit: async function () {
      try {
        this.status = 'processing'

        if (this.category) {
          const axiosConfig = {
            headers: { Authorization: `Bearer ${this.accessToken}` }
          };
          const postdata = {
            name: this.name,
            sku: this.sku,
            category: this.category,
            tags: this.tags,
            instock: this.instock,
            available_stock: this.available_stock,
          }
          const response = await axios.post(`${config.backendUrl}/products/items/`, postdata, axiosConfig);
          if (response.status == 201) {
            this.status = 'successfuly added'
          } else {
            this.status = '='
          }
        } else {
          this.status = '='
        }
      } catch (err) {
        console.log(err)
        this.status = '='
        if (err.response.status == 401) {
          this.$router.push({ path: '/login' })
        }
      }
    }
  },
  mounted: async function () {
    try {
      const accessToken = sessionStorage.getItem("accessToken");
      if (accessToken) {
        this.accessToken = accessToken
        const axiosConfig = {
          headers: { Authorization: `Bearer ${accessToken}` }
        };
        // get all category
        const response = await axios.get(`${config.backendUrl}/products/categories/`, axiosConfig);
        if (response.status == 401) this.$router.push({ path: '/login' })
        if (response.status == 200) {
          this.existing_categories = [...response.data]
        }
      } else {
        this.$router.push({ path: '/login' })
      }

    } catch (err) {
      console.log(err)
      if (err.response.status == 401) {
        this.$router.push({ path: '/login' })
      }
    }

  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 100%;
  padding: 5px;
  border: 1px solid grey;
  border-radius: 10px;
}

.sidebar {
  width: 185px;
  margin-right: 10px;
}

button {
  height: 34px;
  width: 200px;
  font-size: 17px;
  background-color: #a8e0a8;
  border: 1px solid #a8e0a8;
  border-radius: 8px;
  cursor: pointer;
  margin: 5px;
}

.heading {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: space-between;
  margin: 5px;
}

.itemBox {
  border: 1px solid grey;
  border-radius: 8px;
  margin-top: 30px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  width: 100%;
}

.itemBox p {
  margin-top: 15px;
  color: grey;
}

.itemBox form {
  display: flex;
  flex-direction: column;
}


.itemBox form input {
  height: 31px;
  border: 1px solid grey;
  border-radius: 6px;
  margin-bottom: 10px;
}

.itemBox form select {
  height: 31px;
  border: 1px solid grey;
  border-radius: 6px;
  margin-bottom: 10px;
}
</style>