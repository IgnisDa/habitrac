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
            Register
          </div>
          <form class="w-72 sm:w-80 md:w-96" @submit.prevent="onSubmit()">
            <div class="mt-2 mb-5 sm:mt-0">
              <label
                for="identifier"
                class="block font-serif text-lg text-gray-200"
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
                for="passwordOne"
                class="block font-serif text-lg text-gray-200"
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
                  :icon="fieldIcons.passwordOne"
                  @click="togglePasswordVisibility('passwordOne')"
                ></FontAwesomeIcon>
                <input
                  id="passwordOne"
                  v-model="credentials.passwordOne"
                  :type="fieldTypes.passwordOne"
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
            <div class="my-5">
              <label
                for="passwordTwo"
                class="block font-serif text-lg text-gray-200"
              >
                Confirm password
              </label>
              <div
                class="flex items-center p-3 my-2 bg-gray-100 border rounded-sm focus-within:ring-2"
                :class="[
                  errors.password
                    ? 'ring-2 ring-red-600'
                    : 'focus-within:ring-blue-600',
                ]"
              >
                <FontAwesomeIcon
                  class="flex-none w-6 h-6 text-black cursor-pointer fill-current"
                  :icon="fieldIcons.passwordTwo"
                  @click="togglePasswordVisibility('passwordTwo')"
                ></FontAwesomeIcon>
                <input
                  id="passwordTwo"
                  v-model="credentials.passwordTwo"
                  :type="fieldTypes.passwordTwo"
                  class="w-full ml-2 bg-gray-100 border-0 focus:outline-none"
                  placeholder="Retype password"
                  required
                />
              </div>
            </div>
            <button
              type="submit"
              class="w-full p-3 text-lg font-semibold text-center text-red-600 uppercase bg-purple-200 rounded-sm focus:outline-none loading--button-border-blue"
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
      passwordOne: '',
      passwordTwo: '',
    },
    loading: false,
    errors: { identifier: null, password: null },
    fieldTypes: {
      passwordOne: 'password',
      passwordTwo: 'password',
    },
    fieldIcons: {
      passwordOne: ['fas', 'eye'],
      passwordTwo: ['fas', 'eye'],
      identifier: ['fas', 'user'],
    },
  }),
  head: () => ({
    title: 'Register',
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
      createUserMutation: 'user/createUser',
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
      const credentials = this.credentials

      if (credentials.passwordOne !== credentials.passwordTwo) {
        this.errors.password = ['The two passwords do not match']
        return
      }
      const finalCredentials = {
        identifier: credentials.identifier,
        password: credentials.passwordOne,
      }

      this.loading = true
      const res = await this.createUserMutation(finalCredentials)
      this.loading = false
      if (!res.status) {
        this.errors = res.errors
      } else {
        this.$router.push({ name: 'login' })
        this.$addAlert({
          severity: 'info',
          messageHeading: 'Registration successful',
          messageBody: 'Please log in with your new credentials',
          active: true,
        })
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.errors-enter-active,
.errors-leave-active {
  transition-duration: 0.8s;
  transition-property: opacity;
}

.errors-enter,
.errors-leave-to {
  opacity: 0;
}
</style>
