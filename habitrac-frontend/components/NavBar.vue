<template>
  <div class="fixed inset-x-0 bottom-0 w-full">
    {{ determineVisibility(false) }}
    <div class="flex justify-around w-full mx-auto sm:w-9/12 md:w-7/12">
      <div v-for="(link, index) in links" :key="index">
        <div v-if="determineVisibility(link.authenticated)">
          <NuxtLink
            :to="{ name: link.pathName }"
            :class="{ 'website-link': routeInactive(link.pathName) }"
          >
            <div
              class="px-3 pt-1 font-mono text-sm uppercase sm:text-lg sm:tracking-widest"
            >
              {{ link.label }}
            </div>
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  data: () => ({
    links: [
      // the `authenticated` key decides whether the link will be displayed in the navbar
      // according to authentication status
      // --> `null`: displayed always
      // --> `false`: displayed if the user is not logged in otherwise not
      // --> `true`: displayed if the user is logged in otherwise not
      { label: 'Home', pathName: 'index', authenticated: null },
      { label: 'Register', pathName: 'register', authenticated: false },
      { label: 'Login', pathName: 'login', authenticated: false },
      { label: 'Logout', pathName: 'logout', authenticated: true },
    ],
  }),
  computed: {
    ...mapState({
      user: (state) => state.user.user,
    }),
    getNavbarElements() {
      // create a computed property that returns all the navbar elements that we
      // actually require to be rendered
      return ''
    },
  },
  methods: {
    ...mapActions({
      verifyLoggedInAction: 'user/verifyLoggedIn',
    }),
    determineVisibility(authenticated) {
      // let hasToken = null
      this.verifyLoggedInAction().then((resp) => {
        // hasToken = resp
        if (authenticated === null) {
          return true
        } else if (authenticated === false) {
          if (!resp) {
            return true
          } else {
            console.log(resp)
            return false
          }
        } else if (authenticated === true) {
          if (resp) {
            return true
          } else {
            return false
          }
        }
      })
    },
    routeInactive(pathName) {
      return this.$route.name !== pathName
    },
  },
}
</script>

<style lang="scss" scoped>
.nuxt-link-exact-active::before,
.website-link::before {
  content: '';
  @apply block m-auto h-0.5 rounded-md bg-pink-500 transition-width duration-500;
}
.nuxt-link-exact-active::before {
  @apply bg-purple-700;
}
.website-link::before {
  @apply w-0;
}
.website-link:hover::before {
  @apply w-full;
}
</style>
