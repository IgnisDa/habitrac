<template>
  <div>
    <div
      v-if="habit"
      class="flex flex-col items-center justify-center h-screen space-y-8"
    >
      <div
        class="px-5 py-2 font-serif text-3xl font-light border-2 border-yellow-300 rounded-md text-true-gray-200 sm:text-5xl md:text-7xl"
      >
        {{ habit.name }}
      </div>
      <NuxtLink
        :to="{
          name: 'habits-slug-details',
          params: { slug: $route.params.slug },
        }"
        class="relative flex items-center justify-center px-3 py-2 space-x-2 transition-colors duration-300 bg-blue-400 border-yellow-300 rounded-md hover:bg-blue-300"
      >
        <FontAwesomeIcon
          class="w-6 h-6 sm:w-8 sm:h-8"
          :icon="['fas', 'info-circle']"
        ></FontAwesomeIcon>
        <div class="pt-1 text-lg font-display sm:text-xl md:text-3xl">
          Details
        </div>
      </NuxtLink>
      <div
        v-if="habit"
        class="flex flex-col w-full p-3 mx-3 space-y-2 overflow-auto sm:mx-0"
      >
        <div class="flex flex-wrap justify-around my-auto">
          <HabitCycle :tagged="tagged" @clicked="toggleTagCycle()"></HabitCycle>
        </div>
      </div>
    </div>
    <div v-else>Loading...</div>
  </div>
</template>

<script>
import getHabitDetailsQuery from '~/apollo/queries/getHabitDetails.gql'
import toggleTagCycleMutation from '~/apollo/mutations/toggleTagCycle.gql'

export default {
  data: () => ({
    habit: { name: '' },
    cycle: 'Today',
    tagged: null,
  }),
  head() {
    return { title: `${this.habit.name} | ${this.cycle}` }
  },
  async mounted() {
    const slug = this.$route.params.slug
    const { data } = await this.$apollo.query({
      query: getHabitDetailsQuery,
      variables: {
        nameSlug: slug,
      },
      fetchPolicy: 'network-only',
    })
    if (data) {
      const habit = data.getHabitDetails.habit
      const today = this.$dayjs(this.$dayjs().format('YYYY-MM-DD'))
      const cycle = today.format('YYYY-MM-DD')
      const dateFrom = this.$dayjs(habit.dateFrom)
      if (today.isBefore(dateFrom)) {
        this.$router.push({
          name: 'habits-slug-details',
          params: { slug },
        })
        this.$addAlert({
          severity: 'warning',
          messageHeading: 'Not started',
          messageBody: 'The time period for this habit has not started yet',
          active: true,
        })
      }
      if (typeof habit.progress === 'string') {
        habit.progress = JSON.parse(habit.progress)
      }
      this.habit = habit
      this.cycle = cycle
      this.tagged = habit.progress[cycle]
      if (habit.isDone) {
        this.$router.push({
          name: 'habits-slug-details',
          params: { slug },
        })
      }
    }
  },
  methods: {
    toggleTagCycle() {
      this.$apollo
        .mutate({
          mutation: toggleTagCycleMutation,
          variables: {
            data: {
              nameSlug: this.$route.params.slug,
              date: this.cycle,
            },
          },
        })
        .then(({ data }) => {
          if (!data.toggleTagCycle.error) {
            this.tagged = !this.tagged
          } else {
            this.$addAlert({
              severity: 'danger',
              messageHeading: 'Error',
              messageBody: 'There was an error marking the day',
              active: true,
            })
          }
        })
    },
  },
}
</script>

<style scoped>
a::after {
  content: '';
  @apply w-0.5 bg-yellow-300 h-8 absolute -top-8;
}
</style>
