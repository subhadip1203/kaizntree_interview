

<template>
  <div class="container">
    <div class="sidebar">
      <SidebarMenu />
    </div>

    <div style="display: flex; flex-direction: column; padding: 10px ; width: 100%;">
      <div class="heading">
        <div>
          <h2> Item Dashbaord </h2>
          <p style="margin-bottom: 20px;"> All Items</p>
          <button @click="addNewCategory"> Add Item Category</button>
        </div>

        <div style="margin-right: 5px;">
          <div> Total Category : {{ categories.length }}</div>
          <div> Total Items : {{ totalItemCount }} </div>
        </div>

      </div>

      <div class="itemBox">

        <div class="actionArea">
          <button :disabled='categories.length == 0' @click="addNewItem"> New Item</button>
          <input type="text" class="searchBox" placeholder="Search tags ..." v-model="keyword" />
          <img src="../assets/filter.png" height="40px" />
        </div>
        <div class="dataArea">
          <div class="box-head">
            <div style="width: 3%;"> <input type="checkbox" value="all"> </div>
            <div style="width: 8%;">SKU</div>
            <div style="width: 30%;">Name</div>
            <div style="width: 10%;">Tags</div>
            <div style="width: 20%;">Category</div>
            <div style="width: 15%;">In Stock</div>
            <div style="width: 15%;">Available Stock</div>
          </div>
          <div class="box-content" v-for="(item, index) in loadedItems" key="index">
            <div style="width: 3%;"> <input type="checkbox" :id="`item${index}`" value="yes"></div>
            <div style="width: 8%;">{{ item.sku }}</div>
            <div style="width: 30%;">{{ item.name }}</div>
            <div style="width: 10%;">{{ item.tags }}</div>
            <div style="width: 20%;">{{ category_obj[item.category] || '-' }}</div>
            <div style="width: 15%;">{{ item.instock }}</div>
            <div style="width: 15%;">{{ item.available_stock }}</div>

          </div>
        </div>
      </div>
      <div class="prev-next">
        <button :disabled="!itemPaginationPrev" @click="prevItems"> Previous Items</button>
        <button :disabled="!itemPaginationNext" @click="nextItems"> Next Items </button>
      </div>

    </div>

  </div>
</template>


<script>
import axios from 'axios';
import SidebarMenu from '../components/SidebarMenu.vue'
import { config } from '../config'
import debounce from 'lodash.debounce'

export default {
  components: {
    SidebarMenu,
  },
  data() {
    return {
      accessToken: '',
      categories: [],
      category_obj: {},
      totalItemCount: 0,
      loadedItems: [],
      itemPaginationPrev: '',
      itemPaginationNext: '',

      // search keyword
      keyword: ''
    };
  },
  watch: {
    keyword: debounce(function () {
      console.log("run....")
      this.keyword_update()
    }, 500)
  },
  methods: {


    addNewCategory: function () {
      this.$router.push({ path: '/add-category' })
    },
    addNewItem: function () {
      this.$router.push({ path: '/add-item' })
    },

    keyword_update: async function () {
      // get items with  tag 
      const axiosConfig = {
        headers: { Authorization: `Bearer ${this.accessToken}` }
      };
      const response_item = await axios.get(`${config.backendUrl}/products/items/?tag=${this.keyword}`, axiosConfig);
      console.log(response_item)
      if (response_item.status == 200) {
        this.totalItemCount = response_item.data.count
        this.loadedItems = [...response_item.data.results]
        this.itemPaginationPrev = response_item?.data?.previous?.split('api')[1] || null
        this.itemPaginationNext = response_item?.data?.next?.split('api')[1] || null
      }
    },

    prevItems: async function () {
      try {
        // get all items
        const axiosConfig = {
          headers: { Authorization: `Bearer ${this.accessToken}` }
        };
        const response_item = await axios.get(`${config.backendUrl}${this.itemPaginationPrev}`, axiosConfig);
        console.log(response_item)
        if (response_item.status == 200) {
          this.totalItemCount = response_item.data.count
          this.loadedItems = [...response_item.data.results]
          this.itemPaginationPrev = response_item?.data?.previous?.split('api')[1] || null
          this.itemPaginationNext = response_item?.data?.next?.split('api')[1] || null
        }
      } catch (err) {
        console.log(err)
        if (err.response.status == 401) {
          this.$router.push({ path: '/login' })
        }
      }
    },

    nextItems: async function () {
      try {
        // get all items
        const axiosConfig = {
          headers: { Authorization: `Bearer ${this.accessToken}` }
        };
        const response_item = await axios.get(`${config.backendUrl}${this.itemPaginationNext}`, axiosConfig);
        console.log(response_item)
        if (response_item.status == 200) {
          this.totalItemCount = response_item.data.count
          this.loadedItems = [...response_item.data.results]
          this.itemPaginationPrev = response_item?.data?.previous?.split('api')[1] || null
          this.itemPaginationNext = response_item?.data?.next?.split('api')[1] || null
        }
      } catch (err) {
        console.log(err)
        if (err.response.status == 401) {
          this.$router.push({ path: '/login' })
        }
      }
    },

    serachKeyword: async function () {
      try {

        if (this.keyword) {
          console.log(this.keyword)
          // get all items
          const axiosConfig = {
            headers: { Authorization: `Bearer ${this.accessToken}` }
          };
        }

      } catch (err) {
        console.log(err)
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
        const response_category = await axios.get(`${config.backendUrl}/products/categories/`, axiosConfig);
        if (response_category.status == 200) {
          this.categories = [...response_category.data]
          for (const cat of response_category.data) {
            this.category_obj[cat.id] = cat.name
          }
        }

        // get all items
        const response_item = await axios.get(`${config.backendUrl}/products/items/`, axiosConfig);
        console.log(response_item)
        if (response_item.status == 200) {
          this.totalItemCount = response_item.data.count
          this.loadedItems = [...response_item.data.results]
          this.itemPaginationPrev = response_item?.data?.previous?.split('api')[1] || null
          this.itemPaginationNext = response_item?.data?.next?.split('api')[1] || null
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

.actionArea {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: space-between;
}

.searchBox {
  border: 0px;
  border-bottom: 1px solid grey;
  width: 254px;
}

.searchBox:focus {
  outline: none !important;
}

.dataArea {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-top: 5px;
}

.box-head {
  display: flex;
  flex-direction: row;
  width: 100%;
  margin-bottom: 15px;
  margin-top: 15px;
  padding-top: 20px;
  border-top: 1px solid grey;
}

.box-content {
  display: flex;
  flex-direction: row;
  width: 100%;
  margin-bottom: 15px;
  margin-top: 15px;
  padding-top: 20px;
  border-top: 1px solid grey;
}

.prev-next {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-top: 10px;

}
</style>