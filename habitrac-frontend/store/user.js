import getAuthTokenMutation from '~/apollo/mutations/getAuthToken.gql'
import createUserMutation from '~/apollo/mutations/createUser.gql'
import userDetailsQuery from '~/apollo/queries/userDetails.gql'

export const state = () => ({
  user: {
    username: null,
    usernameSlug: null,
  },
})

export const mutations = {
  setUser(state, user) {
    state.user = user.user
  },
  deleteUser(state) {
    state.user = {
      username: null,
      usernameSlug: null,
    }
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
            identifier: payload.identifier,
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
        mutation: getAuthTokenMutation,
        variables: {
          identifier: payload.identifier,
          password: payload.password,
        },
        errorPolicy: 'all',
      })
      .then((resp) => {
        if (resp.data.getAuthToken.error) {
          return resp.data.getAuthToken.error
        } else {
          apolloHelpers.onLogin(resp.data.getAuthToken.auth.token)
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
          fetchPolicy: 'network-only',
        })
        .then(({ data }) => {
          commit('setUser', data.userDetails)
        })
    } catch (error) {
      // This took some time to figure out, but here's the deal:

      // Suppose you have two devices- A and B. You login on device A and then on device B.
      // The package used for authentication in the backend (ariadne_token_auth) supplies
      // them both with just one authentication token (ie both the authentication tokens on
      // device A and B are the same). Now suppose you log out on device B and then login
      // there again. Everything will work fine. However, when you use the website from
      // device A, even though it would look like you are logged in (since you DO have an
      // authentication token set in localStorage), you would actually have the wrong token
      // (that is, the older one) and thus get authentication errors. This is not a problem
      // on the frontend, but a shortcoming on the backend authentication. The solution I
      // am going with, for the time being, is to ask the user to login again if an error
      // is raised here.
      this.app.$apolloHelpers.onLogout()
      this.$addAlert({
        severity: 'danger',
        messageHeading: 'Logged Out',
        messageBody:
          'You have been logged out from another device. Please login again.',
        active: true,
      })
      this.$router.push({ name: 'login' })
    }
  },
}
