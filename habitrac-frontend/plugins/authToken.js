export default ({ app }, inject) => {
  // this will set the $verifyAuthTokenExists helper function which will
  // return `true` if the current user is logged in, otherwise `false`
  inject('verifyAuthTokenExists', () => {
    return !!app.$apolloHelpers.getToken()
  })
}
