<template>
  <div class="flex flex-col items-center justify-center h-screen space-y-8">
    <div
      class="px-5 py-2 font-serif text-3xl font-light border-2 border-red-500 rounded-md sm:text-5xl md:text-7xl"
    >
      {{ habit.name }}
    </div>
    <NuxtLink
      :to="{
        name: 'habits-slug-details',
        params: { slug: $route.params.slug },
      }"
      class="relative flex items-center justify-center px-3 py-2 space-x-2 bg-blue-400 border border-red-500 rounded-md hover:bg-blue-300"
    >
      <FontAwesomeIcon
        class="w-6 h-6 sm:w-8 sm:h-8"
        :icon="['fas', 'info-circle']"
      ></FontAwesomeIcon>
      <div class="font-mono text-lg italic sm:text-xl md:text-3xl">Details</div>
    </NuxtLink>
    <div
      v-if="habit"
      class="flex flex-col w-full p-3 mx-3 space-y-2 overflow-auto sm:mx-0"
    >
      <div class="flex flex-wrap justify-around my-auto">
        <HabitCycle
          :cycle-index="cycleIndex"
          :tagged="tagged"
          @clicked="toggleTagCycle()"
        ></HabitCycle>
      </div>
    </div>
  </div>
</template>

<script>
import getHabitDetailsQuery from '~/apollo/queries/getHabitDetails.gql'
import toggleTagCycleMutation from '~/apollo/mutations/toggleTagCycle.gql'

export default {
  async asyncData({ app, params, $dayjs, redirect }) {
    const apolloClient = app.apolloProvider.defaultClient
    const slug = params.slug
    const { data } = await apolloClient.query({
      query: getHabitDetailsQuery,
      variables: {
        nameSlug: slug,
      },
      fetchPolicy: 'network-only',
    })
    if (data) {
      const habit = data.getHabitDetails.habit
      const today = $dayjs($dayjs().format('YYYY-MM-DD'))
      const startedOn = $dayjs(habit.startedOn)
      const cycleIndex = today.diff(startedOn, 'd') + 1
      const key = `cycle-${cycleIndex}`
      if (typeof habit.progress === 'string') {
        habit.progress = JSON.parse(habit.progress)
      }
      const obj = {
        habit,
        cycleIndex,
        tagged: habit.progress[key],
      }
      if (habit.isDone) {
        redirect({
          name: 'habits-slug-details',
          params: { slug: params.slug },
        })
      } else return obj
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
  @apply w-0.5 bg-red-500 h-8 absolute -top-8;
}
</style>
