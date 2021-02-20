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
            ></div>
          </div>
          <div
            class="relative col-start-1 row-end-2 p-5 m-3 transition-colors duration-300 border rounded-md shadow-xl bg-gray-50 sm:m-0"
          >
            <div class="absolute"></div>
            <div
              class="pb-2 mb-8 text-3xl font-semibold tracking-wider text-center text-blue-500 transition-colors duration-500 border-b-4 border-blue-300 border-dashed sm:text-5xl"
            >
              Start a Habit
            </div>
            <form class="w-72 sm:w-80 md:w-96" @submit.prevent="handleSubmit()">
              <div class="mt-2 mb-5 sm:mt-0">
                <label
                  for="username"
                  class="block font-serif text-lg text-black dark:text-gray-100"
                >
                  Type
                </label>
                <div
                  class="relative w-full p-3 my-2 bg-gray-100 border rounded-sm focus-within:ring-2 focus-within:ring-blue-600"
                >
                  <div class="flex items-center">
                    <input
                      id="habit-name"
                      v-model="formData.client"
                      type="text"
                      class="w-full px-3 bg-gray-100 border-0 focus:outline-none"
                      autocomplete="off"
                      placeholder="Meditate everyday"
                      @keyup="showOptions = true"
                    />
                    <FontAwesomeIcon
                      class="flex-none w-6 h-6 text-black pointer-events-none fill-current"
                      :icon="['fas', 'clock']"
                    ></FontAwesomeIcon>
                  </div>
                  <div
                    v-show="resultQuery.length && showOptions"
                    class="absolute inset-x-0 z-10 mt-1 overflow-hidden overflow-y-scroll bg-white border border-gray-300 rounded-md shadow-md"
                  >
                    <ul class="py-1">
                      <li
                        v-for="(value, index) in resultQuery"
                        :key="index"
                        class="px-3 py-2 cursor-pointer hover:bg-gray-200"
                        @click="setInput(value.type)"
                      >
                        {{ value.type }}
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="mt-2 mb-5 sm:mt-0">
                <div class="relative w-full my-2 rounded-sm">
                  <div class="flex items-center">
                    <div class="w-full px-1">
                      <label
                        for="duration-from"
                        class="block font-serif text-lg text-black dark:text-gray-100"
                      >
                        From
                      </label>
                      <input
                        id="duration-from"
                        type="date"
                        class="w-full p-3 bg-gray-100 border duration-input focus:outline-none focus-within:ring-blue-400 focus-within:ring-2"
                        autocomplete="off"
                        placeholder="Meditate everyday"
                      />
                    </div>
                    <div class="w-full px-1">
                      <label
                        for="duration-to"
                        class="block font-serif text-lg text-black dark:text-gray-100"
                      >
                        To
                      </label>
                      <input
                        id="duration-to"
                        type="date"
                        class="w-full p-3 bg-gray-100 border duration-input focus:outline-none focus-within:ring-blue-400 focus-within:ring-2"
                        autocomplete="off"
                        placeholder="Meditate everyday"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <button
                type="submit"
                class="w-full p-3 text-lg font-semibold text-center text-indigo-700 uppercase bg-gray-200 rounded-sm focus:outline-none loading--button-border-red"
              >
                <span>Create New</span>
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    showOptions: false,
    formData: {},
    data: [
      { id: 1, type: 'Daily' },
      { id: 2, type: 'Hourly' },
    ],
  }),
  head: () => ({
    title: 'New Habit',
  }),
  computed: {
    resultQuery() {
      if (this.formData.client) {
        const data = this.data.filter((item) => {
          return this.formData.client
            .toLowerCase()
            .split(' ')
            .every((v) => item.type.toLowerCase().includes(v))
        })

        return data
      } else {
        return []
      }
    },
  },
  methods: {
    handleSubmit() {
      return ''
    },
    setInput(value) {
      this.$set(this.formData, 'client', value)
      this.$set(this.formData, 'client_id', value.id)
      this.showOptions = false
    },
  },
}
</script>

<style scoped>
.duration-input::-webkit-calendar-picker-indicator {
  margin: 0;
}
</style>
