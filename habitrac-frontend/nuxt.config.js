export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'habitrac-frontend',
    meta: [
      { charset: 'utf-8' },
      {
        name: 'viewport',
        content: 'width=device-width, initial-scale=1, minimum-scale=1',
      },
      {
        hid: 'description',
        name: 'description',
        content:
          'A simple webapp to help you track your habits and keep you responsible for your actions',
      },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: ['~/assets/css/global.scss'],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
    '~/plugins/fontawesome.js',
    '~/plugins/alert.js',
    '~/plugins/authToken.js',
    { src: '~/plugins/confetti.js', mode: 'client' },
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/stylelint
    '@nuxtjs/stylelint-module',
    // https://go.nuxtjs.dev/tailwindcss
    '@nuxtjs/tailwindcss',
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    // https://github.com/nuxt-community/apollo-module
    '@nuxtjs/apollo',
    // https://google-fonts.nuxtjs.org/
    '@nuxtjs/google-fonts',
    // https://github.com/nuxt-community/dayjs-module
    '@nuxtjs/dayjs',
  ],

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {},

  // Added later
  telemetry: false,
  watchers: {
    webpack: {
      aggregateTimeout: 300,
      poll: 1000,
    },
  },
  target: 'server',
  // target: 'static',
  generate: {
    interval: 2000,
  },
  publicRuntimeConfig: {
    backendUrl:
      process.env.VUE_APP_BACKEND_URL || 'http://0.0.0.0:8000/graphql/',
  },
  apollo: {
    clientConfigs: {
      default: '~/configurations/apollo-config.js',
    },
    authenticationType: 'Token',
  },
  googleFonts: {
    families: {
      'Josefin+Sans': [500],
      Sacramento: true,
    },
    display: 'swap',
  },
  pageTransition: {},
  analyze: {
    analyzerMode: 'static',
  },
}
