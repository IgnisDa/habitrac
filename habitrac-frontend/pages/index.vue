<template>
  <div class="flex flex-wrap min-h-screen overflow-hidden">
    <div class="flex w-full overflow-hidden sm:w-1/2">
      <div class="p-2 m-auto text-7xl sm:text-8xl md:text-9xl font-display">
        Habitrac
      </div>
    </div>
    <div
      class="flex flex-wrap items-center w-full py-12 overflow-hidden sm:w-1/2 justify-items-center"
    >
      <div
        v-for="(trait, index) in traits"
        :key="index"
        class="flex items-center w-full mx-5 my-auto sm:flex-row-reverse"
      >
        <FontAwesomeIcon
          class="flex-none w-8 h-8 sm:h-12 sm:w-12"
          :icon="['fas', trait.icon]"
        ></FontAwesomeIcon>
        <div class="ml-5 text-left sm:text-right sm:mr-6">
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
  computed: {},
  mounted() {},
  methods: {
    ...mapActions({
      fetchUserDetailsAction: 'user/fetchUserDetails',
    }),
  },
}
</script>
