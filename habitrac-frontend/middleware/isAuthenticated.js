export default ({ store, error }) => {
  store.dispatch('user/verifyLoggedIn').then((resp) => {
    if (!resp) {
      error({
        statusCode: 503,
        message: 'You are not allowed to see this',
      })
    }
  })
}
