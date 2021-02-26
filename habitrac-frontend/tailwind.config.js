const colors = require('tailwindcss/colors')

module.exports = {
  purge: [],
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    debugScreens: {
      position: ['right', 'top'],
    },
    extend: {
      fontFamily: {
        display: ['Josefin Sans', 'sans-serif'],
      },
      colors: {
        lime: colors.lime,
      },
      transitionProperty: {
        width: 'width',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [require('tailwindcss-debug-screens')],
}
