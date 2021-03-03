export default ({ store, error }) => {
  store.dispatch('user/verifyLoggedIn').then((resp) => {
    if (!resp) {
      error({
        statusCode: 401,
        message: 'You cannot see this page until you log in',
      })
    }
  })
}
