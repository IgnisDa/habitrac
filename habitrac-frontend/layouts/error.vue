<template>
  <div>
    <h1>
      {{ error.statusCode }}
    </h1>
    <h2>{{ error.message }}</h2>
  </div>
</template>

<script>
export default {
  props: {
    error: {
      type: Object,
      default: () => ({
        statusCode: 404,
        message: 'Page not found',
      }),
    },
  },
}
</script>
