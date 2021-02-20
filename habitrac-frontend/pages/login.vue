<template>
  <div class="w-full dark:bg-gray-800">
    <div
      class="container flex items-center justify-center min-h-screen mx-auto"
    >
      <div class="grid">
        <div class="col-start-1 row-end-2">
          <div
            class="w-full h-full transition-all duration-300 transform rounded-xl rotate-6"
            :class="[formErrorsExist ? 'bg-red-600' : 'bg-green-600']"
          ></div>
        </div>
        <div
          class="relative col-start-1 row-end-2 p-5 m-3 transition-colors duration-300 border rounded-md shadow-xl bg-gray-50 sm:m-0"
        >
          <div class="absolute"></div>
          <div
            class="pb-2 mb-8 text-3xl font-semibold tracking-wider text-center text-blue-500 transition-colors duration-500 border-b-4 border-blue-300 border-dashed sm:text-5xl"
            :class="{ 'text-yellow-400': loading }"
          >
            Login
          </div>
          <form class="w-72 sm:w-80 md:w-96" @submit.prevent="onSubmit()">
            <div class="mt-2 mb-5 sm:mt-0">
              <label
                for="username"
                class="block font-serif text-lg text-black dark:text-gray-100"
              >
                Username
              </label>
              <div
                class="flex items-center p-3 my-2 bg-gray-100 border rounded-sm focus-within:ring-2 focus-within:ring-blue-600"
                :class="[
                  errors.username
                    ? 'ring-2 ring-red-600'
                    : 'focus-within:ring-blue-600',
                ]"
              >
                <FontAwesomeIcon
                  class="flex-none w-6 h-6 text-black pointer-events-none fill-current"
                  :icon="fieldIcons.username"
                ></FontAwesomeIcon>
                <input
                  id="username"
                  ref="username"
                  v-model="credentials.username"
                  type="text"
                  class="w-full ml-2 bg-gray-100 border-0 focus:outline-none"
                  placeholder="Username"
                  required
                />
              </div>
              <transition name="errors">
                <ul
                  v-if="errors.username"
                  class="space-y-1 text-xs tracking-wider text-red-500"
                >
                  <li v-for="(error, index) in errors.username" :key="index">
                    {{ error }}
                  </li>
                </ul>
              </transition>
            </div>
            <div class="my-5">
              <label
                for="password"
                class="block font-serif text-lg text-black dark:text-gray-100"
              >
                Password
              </label>
              <div
                class="flex items-center p-3 my-2 bg-gray-100 border rounded-sm ring-black focus-within:ring-2 focus-within:ring-blue-600"
                :class="[
                  errors.password
                    ? 'ring-2 ring-red-600'
                    : 'focus-within:ring-blue-600',
                ]"
              >
                <FontAwesomeIcon
                  class="flex-none w-6 h-6 text-black cursor-pointer fill-current"
                  :icon="fieldIcons.password"
                  @click="togglePasswordVisibility('passwordOne')"
                ></FontAwesomeIcon>
                <input
                  id="password"
                  v-model="credentials.password"
                  :type="fieldTypes.password"
                  class="w-full ml-2 bg-gray-100 border-0 focus:outline-none"
                  placeholder="Password"
                  required
                />
              </div>
              <transition name="errors">
                <ul
                  v-if="errors.password"
                  class="space-y-1 text-xs tracking-wider text-red-500"
                >
                  <li v-for="(error, index) in errors.password" :key="index">
                    {{ error }}
                  </li>
                </ul>
              </transition>
            </div>
            <button
              type="submit"
              class="w-full p-3 text-lg font-semibold text-center text-indigo-700 uppercase bg-gray-200 rounded-sm focus:outline-none loading--button-border-red"
              :class="{ 'loading--button': loading }"
            >
              <span>Login</span>
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data: () => ({
    credentials: {
      username: '',
      password: '',
    },
    loading: false,
    fieldTypes: {
      password: 'password',
    },
    fieldIcons: {
      password: ['fas', 'eye'],
      username: ['fas', 'user'],
    },
    errors: { username: null, password: null },
  }),
  head: () => ({
    title: 'Login',
  }),
  computed: {
    formErrorsExist() {
      let exist = false
      for (const error in this.errors) {
        if (this.errors[error]) {
          exist = true
          break
        }
      }
      return exist
    },
  },
  mounted() {
    this.focusInput()
  },
  methods: {
    ...mapActions({
      fetchTokenAuthAction: 'user/fetchTokenAuth',
      fetchUserDetailsAction: 'user/fetchUserDetails',
    }),
    focusInput() {
      this.$refs.username.focus()
    },
    togglePasswordVisibility(fieldName) {
      this.fieldTypes[fieldName] =
        this.fieldTypes[fieldName] === 'password' ? 'text' : 'password'
      this.fieldIcons[fieldName] =
        this.fieldIcons[fieldName] === 'eye-slash' ? 'eye' : 'eye-slash'
    },
    async onSubmit() {
      this.errors = { username: null, password: null }
      // I initially thought that we do not need `async`-`await` here, but then it didn't
      // work so I added them and it suddenly started working. Reason: We have to first
      // await the response of the `fetchTokenAuthAction` and then, when the authentication
      // token is set in the site cookies, we perform `fetchUSerDetailsAction` with the
      // newly set token present in the request header and get a successful response.
      this.loading = true
      const res = await this.fetchTokenAuthAction(this.credentials)
      this.loading = false
      // The store returns `null` in the response if the login mutation is successful,
      // so we check if it is not `null` and we know that there was an error in the
      // login mutation
      if (res) {
        this.errors.username = [res[0].message]
      } else {
        await this.fetchUserDetailsAction()
        this.$router.push({ name: 'index' })
      }
    },
  },
}
</script>
