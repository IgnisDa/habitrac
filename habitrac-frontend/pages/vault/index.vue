<template>
  <div class="flex items-center justify-center h-screen">
    <div class="w-full mx-3 sm:w-4/5 md:w-1/3">
      <CodeWindow>
        <template #body>
          <div v-if="loading">Loading...</div>
          <div v-else>
            <div v-if="habits.length > 0">
              <div v-for="(habit, index) in habits" :key="index">
                <NuxtLink
                  :to="{
                    name: 'habits-slug',
                    params: { slug: habit.nameSlug },
                  }"
                >
                  <span class="text-true-gray-200 hover:underline sm:text-lg">
                    {{ habit.name }}
                  </span>
                </NuxtLink>
              </div>
            </div>
            <div v-else class="text-center">
              You have not created any habits to track. Create one
              <NuxtLink
                :to="{ name: 'habits-create' }"
                class="text-blue-600 hover:underline"
              >
                here</NuxtLink
              >.
            </div>
          </div>
        </template>
      </CodeWindow>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import getVaultHabitsQuery from '~/apollo/queries/getVaultHabits.gql'
import checkIfVaultPasswordSetQuery from '~/apollo/queries/checkIfVaultPasswordSet.gql'
import { getCookie } from '~/utils.js'

export default {
  data: () => ({ habits: [], loading: false }),
  computed: {
    ...mapState({
      usernameSlug: (state) => state.user.user.usernameSlug,
    }),
  },
  async mounted() {
    const {
      data: { checkIfVaultPasswordSet: data },
    } = await this.$apollo.query({
      query: checkIfVaultPasswordSetQuery,
      fetchPolicy: 'network-only',
    })
    console.log(data)
    if (!data) {
      this.$addAlert({
        severity: 'warning',
        messageBody: 'You have not set a vault password.',
        messageHeading: 'No password',
        active: true,
      })
      this.$router.push({ name: 'vault-first' })
    } else if (!getCookie('vault-token')) {
      this.$addAlert({
        severity: 'danger',
        messageBody:
          'The vault token has expired, please login into the vault again.',
        messageHeading: 'Expired',
        active: true,
      })
      this.$router.push({ name: 'vault-prompt' })
    } else {
      this.loading = true
      await this.fetchUserDetailsAction()
      await this.$apollo
        .query({
          query: getVaultHabitsQuery,
          variables: {
            usernameSlug: this.usernameSlug,
          },
          fetchPolicy: 'network-only',
        })
        .then(({ data: { getVaultHabits: data } }) => {
          this.habits = data
          this.loading = false
        })
    }
  },
  methods: {
    ...mapActions({
      fetchUserDetailsAction: 'user/fetchUserDetails',
    }),
  },
}
</script>
