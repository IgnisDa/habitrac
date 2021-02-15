<template>
  <div class="fixed top-0 left-0 right-0 flex mt-2 ml-1 cursor-pointer">
    <div class="flex justify-around w-full mx-auto lg:w-10/12 xl:w-8/12">
      <a href="//github.com/IgnisDa/habitrac" target="blank">
        <FontAwesomeIcon
          class="w-8 h-8 sm:h-10 sm:w-10"
          :icon="['fab', 'github']"
        ></FontAwesomeIcon>
      </a>
      <transition name="color-mode" mode="out-in">
        <component
          :is="getColorModeIcon"
          classes="h-8 w-8 sm:h-10 sm:w-10"
          @click.native="toggleColorMode"
        ></component>
      </transition>
    </div>
  </div>
</template>

<script>
import DarkModeIcon from '~/components/DarkModeIcon.vue'
import LightModeIcon from '~/components/LightModeIcon.vue'

export default {
  components: {
    DarkModeIcon,
    LightModeIcon,
  },
  computed: {
    getColorModeIcon() {
      if (this.$colorMode.value === 'light') {
        return 'LightModeIcon'
      } else {
        return 'DarkModeIcon'
      }
    },
  },
  methods: {
    toggleColorMode() {
      if (this.$colorMode.value === 'light') {
        this.$colorMode.preference = 'dark'
      } else {
        this.$colorMode.preference = 'light'
      }
    },
  },
}
</script>

<style scoped>
.color-mode-enter-active,
.color-mode-leave-active {
  transition-duration: 0.7s;
  transition-property: opacity scale;
  transition-timing-function: ease-in-out;
}
.color-mode-enter,
.color-mode-leave-to {
  @apply opacity-0 scale-75 transform;
}
</style>
