<template>
  <div class="flex items-center justify-center h-screen">
    <div
      v-if="habit"
      class="flex flex-col w-full p-3 mx-3 space-y-2 overflow-auto bg-gray-200 rounded-lg shadow-lg sm:w-3/5 h-4/6 sm:h-5/6 sm:mx-0"
    >
      <div class="flex flex-wrap justify-around my-auto">
        <div v-for="(value, _, index) in habit.progress" :key="index">
          <HabitCycleBox
            :cycle="value"
            :started-on="habit.startedOn"
            :index="index"
            :tooltip-text="parseDate(index).format('dddd, DD MMM YYYY')"
            @click.native="toggleTagCycle(index)"
          >
            {{ parseDate(index).format('DD') }}
          </HabitCycleBox>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import getHabitDetailsQuery from '~/apollo/queries/getHabitDetails.gql'
import toggleTagCycleMutation from '~/apollo/mutations/toggleTagCycle.gql'

export default {
  async asyncData({ app, params }) {
    const apolloClient = app.apolloProvider.defaultClient
    const slug = params.slug
    const { data } = await apolloClient.query({
      query: getHabitDetailsQuery,
      variables: {
        nameSlug: slug,
      },
    })
    if (data) {
      const obj = {
        habit: data.getHabitDetails.habit,
      }
      if (typeof obj.habit.progress === 'string') {
        obj.habit.progress = JSON.parse(obj.habit.progress)
      }
      return obj
    }
  },
  methods: {
    parseDate(index) {
      return this.$dayjs(this.habit.startedOn).add(index, 'day')
    },
    toggleTagCycle(index) {
      // const today = new Date().getDate()
      this.$apollo
        .mutate({
          mutation: toggleTagCycleMutation,
          variables: {
            data: {
              nameSlug: this.$route.params.slug,
              cycleIndex: index,
            },
          },
        })
        .then(() => {
          const key = `cycle-${index + 1}`
          this.habit.progress[key] = !this.habit.progress[key]
        })
    },
  },
}
</script>
