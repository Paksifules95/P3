<template>
  <div id="app">
    <h1>Transport Management System</h1>
    <CreateOrder />
    <OrderList />
  </div>
</template>

<script>
import CreateOrder from './components/CreateOrder.vue'
import OrderList from './components/OrderList.vue'

export default {
  name: 'App',
  components: {
    CreateOrder,
    OrderList
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
