<template>
  <div>{{ users }}</div>
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
    },
  },
}
</script>
