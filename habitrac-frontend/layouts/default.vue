<template>
  <div
    :class="mode !== 'production' ? 'debug-screens' : ''"
    class="antialiased"
  >
    <Nuxt />
    <NavBar></NavBar>
  </div>
</template>

<script>
export default {
  data: () => ({
    mode: process.env.NODE_ENV,
  }),
}
</script>
