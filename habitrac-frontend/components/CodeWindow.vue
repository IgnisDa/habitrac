<template>
  <div>
    <div
      class="flex flex-row-reverse items-center justify-start px-3 py-2 bg-gray-900 rounded-t-lg"
    >
      <div class="flex flex-row-reverse space-x-3 space-x-reverse">
        <div
          class="w-4 h-4 bg-blue-500 rounded-full cursor-pointer sm:w-6 sm:h-6"
          @click="clicked++"
        ></div>
        <div
          class="w-4 h-4 bg-yellow-400 rounded-full cursor-pointer sm:w-6 sm:h-6"
          @click="clicked++"
        ></div>
        <div
          class="w-4 h-4 bg-red-500 rounded-full cursor-pointer sm:w-6 sm:h-6"
          @click="clicked++"
        ></div>
      </div>
    </div>
    <div
      class="w-full p-3 px-3 py-2 space-y-5 overflow-auto font-mono text-xl rounded-b-lg text-true-gray-100 bg-true-gray-900 bg-opacity-80"
    >
      <slot name="body"></slot>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    clicked: 0,
  }),
  watch: {
    clicked(value) {
      if (value % 5 === 0) {
        alert(
          'This button has no purpose other than displaying this stupid message...'
        )
      }
    },
  },
}
</script>
