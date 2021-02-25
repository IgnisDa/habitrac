<template>
  <div class="p-0.5 cursor-pointer">
    <div
      :class="
        cycle
          ? 'bg-green-500 hover:bg-green-400'
          : 'bg-red-500 hover:bg-red-400'
      "
      class="flex items-center justify-center w-8 h-8 transition-colors duration-300 rounded-sm"
      :title="tooltipText"
    >
      <slot></slot>
    </div>
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
    tooltipText: {
      type: String,
      default: '',
    },
  },
  computed: {},
}
</script>
