<template>
  <div class="flex items-center justify-center h-screen">
    <div
      v-if="habit"
      class="flex flex-col w-full p-3 mx-3 space-y-2 overflow-auto sm:w-4/5 h-4/6 sm:h-5/6 sm:mx-0"
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
const isToday = require('dayjs/plugin/isToday')

export default {
  async asyncData({ app, params, $dayjs }) {
    const apolloClient = app.apolloProvider.defaultClient
    const slug = params.slug
    const { data } = await apolloClient.query({
      query: getHabitDetailsQuery,
      variables: {
        nameSlug: slug,
      },
    })
    if (data) {
      const habit = data.getHabitDetails.habit
      $dayjs.extend(isToday)
      const today = $dayjs().add(1, 'd')
      const startedOn = $dayjs(habit.startedOn)
      const cycleIndex = today.diff(startedOn, 'd')
      const key = `cycle-${cycleIndex}`
      const obj = {
        habit,
        cycleIndex,
        tagged: habit.progress[key],
      }
      if (typeof obj.habit.progress === 'string') {
        obj.habit.progress = JSON.parse(obj.habit.progress)
      }
      return obj
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
              cycleIndex: this.cycleIndex,
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
