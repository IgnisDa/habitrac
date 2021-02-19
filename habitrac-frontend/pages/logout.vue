<template>
  <div>You have been logged out!</div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  head: () => ({
    title: 'Logout',
  }),
  mounted() {
    this.$apolloHelpers.onLogout()
    this.constructNavbarElementsAction()
  },
  methods: {
    ...mapActions({
      constructNavbarElementsAction: 'navbar/constructNavbarElements',
    }),
  },
}
</script>
