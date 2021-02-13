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
          class="w-12 h-12 mx-auto"
          :icon="['fas', 'user-graduate']"
        ></FontAwesomeIcon>
      </div>
      <div class="w-1/2">
        <FontAwesomeIcon
          class="w-12 h-12 mx-auto"
          :icon="['fas', 'clock']"
        ></FontAwesomeIcon>
      </div>
      <div class="w-1/2">
        <FontAwesomeIcon
          class="w-12 h-12 mx-auto"
          :icon="['fas', 'guitar']"
        ></FontAwesomeIcon>
      </div>
      <div class="w-1/2">
        <FontAwesomeIcon
          class="w-12 h-12 mx-auto"
          :icon="['fas', 'users']"
        ></FontAwesomeIcon>
      </div>
    </div>
  </div>
</template>

<script>
// import userDetailsQuery from '~/apollo/queries/userDetails.gql'

export default {
  data: () => ({
    me: null,
    loading: true,
  }),
  mounted() {
    // this.$apollo
    //   .query({
    //     query: userDetailsQuery,
    //   })
    //   .then((result) => {
    //     this.me = result.data.userDetails
    //     this.loading = false
    //   })
    //   .catch((_error) => {
    //     alert('You should be logged in!')
    //   })
  },
}
</script>
