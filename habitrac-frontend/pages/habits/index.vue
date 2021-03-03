<template>
  <div class="flex items-center justify-center h-screen">
    <div class="w-full mx-3 sm:w-4/5 md:w-1/3">
      <CodeWindow>
        <template #body>
          <div v-if="loading">Loading...</div>
          <div v-else>
            <div v-if="habits.length > 0">
              <div v-for="(habit, index) in habits" :key="index">
                <NuxtLink
                  :to="{
                    name: 'habits-slug',
                    params: { slug: habit.nameSlug },
                  }"
                >
                  <span class="text-true-gray-200 hover:underline sm:text-lg">
                    {{ habit.name }}
                  </span>
                </NuxtLink>
              </div>
            </div>
            <div v-else class="text-center">
              You have not created any habits to track. Create one
              <NuxtLink
                :to="{ name: 'habits-create' }"
                class="text-blue-600 hover:underline"
              >
                here</NuxtLink
              >.
            </div>
          </div>
        </template>
      </CodeWindow>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import getAllHabitsQuery from '~/apollo/queries/getAllHabits.gql'

export default {
  middleware: ['isAuthenticated'],
  data: () => ({ habits: [], loading: false }),
  head: () => ({ title: 'All Habits' }),
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
