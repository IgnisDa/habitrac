<template>
  <div class="container bg-red-100">
    <form @submit.prevent="onSubmit()">
      <input
        v-model="credentials.username"
        type="text"
        placeholder="username"
      />
      <input
        v-model="credentials.password"
        type="password"
        placeholder="password"
      />
      <input type="submit" value="Login" />
    </form>
  </div>
</template>

<script>
import tokenAuthMutation from '~/apollo/mutations/tokenAuth.gql'

export default {
  data: () => ({
    credentials: {
      username: 'test',
      password: 'test-password',
    },
  }),
  methods: {
    async onSubmit() {
      const credentials = this.credentials
      try {
        await this.$apollo
          .mutate({
            mutation: tokenAuthMutation,
            variables: {
              username: credentials.username,
              password: credentials.password,
            },
          })
          .then(({ data }) => {
            this.$apolloHelpers.onLogin(data.tokenAuth.token)
          })
      } catch (e) {
        alert('Invalid credentials!')
      }
    },
  },
}
</script>
