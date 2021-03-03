<template>
  <div class="flex items-center justify-center min-h-screen">
    <div v-if="report" class="mx-3 sm:w-4/5 md:w-2/3">
      <CodeWindow>
        <template #body>
          <div class="flex flex-col font-serif divide-y">
            <div class="flex justify-between space-x-3">
              <div>Total number of habits</div>
              <div>{{ report.numberOfHabits }}</div>
            </div>
            <div class="flex justify-between space-x-3">
              <div>Habits completed</div>
              <div>{{ report.completedHabits }}</div>
            </div>
            <div class="flex justify-between space-x-3">
              <div>Habits followed through successfully</div>
              <div>{{ report.doneHabits }}</div>
            </div>
          </div>
        </template>
      </CodeWindow>
    </div>
    <div v-else>Still Loading</div>
  </div>
</template>

<script>
import getUserReportQuery from '~/apollo/queries/getUserReport.gql'

export default {
  middleware: ['isAuthenticated'],
  async asyncData({ app }) {
    const apolloClient = app.apolloProvider.defaultClient
    const { data } = await apolloClient.query({
      query: getUserReportQuery,
    })
    const report = data.getUserReport
    const obj = { report }
    return obj
  },
}
</script>
