export default {
  mounted() {
    // This is run on every route to make sure that the navbar elements
    // are always up-to-date. Though we could probably get away with running the
    // `constructNavbarElements` action only on login and logout routes, it would
    // introduce inconsistent behaviour if the user refreshes the website for any
    // reason.
    this.$store.dispatch('navbar/constructNavbarElements')
  },
}
