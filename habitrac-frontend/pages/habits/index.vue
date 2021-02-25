<template>
  <div class="flex items-center justify-center h-screen">
    <ol
      class="flex flex-col w-full p-3 mx-3 space-y-2 overflow-auto list-decimal list-inside bg-gray-200 divide-y divide-purple-200 rounded-lg shadow-lg sm:w-3/5 h-4/6 sm:h-5/6 sm:mx-0"
    >
      <div v-if="loading">Its still loading</div>
      <li v-for="(habit, index) in habits" v-else :key="index">
        <NuxtLink
          :to="{
            name: 'habits-slug',
            params: { slug: habit.nameSlug },
          }"
        >
          <span
            class="text-blue-800 hover:text-blue-700 hover:underline sm:text-lg"
          >
            {{ habit.name }}
          </span>
        </NuxtLink>
      </li>
    </ol>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import getAllHabitsQuery from '~/apollo/queries/getAllHabits.gql'

export default {
  middleware: ['isAuthenticated'],
  data: () => ({ habits: [], loading: false }),
  computed: {
    ...mapState({
      usernameSlug: (state) => state.user.user.usernameSlug,
    }),
  },
  async mounted() {
    this.loading = true
    await this.fetchUserDetailsAction()
    this.$apollo
      .query({
        query: getAllHabitsQuery,
        variables: {
          usernameSlug: this.usernameSlug,
        },
      })
      .then(({ data }) => {
        this.habits = data.getAllHabits
        this.loading = false
      })
  },
  methods: {
    ...mapActions({
      fetchUserDetailsAction: 'user/fetchUserDetails',
    }),
  },
}
</script>
