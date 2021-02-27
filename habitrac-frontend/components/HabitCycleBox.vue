<template>
  <div class="p-0.5">
    <div
      :class="cycle ? 'bg-green-500' : 'bg-red-500'"
      class="flex items-center justify-center w-8 h-8 transition-colors duration-300 rounded-full"
      :title="getTooltipText"
    ></div>
  </div>
</template>
<script>
export default {
  props: {
    cycle: {
      type: Boolean,
      default: false,
    },
    startedOn: {
      type: String,
      default: '',
    },
    index: {
      type: Number,
      default: 1,
    },
  },
  computed: {
    getTooltipText() {
      return this.$dayjs(this.startedOn)
        .add(this.index, 'd')
        .format('DD/MMM/YYYY')
    },
  },
}
</script>
