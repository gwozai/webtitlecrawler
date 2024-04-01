<template>
  <div>
    <p>{{ data }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      data: null
    }
  },
  mounted () {
    axios.get('http://localhost:5000/api/data')
      .then(response => (this.data = response.data))
  }
}
</script>