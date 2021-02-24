<template>
  <div class="flex items-center justify-center min-h-screen">
    <div class="text-3xl tracking-wide text-center sm:text-5xl">
      You have been logged out!
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import deleteAuthTokenAction from '~/apollo/mutations/deleteAuthToken.gql'

export default {
  head: () => ({
    title: 'Logout',
  }),
  mounted() {
    const authToken = this.$apolloHelpers.getToken()
    this.$apollo
      .mutate({
        mutation: deleteAuthTokenAction,
        variables: {
          token: authToken,
        },
      })
      .then(() => {
        this.$apolloHelpers.onLogout()
        this.constructNavbarElementsAction()
      })
  },
  methods: {
    ...mapActions({
      constructNavbarElementsAction: 'navbar/constructNavbarElements',
    }),
  },
}
</script>
