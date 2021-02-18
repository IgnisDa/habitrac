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
            :icon="['fas', 'sign-in-alt']"
          ></FontAwesomeIcon>
        </div>
        <form class="w-72" @submit.prevent="onSubmit()">
          <div class="mt-2 mb-5 sm:mt-0">
            <label for="username" class="block text-black dark:text-gray-100">
              Username
            </label>
            <div
              class="flex items-center p-3 my-2 bg-gray-100 border rounded-sm focus-within:ring-2 focus-within:ring-blue-600"
            >
              <FontAwesomeIcon
                class="flex-none w-6 h-6 text-black pointer-events-none fill-current"
                :icon="fieldIcons.username"
              ></FontAwesomeIcon>
              <input
                id="username"
                v-model="credentials.username"
                type="text"
                class="w-full ml-2 bg-gray-100 border-0 focus:outline-none"
                placeholder="Username"
                required
              />
            </div>
          </div>
          <div class="my-5">
            <label for="password1" class="block text-black dark:text-gray-100">
              Password
            </label>
            <div
              class="flex items-center p-3 my-2 bg-gray-100 border rounded-sm ring-black focus-within:ring-2 focus-within:ring-blue-600"
            >
              <FontAwesomeIcon
                class="flex-none w-6 h-6 text-black cursor-pointer fill-current"
                :icon="fieldIcons.password"
                @click="togglePasswordVisibility('password')"
              ></FontAwesomeIcon>
              <input
                id="password1"
                v-model="credentials.password"
                :type="fieldTypes.password"
                class="w-full ml-2 bg-gray-100 border-0 focus:outline-none"
                placeholder="Password"
                required
              />
            </div>
          </div>
          <button
            type="submit"
            2
            class="block w-full p-3 text-center text-white duration-300 bg-gray-800 rounded-sm hover:bg-black dark:bg-green-700"
          >
            Login
          </button>
        </form>
      </div>
      <div class="hidden p-5 align-top border-2 border-l-0 rounded sm:block">
        <FontAwesomeIcon
          class="w-32 h-32 transition-colors duration-500 fill-current"
          :icon="['fas', 'sign-in-alt']"
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
      password: 'test-password',
    },
    loading: false,
    fieldTypes: {
      password: 'password',
    },
    fieldIcons: {
      password: ['fas', 'eye'],
      username: ['fas', 'user'],
    },
  }),
  head: () => ({
    title: 'Login',
  }),
  methods: {
    ...mapActions({
      fetchTokenAuthAction: 'user/fetchTokenAuth',
      fetchUserDetailsAction: 'user/fetchUserDetails',
    }),
    togglePasswordVisibility(fieldName) {
      this.fieldTypes[fieldName] =
        this.fieldTypes[fieldName] === 'password' ? 'text' : 'password'
      this.fieldIcons[fieldName] =
        this.fieldIcons[fieldName] === 'eye-slash' ? 'eye' : 'eye-slash'
    },
    async onSubmit() {
      // I initially thought that we do not need `async`-`await` here, but then it didn't
      // work so I added them and it suddenly started working. Reason: We have to first
      // await the response of the `fetchTokenAuthAction` and then, when the authentication
      // token is set in the site cookies, we perform `fetchUSerDetailsAction` with the
      // newly set token present in the request header and get a successful response.
      this.loading = true
      await this.fetchTokenAuthAction(this.credentials)
      await this.fetchUserDetailsAction()
      this.loading = false
    },
  },
}
</script>
