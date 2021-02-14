<template>
  <div class="flex flex-wrap min-h-screen overflow-hidden">
    <div class="flex w-full overflow-hidden sm:w-1/2">
      <div class="p-2 m-auto text-9xl font-display">Habitrac</div>
    </div>
    <div
      class="flex flex-wrap items-center w-full py-24 overflow-hidden sm:w-1/2 justify-items-center"
    >
      <div class="w-1/2">
        <FontAwesomeIcon
          class="w-20 h-20 mx-auto"
          :icon="['fas', 'user-graduate']"
        ></FontAwesomeIcon>
      </div>
      <div class="w-1/2">
        <FontAwesomeIcon
          class="w-20 h-20 mx-auto"
          :icon="['fas', 'clock']"
        ></FontAwesomeIcon>
      </div>
      <div class="w-1/2">
        <FontAwesomeIcon
          class="w-20 h-20 mx-auto"
          :icon="['fas', 'guitar']"
        ></FontAwesomeIcon>
      </div>
      <div class="w-1/2">
        <FontAwesomeIcon
          class="w-20 h-20 mx-auto"
          :icon="['fas', 'users']"
        ></FontAwesomeIcon>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data: () => ({}),
  mounted() {},
  methods: {
    ...mapActions({
      fetchUserDetailsAction: 'user/fetchUserDetails',
    }),
  },
}
</script>
