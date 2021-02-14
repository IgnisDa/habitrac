<template>
  <div class="fixed inset-x-0 bottom-0 w-full">
    <div class="flex justify-around w-full mx-auto sm:w-9/12 md:w-7/12">
      <div v-for="(link, index) in links" :key="index">
        <NuxtLink
          :to="{ name: link.pathName }"
          :class="{ 'website-link': routeActive(link.pathName) }"
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
export default {
  data: () => ({
    links: [
      { label: 'Home', pathName: 'index' },
      { label: 'Register', pathName: 'register' },
      { label: 'Login', pathName: 'login' },
      { label: 'Logout', pathName: 'logout' },
    ],
  }),
  methods: {
    routeActive(pathName) {
      return this.$route.name !== pathName
    },
  },
}
</script>

<style scoped>
.nuxt-link-exact-active::before,
.website-link::before {
  content: '';
  @apply block m-auto h-0.5 rounded-md w-full bg-purple-700 transition-width duration-200;
}
.website-link::before {
  @apply w-0;
}
.website-link:hover::before {
  @apply w-full bg-pink-500;
}
</style>
