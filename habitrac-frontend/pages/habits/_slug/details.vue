<template>
  <div
    class="flex flex-col items-center justify-center w-full min-h-screen mx-auto sm:w-4/5 md:h-3/4"
  >
    <div
      class="px-5 py-2 font-serif text-3xl font-light sm:text-5xl md:text-7xl"
    >
      {{ habit.name }}
    </div>
    <div v-if="habit.isDone">
      <div class="text-lg font-bold text-center text-green-600 sm:text-2xl">
        The duration of this habit is now over!
      </div>
    </div>
    <!-- <div
      class="flex flex-wrap w-full overflow-x-auto h-4/5 justify-items-center opacity-20"
    >
      <div v-for="(value, _, index) in habit.progress" :key="index">
        <HabitCycleBox
          :cycle="value"
          :started-on="habit.startedOn"
          :index="index"
        >
        </HabitCycleBox>
      </div>
    </div> -->
  </div>
</template>

<script>
import getHabitDetailsQuery from '~/apollo/queries/getHabitDetails.gql'

export default {
  async asyncData({ app, params, $dayjs }) {
    const apolloClient = app.apolloProvider.defaultClient
    const slug = params.slug
    const { data } = await apolloClient.query({
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
    if (data) {
      const habit = data.getHabitDetails.habit
      const obj = {
        habit,
        startedOn: $dayjs(habit.startedOn),
      }
      if (typeof obj.habit.progress === 'string') {
        obj.habit.progress = JSON.parse(obj.habit.progress)
      }
      return obj
    }
  },
  mounted() {
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
  methods: {},
}
</script>
