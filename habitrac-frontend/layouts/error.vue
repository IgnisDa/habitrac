<template>
  <div class="flex items-center justify-center min-h-screen">
    <div class="flex flex-col mx-4 space-y-5">
      <div class="text-6xl text-center text-red-600">
        {{ error.statusCode }}
      </div>
      <div class="text-2xl text-center underline text-true-gray-200">
        {{ error.message }}
      </div>
    </div>
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
