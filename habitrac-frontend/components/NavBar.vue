<template>
  <div class="fixed inset-x-0 bottom-0 w-full">
    <div class="flex justify-around w-full mx-auto sm:w-9/12 md:w-7/12">
      <div v-for="(link, index) in elements" :key="index">
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
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState({
      user: (state) => state.user.user,
      elements: (state) => state.navbar.elements,
    }),
  },
  methods: {
    ...mapActions({
      verifyLoggedInAction: 'user/verifyLoggedIn',
    }),
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
