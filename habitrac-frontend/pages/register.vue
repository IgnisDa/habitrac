<template>
  <div class="container bg-red-100">
    <form @submit.prevent="onSubmit()">
      <input
        v-model="credentials.username"
        type="text"
        placeholder="username"
        required
      />
      <input
        v-model="credentials.password"
        type="password"
        placeholder="password"
        required
      />
      <div class="w-1/2">
        <FontAwesomeIcon
          class="w-20 h-20 mx-auto"
          :class="loading ? 'animate-spin' : 'animate-none'"
          :icon="['fas', 'users']"
        ></FontAwesomeIcon>
      </div>
      <input type="submit" value="Register" />
      {{ errors }}
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data: () => ({
    credentials: {
      username: 'test',
      password: 'test-password',
    },
    loading: false,
    errors: [],
  }),
  methods: {
    ...mapActions({
      createUserMutation: 'user/createUser',
    }),
    async onSubmit() {
      // I initially thought that we do not need `async`-`await` here, but then it didn't
      // work so I added them and it suddenly started working. Reason: We have to first
      // await the response of the `fetchTokenAuthAction` and then when the authentication
      // token is set in the site cookies, we perform `fetchUSerDetailsAction` with the
      // newly set token present in the request header and get a successful response.
      this.loading = true
      const res = await this.createUserMutation(this.credentials)
      if (!res.status) {
        this.errors = res.errors
      }
      this.loading = false
    },
  },
}
</script>
