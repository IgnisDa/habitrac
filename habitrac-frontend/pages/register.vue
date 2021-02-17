<template>
  <div class="w-full dark:bg-gray-800">
    <div
      class="container flex items-center justify-center min-h-screen mx-auto"
    >
      <div class="p-5 m-3 border-2 rounded-md shadow-lg sm:m-0">
        <div class="flex justify-center -mt-20 sm:hidden">
          <FontAwesomeIcon
            class="w-24 h-24 transition-colors duration-500 rounded-full fill-current"
            :class="{ 'text-yellow-400': loading }"
            :icon="['fas', 'user-plus']"
          ></FontAwesomeIcon>
        </div>
        <form class="w-72" @submit.prevent="onSubmit()">
          <div class="mt-2 mb-5 sm:mt-0">
            <label for="username" class="block text-black dark:text-gray-100"
              >Username</label
            >
            <input
              id="username"
              v-model="credentials.username"
              type="text"
              autofocus
              class="w-full px-4 py-3 mt-3 bg-gray-100 rounded-sm"
              placeholder="Username"
              required
            />
          </div>
          <div class="my-5">
            <label for="password1" class="block text-black dark:text-gray-100">
              Password
            </label>
            <input
              id="password1"
              v-model="credentials.password1"
              type="password"
              class="w-full px-4 py-3 mt-3 bg-gray-100 rounded-sm focus:outline-none"
              placeholder="Password"
              required
            />
          </div>
          <div class="my-5">
            <label for="password2" class="block text-black dark:text-gray-100">
              Confirm password
            </label>
            <input
              id="password2"
              v-model="credentials.password2"
              type="password"
              class="w-full px-4 py-3 mt-3 bg-gray-100 rounded-sm focus:outline-none"
              placeholder="Password"
              required
            />
            <div class="flex justify-end mt-2 text-xs text-gray-600">
              <a class="hover:text-blue-900 dark:text-gray-100">
                Forgot Password?
              </a>
            </div>
          </div>
          <button
            type="submit"
            class="block w-full p-3 text-center text-white duration-300 bg-gray-800 rounded-sm hover:bg-black dark:bg-green-700"
          >
            Register
          </button>
        </form>
      </div>
      <div class="hidden p-5 align-top border-2 border-l-0 rounded sm:block">
        <FontAwesomeIcon
          class="w-32 h-32 transition-colors duration-500 fill-current dark:text-green-700"
          :icon="['fas', 'user-plus']"
          :class="{ 'text-yellow-400': loading }"
        ></FontAwesomeIcon>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data: () => ({
    credentials: {
      username: 'test',
      password1: 'test-password',
      password2: 'test-password',
    },
    loading: false,
    errors: [],
  }),
  head: () => ({
    title: 'Register',
  }),
  methods: {
    ...mapActions({
      createUserMutation: 'user/createUser',
    }),
    async onSubmit() {
      const credentials = this.credentials

      if (credentials.password1 !== credentials.password2) {
        alert('The two passwords are different!')
        return
      }
      const finalCredentials = {
        username: credentials.username,
        password: credentials.password1,
      }

      // I initially thought that we do not need `async`-`await` here, but then it didn't
      // work so I added them and it suddenly started working. Reason: We have to first
      // await the response of the `fetchTokenAuthAction` and then when the authentication
      // token is set in the site cookies, we perform `fetchUSerDetailsAction` with the
      // newly set token present in the request header and get a successful response.
      this.loading = true
      const res = await this.createUserMutation(finalCredentials)
      if (!res.status) {
        this.errors = res.errors
      }
      this.loading = false
    },
  },
}
</script>
