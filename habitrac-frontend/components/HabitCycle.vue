<template>
  <div class="flex w-full">
    <div
      :class="
        tagged
          ? 'bg-green-500 hover:bg-green-400'
          : 'bg-red-500 hover:bg-red-400'
      "
      class="flex flex-col items-center justify-around w-40 mx-auto transition-colors duration-300 rounded-l-sm rounded-r-lg h-52"
      @click="toggleTagCycle(cycleIndex)"
    >
      <div class="w-full pr-3 text-right">
        <div class="text-3xl font-extrabold text-white">
          {{ today.format('DD') }}
        </div>
        <div
          class="text-xl font-semibold tracking-wide text-gray-700 uppercase"
        >
          {{ today.format('dddd') }}
        </div>
        <div class="text-sm text-gray-700 uppercase font-display">
          {{ today.format('MMMM/YYYY') }}
        </div>
      </div>
      <div class="">Check today</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    tagged: {
      type: Boolean,
      default: false,
    },
    cycleIndex: {
      type: Number,
      default: 0,
    },
  },
  data() {
    const today = this.$dayjs()
    return { today }
  },
  computed: {},
  methods: {
    toggleTagCycle() {
      this.$emit('clicked')
    },
  },
}
</script>
