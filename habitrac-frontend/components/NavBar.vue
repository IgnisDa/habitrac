<template>
  <div class="fixed inset-x-0 bottom-0 w-full">
    <div
      class="flex justify-around w-full mx-auto font-mono uppercase sm:w-9/12 md:w-7/12"
    >
      <div v-for="(link, index) in links" :key="index">
        <NuxtLink
          :to="{ name: link.pathName }"
          :class="{ 'website-link': routeActive(link.pathName) }"
        >
          <div class="px-4 pt-2">{{ link.label }}</div>
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
.nuxt-link-exact-active::before {
  content: '';
  display: block;
  margin: auto;
  height: 3px;
  width: 100%;
  background: blue;
  transition: width 0.3s ease, background-color 0.3s ease;
}
.website-link::before {
  content: '';
  width: 0;
  display: block;
  margin: auto;
  height: 3px;
  transition: width 0.3s ease, background-color 0.3s ease;
}
.website-link:hover::before {
  width: 100%;
  background: blue;
}
</style>
