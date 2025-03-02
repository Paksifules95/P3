<template>
    <div>
      <h2>Order List</h2>
      <ul>
        <li v-for="order in orders" :key="order.id">
          <strong>{{ order.order_number }}</strong> - {{ order.customer_name }} ({{ order.date }})
          <ul>
            <li v-for="wp in order.waypoints" :key="wp.id">
              {{ wp.location }} - {{ wp.waypoint_type }}
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  export default {
    name: 'OrderList',
    setup() {
      const orders = ref([])
  
      // Load orders from backend
      async function fetchOrders() {
        try {
          const response = await axios.get('http://localhost:8000/api/orders/')
          orders.value = response.data
        } catch (error) {
          console.error('Error fetching orders:', error)
        }
      }
  
      onMounted(() => {
        fetchOrders()
      })
  
      return { orders }
    }
  }
  </script>
  