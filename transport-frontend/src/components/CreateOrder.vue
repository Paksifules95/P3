<template>
  <div>
    <h2>Create New Order</h2>
    <form @submit.prevent="submitOrder">
      <div>
        <label for="orderNumber">Order Number:</label>
        <input id="orderNumber" v-model="order.order_number" required />
      </div>
      <div>
        <label for="customerName">Customer Name:</label>
        <input id="customerName" v-model="order.customer_name" required />
      </div>
      <div>
        <label for="date">Date:</label>
        <input id="date" type="date" v-model="order.date" required />
      </div>

      <h3>Waypoints</h3>
      <div v-for="(wp, index) in order.waypoints" :key="index">
        <input v-model="wp.location" placeholder="Location" required />
        <select v-model="wp.waypoint_type" required>
          <option disabled value="">Select type</option>
          <option value="pickup">Pickup</option>
          <option value="delivery">Delivery</option>
        </select>
        <button type="button" @click="removeWaypoint(index)">Remove</button>
      </div>
      <button type="button" @click="addWaypoint">Add New Waypoint</button>

      <button type="submit">Submit Order</button>
    </form>
  </div>
</template>

<script>
import { reactive } from 'vue'
import axios from 'axios'

export default {
  name: 'CreateOrder',
  setup() {
    const order = reactive({
      order_number: '',
      customer_name: '',
      date: '',
      waypoints: [
        { location: '', waypoint_type: '' }
      ]
    })

    function addWaypoint() {
      order.waypoints.push({ location: '', waypoint_type: '' })
    }

    function removeWaypoint(index) {
      order.waypoints.splice(index, 1)
    }

    async function submitOrder() {
      console.log('submitOrder function called')
      console.log('Form data:', JSON.stringify(order, null, 2))
      
      if (!order.order_number || !order.customer_name || !order.date) {
        console.error('Required fields missing')
        return
      }
      
      // Check if all waypoints have location and type
      for (let i = 0; i < order.waypoints.length; i++) {
        if (!order.waypoints[i].location || !order.waypoints[i].waypoint_type) {
          console.error('Waypoint missing required fields')
          return
        }
      }
      
      try {
        console.log('Sending POST request to:', 'http://localhost:8000/api/orders/')
        const response = await axios.post('http://localhost:8000/api/orders/', order)
        console.log('Response received:', response)
        console.log('Order created successfully:', response.data)
        order.order_number = ''
        order.customer_name = ''
        order.date = ''
        order.waypoints = [{ location: '', waypoint_type: '' }]
      } catch (error) {
        console.error('Error details:', error)
        if (error.response) {
          console.error('Server responded with:', error.response.status, error.response.data)
        } else if (error.request) {
          console.error('No response received from server')
        } else {
          console.error('Error setting up request:', error.message)
        }
      }
    }

    return { order, addWaypoint, removeWaypoint, submitOrder }
  }
}
</script>
