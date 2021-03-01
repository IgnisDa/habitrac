<template>
  <div
    :class="mode !== 'production' ? 'debug-screens' : ''"
    class="min-h-screen antialiased bg-center bg-no-repeat bg-cover"
    :style="{
      backgroundImage: `linear-gradient(90deg, rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.15)), url(${getBackgroundImage})`,
    }"
  >
    <Alert></Alert>
    <Nuxt />
    <NavBar></NavBar>
    <ControlBar></ControlBar>
  </div>
</template>

<script>
import Vue from 'vue'
import navbarMixin from '~/mixin/setNavbarElements.js'

Vue.mixin(navbarMixin)

export default {
  data: () => ({
    mode: process.env.NODE_ENV,
  }),
  computed: {
    getBackgroundImage() {
      return require(`~/assets/images/page-bg.jpg`)
    },
  },
}
</script>
