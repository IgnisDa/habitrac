<template>
  <div class="flex items-center justify-center min-h-screen">
    <div class="text-3xl tracking-wide text-center sm:text-5xl">
      This is the test page!
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  middleware: ['onlyDevPage'],
  head: () => ({
    title: 'Test page',
  }),
  mounted() {
    this.$apolloHelpers.onLogout()
    this.constructNavbarElementsAction()
    this.$addAlert({
      severity: 'info',
      messageHeading: 'Logged Out',
      messageBody: 'You have been logged out successfully!',
      active: true,
    })
    this.$addAlert({
      severity: 'danger',
      messageHeading: 'Logged Out',
      messageBody: 'You have been logged out successfully!',
      active: true,
    })
    this.$addAlert({
      severity: 'success',
      messageHeading: 'Logged Out',
      messageBody: 'You have been logged out successfully!',
      active: true,
    })
    this.$disableAlert(2)
  },
  methods: {
    ...mapActions({
      constructNavbarElementsAction: 'navbar/constructNavbarElements',
    }),
  },
}
</script>
