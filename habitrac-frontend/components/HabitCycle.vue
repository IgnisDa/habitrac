<template>
  <div
    class="flex flex-col-reverse items-center justify-center w-full sm:flex-row-reverse"
  >
    <div
      class="transition-colors duration-300 bg-gray-800 rounded-lg w-52 sm:w-64 h-52 sm:h-64"
    >
      <div class="flex flex-col items-center justify-around h-full px-3">
        <div class="w-full text-center">
          <div class="text-3xl font-extrabold text-white sm:text-5xl">
            {{ today.format('DD') }}
          </div>
          <div
            class="text-xl font-semibold tracking-wide text-gray-300 uppercase sm:text-3xl"
          >
            {{ today.format('dddd') }}
          </div>
          <div
            class="mt-2 text-sm text-gray-400 uppercase sm:text-base font-display"
          >
            {{ today.format('MMMM/YYYY') }}
          </div>
        </div>
        <div class="flex justify-around w-full">
          <button
            class="flex items-center p-1 px-2 transition duration-300 transform rounded-lg focus:outline-none hover:scale-110"
            :class="tagged ? 'bg-red-600' : 'bg-lime-600'"
            @click="toggleTagCycle()"
          >
            <transition name="button-icon" mode="out-in">
              <component
                :is="getIcon"
                classes="text-gray-100 fill-current h-8 w-8 sm:h-12 sm:w-12"
              ></component>
            </transition>
          </button>
        </div>
      </div>
    </div>
    <div
      :class="tagged ? 'bg-red-600' : 'bg-lime-600'"
      class="flex w-40 px-2 py-3 text-xl text-center uppercase transition-colors duration-1000 rounded-t-lg font-display sm:rounded-t-none sm:rounded-l-lg sm:text-3xl sm:w-52"
    >
      <transition name="tag-text" mode="out-in">
        <div v-if="!tagged" key="1" class="m-auto">Mark as done</div>
        <div v-else key="2" class="m-auto">Mark as not done</div>
      </transition>
    </div>
  </div>
</template>

<script>
import CheckMarkIcon from '~/components/icons/CheckMarkIcon.vue'
import TimesIcon from '~/components/icons/TimesIcon.vue'

export default {
  components: {
    CheckMarkIcon,
    TimesIcon,
  },
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
  computed: {
    getIcon() {
      return !this.tagged ? 'CheckMarkIcon' : 'TimesIcon'
    },
  },
  methods: {
    toggleTagCycle() {
      this.$emit('clicked')
    },
  },
}
</script>

<style scoped>
.button-icon-enter-active,
.button-icon-leave-active {
  transition-duration: 0.5s;
  transition-property: opacity scale;
}

.button-icon-enter,
.button-icon-leave-to {
  @apply scale-125 opacity-0 transform;
}

.tag-text-leave-active,
.tag-text-enter-active {
  transition-duration: 0.5s;
  transition-property: transform opacity background-color;
}

.tag-text-leave-to,
.tag-text-enter {
  opacity: 0;
  transform: translateY(-50px);
}
</style>
