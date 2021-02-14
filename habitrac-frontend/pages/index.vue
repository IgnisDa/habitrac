<template>
  <div
    class="flex flex-wrap min-h-screen mx-auto overflow-hidden lg:w-10/12 xl:w-8/12"
  >
    <div class="flex w-full overflow-hidden sm:w-1/2">
      <div class="p-2 m-auto text-7xl md:text-8xl 2xl:text-9xl font-display">
        Habitrac
      </div>
    </div>
    <div
      class="flex flex-wrap items-center w-full py-12 overflow-hidden sm:w-1/2 justify-items-center"
    >
      <div
        v-for="(trait, index) in traits"
        :key="index"
        class="flex items-center justify-between w-full mx-5 my-auto"
        :class="[
          index % 2 === 0 ? 'flex-row' : 'flex-row-reverse',
          index % 2 === 1 ? 'text-left' : 'text-right',
        ]"
      >
        <FontAwesomeIcon
          class="flex-none w-8 h-8 sm:h-12 sm:w-12"
          :icon="['fas', trait.icon]"
        ></FontAwesomeIcon>
        <div>
          {{ trait.text }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data: () => ({
    traits: [
      {
        icon: 'user-graduate',
        text:
          'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officia,distinctio alias.',
      },
      {
        icon: 'clock',
        text:
          'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officia,distinctio alias.',
      },
      {
        icon: 'guitar',
        text:
          'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officia,distinctio alias.',
      },
      {
        icon: 'users',
        text:
          'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officia,distinctio alias.',
      },
    ],
  }),
  head: () => ({
    title: 'Habitrac',
  }),
  methods: {
    ...mapActions({
      fetchUserDetailsAction: 'user/fetchUserDetails',
    }),
  },
}
</script>
