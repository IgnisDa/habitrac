export default ({ store, error }) => {
  if (!process.server) {
    store.dispatch('user/verifyLoggedIn').then((resp) => {
      if (!resp) {
        error({
          statusCode: 503,
          message: 'You are not allowed to see this',
        })
      }
    })
  }
}
