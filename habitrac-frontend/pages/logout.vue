<template>
  <div>You have been logged out!</div>
</template>

<script>
export default {
  mounted() {
    this.$apolloHelpers.onLogout()
  },
}
</script>
