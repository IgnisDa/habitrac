<template>
  <div>
    <div
      v-if="habit"
      class="flex flex-col items-center justify-center w-full min-h-screen mx-auto space-y-10 sm:w-4/5 md:h-3/4"
    >
      <div
        class="flex items-center px-5 py-2 space-x-3 font-serif text-3xl font-light border-2 border-yellow-300 rounded-md text-true-gray-200 sm:text-5xl md:text-7xl"
      >
        <div>{{ habit.name }}</div>
        <div class="flex flex-col space-y-2">
          <NuxtLink
            :to="{
              name: 'habits-slug-update',
              params: { slug: $route.params.slug },
            }"
          >
            <FontAwesomeIcon
              class="w-6 h-6 transition-transform duration-300 transform sm:w-8 sm:h-8 hover:scale-110"
              :icon="['fas', 'pencil-alt']"
            ></FontAwesomeIcon>
          </NuxtLink>
          <button class="focus:outline-none" @click="handleDelete()">
            <FontAwesomeIcon
              class="w-6 h-6 transition-transform duration-300 transform sm:w-8 sm:h-8 hover:scale-110"
              :icon="['fas', 'trash-alt']"
            ></FontAwesomeIcon>
          </button>
        </div>
      </div>
      <div
        class="mx-5 text-sm italic text-center text-indigo-400 sm:text-base md:text-xl sm:w-4/5 md:w-2/3"
      >
        {{ habit.description }}
      </div>
      <div v-if="habit.isDone">
        <div class="text-lg font-bold text-center text-green-600 sm:text-2xl">
          The duration of this habit is now over!
        </div>
      </div>
      <div class="mx-3 sm:w-4/5 md:w-2/3">
        <CodeWindow>
          <template #body>
            <div v-if="report">
              <div class="flex flex-col font-serif divide-y">
                <div class="flex justify-between space-x-3">
                  <div>Started on</div>
                  <div>{{ startedOn }}</div>
                </div>
                <div class="flex justify-between space-x-3">
                  <div>End date</div>
                  <div>{{ dateTo }}</div>
                </div>
                <div class="flex justify-between space-x-3">
                  <div>Total</div>
                  <div>{{ report.total }}</div>
                </div>
                <div class="flex justify-between space-x-3">
                  <div>Completed</div>
                  <div>{{ report.complete }}</div>
                </div>
                <div class="flex justify-between space-x-3">
                  <div>Incomplete</div>
                  <div>{{ report.incomplete }}</div>
                </div>
                <div class="flex justify-between space-x-3">
                  <div>Percentage of days followed through</div>
                  <div>{{ report.completionPercentage }}%</div>
                </div>
              </div>
            </div>
            <div v-else>Loading...</div>
          </template>
        </CodeWindow>
      </div>
    </div>
    <div v-else>Loading...</div>
  </div>
</template>

<script>
import getHabitDetailsQuery from '~/apollo/queries/getHabitDetails.gql'
import getHabitReportQuery from '~/apollo/queries/getHabitReport.gql'
import deleteHabitMutation from '~/apollo/mutations/deleteHabit.gql'

export default {
  data: () => ({
    habit: { name: '' },
    startedOn: null,
    dateTo: null,
    report: null,
  }),
  head() {
    return { title: `${this.habit.name} | Details` }
  },
  async mounted() {
    const slug = this.$route.params.slug
    const { data } = await this.$apollo.query({
      query: getHabitDetailsQuery,
      variables: {
        nameSlug: slug,
      },
      // Had to do this because apollo does some stupid caching stuff. Like TF bro? If I
      // had to to cache my query's results, I would have stored the fucking results
      // somewhere, not made this method. What a massive idiot.
      fetchPolicy: 'network-only',
      // In retrospection, I kinda regret what I said above. Caching the results does make
      // sense for most use cases; backend data doesn't change very much or that often.
      // I feel like the massive idiot now.
    })
    const { data: report } = await this.$apollo.query({
      query: getHabitReportQuery,
      variables: {
        nameSlug: slug,
      },
      fetchPolicy: 'network-only',
    })

    if (data) {
      const habit = data.getHabitDetails.habit
      if (typeof habit.progress === 'string') {
        habit.progress = JSON.parse(habit.progress)
      }
      const startedOn = this.$dayjs(habit.startedOn).format('D, MMM YYYY')
      const dateTo = this.$dayjs(report.getHabitReport.dateTo).format(
        'D, MMM YYYY'
      )
      this.habit = habit
      this.startedOn = startedOn
      this.dateTo = dateTo
      this.report = report.getHabitReport
    }
    if (this.habit.isCompleted) {
      this.$confetti.start({
        particlesPerFrame: 0.7,
        particles: [
          {
            type: 'heart',
            dropRate: 6,
          },
          {
            type: 'circle',
            size: 3,
          },
        ],
      })
    }
  },
  beforeDestroy() {
    this.$confetti.stop()
  },
  methods: {
    async handleDelete() {
      if (
        confirm(
          'This action is irreversible. Are you sure you want to delete this habit?'
        )
      ) {
        const slug = this.$route.params.slug
        const { data } = await this.$apollo.mutate({
          mutation: deleteHabitMutation,
          variables: {
            nameSlug: slug,
          },
        })
        if (!data.deleteHabit.error) {
          this.$addAlert({
            severity: 'info',
            messageHeading: 'Deleted',
            messageBody: `The habit '${slug}' was deleted successfully!`,
            active: true,
          })
          this.$router.push({ name: 'habits' })
        } else {
          this.$addAlert({
            severity: 'danger',
            messageHeading: 'Error',
            messageBody:
              'We encountered an error while performing this operation. Please try again.',
            active: true,
          })
        }
      }
    },
  },
}
</script>
