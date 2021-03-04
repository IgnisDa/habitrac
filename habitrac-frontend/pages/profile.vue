<template>
  <div class="flex items-center justify-center min-h-screen">
    <div v-if="report" class="mx-3 sm:w-4/5 md:w-2/3">
      <CodeWindow>
        <template #body>
          <div class="flex flex-col font-serif divide-y">
            <div class="flex justify-between space-x-3">
              <div>Username</div>
              <div>{{ username }}</div>
            </div>
            <div class="flex justify-between space-x-3">
              <div>Total number of habits</div>
              <div>{{ report.numberOfHabits }}</div>
            </div>
            <div class="flex justify-between space-x-3">
              <div>Habits completed</div>
              <div>{{ report.doneHabits }}</div>
            </div>
            <div class="flex justify-between space-x-3">
              <div>Habits followed through successfully</div>
              <div>{{ report.completedHabits }}</div>
            </div>
          </div>
        </template>
      </CodeWindow>
    </div>
    <div v-else class="text-3xl text-center text-gray-200">Loading...</div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import getUserReportQuery from '~/apollo/queries/getUserReport.gql'

export default {
  middleware: ['isAuthenticated'],
  data: () => ({
    report: null,
  }),
  head: () => ({
    title: 'Profile',
  }),

  computed: {
    ...mapState({
      username: (state) => state.user.user.username,
    }),
  },
  async mounted() {
    await this.$store.dispatch('user/fetchUserDetails')
    const { data } = await this.$apollo.query({
      query: getUserReportQuery,
    })
    this.report = data.getUserReport
  },
}
</script>
