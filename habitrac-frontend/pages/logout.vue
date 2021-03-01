<template>
  <div class="flex items-center justify-center min-h-screen">
    <div class="text-3xl tracking-wide text-center text-green-300 sm:text-5xl">
      You have been logged out!
    </div>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'
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
        this.deleteUserMutation()
        this.constructNavbarElementsAction()
      })
  },
  methods: {
    ...mapActions({
      constructNavbarElementsAction: 'navbar/constructNavbarElements',
    }),
    ...mapMutations({
      deleteUserMutation: 'user/deleteUser',
    }),
  },
}
</script>
