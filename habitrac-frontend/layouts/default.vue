<template>
  <div
    :class="mode !== 'production' ? 'debug-screens' : ''"
    class="antialiased"
  >
    <Alert></Alert>
    <Nuxt />
    <NavBar></NavBar>
    <ControlBar></ControlBar>
  </div>
</template>

<script>
import Vue from 'vue'
import globalMixin from '~/mixin/setNavbarElements.js'

Vue.mixin(globalMixin)
export default {
  data: () => ({
    mode: process.env.NODE_ENV,
  }),
}
</script>
