<template>
  <div class="flex items-center justify-center min-h-screen overflow-x-hidden">
    <div class="w-full">
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
            class="relative col-start-1 row-end-2 p-5 m-3 transition-colors duration-300 bg-gray-900 border rounded-md shadow-xl sm:m-0"
          >
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
                  class="block font-serif text-lg text-gray-100"
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
                      ref="name"
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
                        class="block font-serif text-lg text-gray-100"
                      >
                        From
                      </label>
                      <input
                        id="duration-from"
                        v-model="data.dateFrom"
                        type="date"
                        class="w-full p-3 bg-gray-100 border duration-input focus:outline-none focus-within:ring-blue-400 focus-within:ring-2"
                        required
                        :min="data.dateFrom"
                        disabled
                      />
                    </div>
                    <div class="w-full px-1 sm:w-1/2">
                      <label
                        for="duration-to"
                        class="block font-serif text-lg text-gray-100"
                      >
                        To
                      </label>
                      <input
                        id="duration-to"
                        v-model="data.dateTo"
                        type="date"
                        class="w-full p-3 bg-gray-100 border duration-input focus:outline-none focus-within:ring-blue-400 focus-within:ring-2"
                        required
                        :min="data.dateFrom"
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
              <div class="mt-2 mb-5 sm:mt-0">
                <label
                  for="habit-description"
                  class="block font-serif text-lg text-gray-100"
                >
                  Briefly description of the habit
                </label>
                <div
                  class="relative w-full p-3 my-2 bg-gray-100 border rounded-sm focus-within:ring-2 focus-within:ring-blue-600"
                >
                  <div class="flex items-center">
                    <textarea
                      id="habit-description"
                      v-model="data.description"
                      type="text"
                      class="w-full px-1 bg-gray-100 order-0 focus:outline-none"
                      autocomplete="off"
                      required
                    ></textarea>
                  </div>
                </div>
              </div>
              <div class="flex items-center mt-2 mb-5 sm:mt-0">
                <div class="p-1 my-2 rounded-sm">
                  <div class="flex items-center">
                    <input
                      id="habit-vault"
                      v-model="data.vault"
                      type="checkbox"
                    />
                  </div>
                </div>
                <label
                  for="vault"
                  class="block font-serif text-lg text-gray-100"
                >
                  Vault
                </label>
                <div class="mx-2 cursor-pointer" @click="showVaultDetails()">
                  <FontAwesomeIcon
                    class="flex-none w-5 h-5 text-gray-100 fill-current"
                    :icon="['fas', 'info-circle']"
                  ></FontAwesomeIcon>
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
import getHabitDetailsQuery from '~/apollo/queries/getHabitDetails.gql'
import updateDailyHabitMutation from '~/apollo/mutations/updateDailyHabit.gql'

export default {
  async asyncData({ app, params, $dayjs }) {
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
      if (typeof habit.progress === 'string') {
        habit.progress = JSON.parse(habit.progress)
      }
      const startedOn = $dayjs(habit.startedOn).format('YYYY-MM-DD')
      const dateTo = $dayjs(habit.dateTo).format('YYYY-MM-DD')
      const obj = {
        data: {
          dateTo,
          name: habit.name,
          description: habit.description,
          dateFrom: startedOn,
          vault: habit.vault,
        },
      }
      return obj
    }
  },
  data: () => ({
    loading: false,
    errors: { name: null, duration: null },
  }),
  head() {
    return { title: `${this.data.name} | Update` }
  },
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
  mounted() {},
  methods: {
    showVaultDetails() {
      alert(
        'The habits that are stored in the vault can only be accessed with a password. The vault can be accessed in the dashboard'
      )
    },
    async handleSubmit() {
      this.errors = { name: null, duration: null }
      this.loading = true
      const { data } = await this.$apollo.mutate({
        mutation: updateDailyHabitMutation,
        variables: {
          data: this.data,
          nameSlug: this.$route.params.slug,
        },
      })
      this.loading = false
      if (!data.updateDailyHabit.status) {
        this.errors.duration = data.updateDailyHabit.errors.duration
        this.errors.name = data.updateDailyHabit.errors.name
      } else {
        this.$addAlert({
          severity: 'success',
          messageHeading: 'Updated',
          messageBody: 'Your habit was updated successfully!',
          active: true,
        })
        this.$router.push({
          name: 'habits-slug',
          params: { slug: data.updateDailyHabit.habit.nameSlug },
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
