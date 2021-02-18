<template>
  <div>{{ user }}</div>
</template>

<script>
import userProfileDetailsQuery from '~/apollo/queries/userProfileDetails.gql'

export default {
  async asyncData({ app, params, error }) {
    const apolloClient = app.apolloProvider.defaultClient
    return await apolloClient
      .query({
        query: userProfileDetailsQuery,
        variables: {
          id: Number(params.id),
        },
      })
      .then(({ data }) => {
        return { user: data.userProfileDetails.username }
      })
  },
}
</script>
