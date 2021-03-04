<template>
  <div
    :class="mode !== 'production' ? 'debug-screens' : ''"
    class="min-h-screen antialiased bg-left bg-no-repeat bg-cover sm:bg-center"
    :style="{
      backgroundImage: `linear-gradient(90deg, rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.15)), url('https://images.pexels.com/photos/1111318/pexels-photo-1111318.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260')`,
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
