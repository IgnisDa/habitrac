<template>
  <div
    :class="{ 'debug-screens': mode !== 'production' }"
    class="min-h-screen antialiased bg-left bg-no-repeat bg-cover sm:bg-center"
    :style="{
      backgroundImage: `linear-gradient(90deg, rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.15)), url(${require('~/assets/images/background.jpeg')})`,
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
}
</script>
