<template>
  <div class="flex items-center justify-center min-h-screen">
    <div class="text-3xl tracking-wide text-center sm:text-5xl">
      You have been logged out!
    </div>
  </div>
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
