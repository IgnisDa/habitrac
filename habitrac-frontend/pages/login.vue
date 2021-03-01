<template>
  <div class="w-full">
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
          class="relative col-start-1 row-end-2 p-5 m-3 transition-colors duration-300 bg-gray-900 rounded-md shadow-2xl sm:m-0"
        >
          <div
            class="pb-2 mb-8 text-3xl font-semibold tracking-wider text-center text-blue-500 transition-colors duration-500 border-b-4 border-blue-300 border-dashed sm:text-5xl"
            :class="{ 'text-yellow-400': loading }"
          >
            Login
          </div>
          <form class="w-72 sm:w-80 md:w-96" @submit.prevent="onSubmit()">
            <div class="mt-2 mb-5 sm:mt-0">
              <label
                for="identifier"
                class="block font-serif text-lg text-gray-100"
              >
                Username
              </label>
              <div
                class="flex items-center p-3 my-2 bg-gray-100 border rounded-sm focus-within:ring-2 focus-within:ring-blue-600"
                :class="[
                  errors.identifier
                    ? 'ring-2 ring-red-600'
                    : 'focus-within:ring-blue-600',
                ]"
              >
                <FontAwesomeIcon
                  class="flex-none w-6 h-6 text-black pointer-events-none fill-current"
                  :icon="fieldIcons.identifier"
                ></FontAwesomeIcon>
                <input
                  id="identifier"
                  ref="identifier"
                  v-model="credentials.identifier"
                  type="text"
                  class="w-full ml-2 bg-gray-100 border-0 focus:outline-none"
                  placeholder="Username"
                  required
                />
              </div>
              <transition name="errors">
                <ul
                  v-if="errors.identifier"
                  class="space-y-1 text-xs tracking-wider text-red-500"
                >
                  <li v-for="(error, index) in errors.identifier" :key="index">
                    {{ error }}
                  </li>
                </ul>
              </transition>
            </div>
            <div class="my-5">
              <label
                for="password"
                class="block font-serif text-lg text-gray-100"
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
                  @click="togglePasswordVisibility('password')"
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
              <span>Submit</span>
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
      identifier: '',
      password: '',
    },
    loading: false,
    fieldTypes: {
      password: 'password',
    },
    fieldIcons: {
      password: ['fas', 'eye'],
      identifier: ['fas', 'user'],
    },
    errors: { identifier: null, password: null },
  }),
  head: () => ({
    title: 'Login',
  }),
  computed: {
    formErrorsExist() {
      if (this.errors.identifier !== null) {
        return true
      }
      return false
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
      this.$refs.identifier.focus()
    },
    togglePasswordVisibility(fieldName) {
      this.fieldTypes[fieldName] =
        this.fieldTypes[fieldName] === 'password' ? 'text' : 'password'
      this.fieldIcons[fieldName] =
        this.fieldIcons[fieldName] === 'eye-slash' ? 'eye' : 'eye-slash'
    },
    async onSubmit() {
      this.errors = { identifier: null, password: null }
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
        this.errors.identifier = [res]
      } else {
        await this.fetchUserDetailsAction()
        this.$router.push({ name: 'index' })
      }
    },
  },
}
</script>
