<template>
  <div class="flex items-center justify-center h-screen">
    <ol
      class="flex flex-col w-full p-3 mx-3 space-y-2 overflow-auto list-decimal list-inside bg-gray-200 divide-y divide-purple-200 rounded-lg shadow-lg sm:w-3/5 h-4/6 sm:h-5/6 sm:mx-0"
    >
      <client-only>
        <li v-for="(user, index) in users" :key="index">
          <NuxtLink
            :to="{ name: 'users-slug', params: { slug: user.usernameSlug } }"
          >
            <span
              class="text-blue-800 hover:text-blue-700 hover:underline sm:text-lg"
              >{{ user.username }}</span
            >
          </NuxtLink>
        </li>
      </client-only>
    </ol>
  </div>
</template>

<script>
import getUsersListQuery from '~/apollo/queries/getUsersList.gql'

export default {
  apollo: {
    users: {
      query: getUsersListQuery,
      update: (value) => {
        return value.getUsersList
      },
      prefetch: false,
    },
  },
}
</script>
