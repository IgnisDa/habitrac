export default ({ store, error }) => {
  store.dispatch('user/verifyLoggedIn').then((resp) => {
    if (!resp) {
      error({
        statusCode: 401,
        message: 'You are not allowed to see this page',
      })
    }
  })
}
