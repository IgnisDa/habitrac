<template>
  <div class="flex items-center justify-center min-h-screen">
    <div class="w-full dark:bg-gray-800">
      <div
        class="container flex items-center justify-center min-h-screen mx-auto"
      >
        <div class="grid">
          <div class="col-start-1 row-end-2">
            <div
              class="w-full h-full transition-all duration-300 transform rounded-xl rotate-6"
              :class="[formErrorsExist ? 'bg-red-600' : 'bg-green-600']"
            ></div>
          </div>
          <div
            class="relative col-start-1 row-end-2 p-5 m-3 transition-colors duration-300 border rounded-md shadow-xl bg-gray-50 sm:m-0"
          >
            <div class="absolute"></div>
            <div
              class="pb-2 mb-8 text-3xl font-semibold tracking-wider text-center text-blue-500 transition-colors duration-500 border-b-4 border-blue-300 border-dashed sm:text-5xl"
              :class="{ 'text-yellow-400': loading }"
            >
              Start a Habit
            </div>
            <form class="w-72 sm:w-80 md:w-96" @submit.prevent="handleSubmit()">
              <div class="mt-2 mb-5 sm:mt-0">
                <label
                  for="username"
                  class="block font-serif text-lg text-black dark:text-gray-100"
                >
                  What's the habit about?
                </label>
                <div
                  class="relative w-full p-3 my-2 bg-gray-100 border rounded-sm focus-within:ring-2 focus-within:ring-blue-600"
                  :class="[
                    errors.name
                      ? 'ring-2 ring-red-600'
                      : 'focus-within:ring-blue-600',
                  ]"
                >
                  <div class="flex items-center">
                    <input
                      id="habit-name"
                      v-model="data.name"
                      type="text"
                      class="w-full px-1 bg-gray-100 order-0 focus:outline-none"
                      autocomplete="off"
                      placeholder="Meditate everyday"
                      required
                    />
                    <FontAwesomeIcon
                      class="flex-none w-6 h-6 text-black pointer-events-none fill-current"
                      :icon="['fas', 'clock']"
                    ></FontAwesomeIcon>
                  </div>
                </div>
                <transition name="name-errors">
                  <ul
                    v-if="errors.name"
                    class="space-y-1 text-xs tracking-wider text-red-500"
                  >
                    <li v-for="(error, index) in errors.name" :key="index">
                      {{ error }}
                    </li>
                  </ul>
                </transition>
              </div>
              <div class="mt-2 mb-5 sm:mt-0">
                <div class="relative w-full my-2 rounded-sm">
                  <div class="flex flex-wrap items-center">
                    <div class="w-full px-1 sm:w-1/2">
                      <label
                        for="duration-from"
                        class="block font-serif text-lg text-black dark:text-gray-100"
                      >
                        From
                      </label>
                      <input
                        id="duration-from"
                        v-model="data.duration.from"
                        type="date"
                        class="w-full p-3 bg-gray-100 border duration-input focus:outline-none focus-within:ring-blue-400 focus-within:ring-2"
                        required
                      />
                    </div>
                    <div class="w-full px-1 sm:w-1/2">
                      <label
                        for="duration-to"
                        class="block font-serif text-lg text-black dark:text-gray-100"
                      >
                        To
                      </label>
                      <input
                        id="duration-to"
                        v-model="data.duration.to"
                        type="date"
                        class="w-full p-3 bg-gray-100 border duration-input focus:outline-none focus-within:ring-blue-400 focus-within:ring-2"
                        required
                      />
                    </div>
                  </div>
                  <transition name="duration-errors">
                    <ul
                      v-if="errors.duration"
                      class="space-y-1 text-xs tracking-wider text-red-500"
                    >
                      <li
                        v-for="(error, index) in errors.duration"
                        :key="index"
                      >
                        {{ error }}
                      </li>
                    </ul>
                  </transition>
                </div>
              </div>
              <button
                type="submit"
                class="w-full p-3 text-lg font-semibold text-center text-indigo-700 uppercase bg-gray-200 rounded-sm focus:outline-none loading--button-border-red"
                :class="{ 'loading--button': loading }"
              >
                <span>Create</span>
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import createDailyHabitMutation from '~/apollo/mutations/createDailyHabit.gql'

export default {
  data: () => ({
    data: { name: '', duration: { from: '', to: '' } },
    loading: false,
    errors: { name: null, duration: null },
  }),
  head: () => ({
    title: 'New Habit',
  }),
  computed: {
    formErrorsExist() {
      let exist = false
      for (const error in this.errors) {
        if (this.errors[error]) {
          exist = true
          break
        }
      }
      return exist
    },
  },
  methods: {
    async handleSubmit() {
      this.errors = { name: null, duration: null }
      this.loading = true
      const resp = await this.$apollo.mutate({
        mutation: createDailyHabitMutation,
        variables: {
          data: this.data,
        },
      })
      this.loading = false
      if (!resp.data.createDailyHabit.status) {
        this.errors.duration = resp.data.createDailyHabit.errors.duration
        this.errors.name = resp.data.createDailyHabit.errors.name
      } else {
        this.$addAlert({
          severity: 'success',
          messageHeading: 'Created',
          messageBody: 'Your new habit was created successfully!',
          active: true,
        })
        this.$router.push({
          name: 'habits-slug',
          params: { slug: resp.data.createDailyHabit.habit.nameSlug },
        })
      }
    },
  },
}
</script>

<style scoped>
.duration-input::-webkit-calendar-picker-indicator {
  margin: 0;
}

.name-errors-enter-active,
.name-errors-leave-active,
.duration-errors-enter-active,
.duration-errors-leave-active {
  transition-duration: 0.8s;
  transition-property: opacity;
}

.name-errors-enter,
.name-errors-leave-to,
.duration-errors-enter,
.duration-errors-leave-to {
  opacity: 0;
}
</style>
