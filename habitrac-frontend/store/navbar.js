export const state = () => ({
  elements: [],
  // the `authenticated` key decides whether the link will be displayed in the navbar
  // according to authentication status
  // --> `null`: displayed always
  // --> `false`: displayed if the user is not logged in otherwise not
  // --> `true`: displayed if the user is logged in otherwise not
  allElements: [
    { label: 'Home', pathName: 'index', authenticated: null },
    { label: 'Login', pathName: 'login', authenticated: false },
    { label: 'Register', pathName: 'register', authenticated: false },
    { label: 'Profile', pathName: 'profile', authenticated: true },
    { label: 'Logout', pathName: 'logout', authenticated: true },
  ],
})

export const mutations = {
  setNavbar(state, elements) {
    state.elements = elements
  },
}

export const actions = {
  constructNavbarElements({ state, commit }) {
    const links = []
    const hasToken = this.app.$verifyAuthTokenExists()
    for (const link of state.allElements) {
      if (link.authenticated === null) {
        links.push(link)
      } else if (link.authenticated === false) {
        if (!hasToken) {
          links.push(link)
        }
      } else if (link.authenticated === true) {
        if (hasToken) {
          links.push(link)
        }
      }
    }
    commit('setNavbar', links)
  },
}
