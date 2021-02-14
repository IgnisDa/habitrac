<template>
  <div>You have been logged out!</div>
</template>

<script>
export default {
  head: () => ({
    title: 'Logout',
  }),
  mounted() {
    this.$apolloHelpers.onLogout()
  },
}
</script>
