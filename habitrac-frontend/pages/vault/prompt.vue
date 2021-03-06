<template>
  <div class="flex items-center justify-center min-h-screen">
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
          Unlock Vault
        </div>
        <form class="w-72 sm:w-80 md:w-96" @submit.prevent="onSubmit()">
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
                ref="password"
                v-model="password"
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
</template>

<script>
import { v4 as uuid4 } from 'uuid'
import { getCookie } from '~/utils.js'
import checkVaultPasswordQuery from '~/apollo/queries/checkVaultPassword.gql'

export default {
  data: () => ({
    password: '',
    loading: false,
    fieldIcons: {
      password: ['fas', 'eye'],
    },
    fieldTypes: {
      password: 'password',
    },
    errors: { password: null },
  }),
  head: () => ({
    title: 'Unlock Vault',
  }),
  computed: {
    formErrorsExist() {
      if (this.errors.password !== null) {
        return true
      }
      return false
    },
  },
  mounted() {
    this.focusInput()
    if (getCookie('vault-token')) {
      this.$router.push({ name: 'vault' })
    }
  },
  methods: {
    focusInput() {
      this.$refs.password.focus()
    },
    togglePasswordVisibility(fieldName) {
      this.fieldTypes[fieldName] =
        this.fieldTypes[fieldName] === 'password' ? 'text' : 'password'
      this.fieldIcons[fieldName] =
        this.fieldIcons[fieldName] === 'eye-slash' ? 'eye' : 'eye-slash'
    },
    async onSubmit() {
      this.errors = { password: null }
      const {
        data: { checkVaultPassword: data },
      } = await this.$apollo.query({
        query: checkVaultPasswordQuery,
        variables: {
          password: this.password,
        },
      })
      if (!data) {
        this.errors.password = ['The password supplied was incorrect']
      } else {
        const expiry = new Date()
        // each token expires after 10 minutes
        expiry.setTime(expiry.getTime() + 1000 * 60 * 10)
        document.cookie = `vault-token=${uuid4()}; expires=${expiry.toGMTString()}; path=/`
        this.$router.push({ name: 'vault' })
      }
    },
  },
}
</script>
