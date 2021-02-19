import tokenAuthMutation from '~/apollo/mutations/tokenAuth.gql'
import createUserMutation from '~/apollo/mutations/createUser.gql'
import userDetailsQuery from '~/apollo/queries/userDetails.gql'

export const state = () => ({
  user: null,
})

export const mutations = {
  setUser(state, user) {
    state.user = user.user
  },
}

export const actions = {
  verifyLoggedIn() {
    return !!this.app.$apolloHelpers.getToken()
  },
  async createUser(_context, payload) {
    const apolloClient = this.app.apolloProvider.defaultClient
    return await apolloClient
      .mutate({
        mutation: createUserMutation,
        variables: {
          data: {
            username: payload.username,
            password: payload.password,
          },
        },
      })
      .then(({ data }) => {
        return data.createUser
      })
  },
  async fetchTokenAuth(_context, payload) {
    const apolloHelpers = this.app.$apolloHelpers
    const apolloClient = this.app.apolloProvider.defaultClient
    return await apolloClient
      .mutate({
        mutation: tokenAuthMutation,
        variables: {
          username: payload.username,
          password: payload.password,
        },
        errorPolicy: 'all',
      })
      .then((resp) => {
        if (resp.errors) {
          return resp.errors
        } else {
          apolloHelpers.onLogin(resp.data.tokenAuth.token)
        }
      })
  },
  async fetchUserDetails({ commit }) {
    const apolloClient = this.app.apolloProvider.defaultClient
    try {
      await apolloClient
        .query({
          query: userDetailsQuery,
          // The following code will add a custom header to the request on a per-request
          // basis. Make sure you add the custom header name in the `CORS_ALLOW_HEADERS`
          // list on the backend otherwise your requests will be rejected.
          // context: {
          //   headers: {
          //     'X-Example-Header': `some-custom-value`,
          //   },
          // },
        })
        .then(({ data }) => {
          commit('setUser', data.userDetails)
        })
    } catch (error) {
      alert('We encountered a problem trying to log you in, please try again!')
    }
  },
}
