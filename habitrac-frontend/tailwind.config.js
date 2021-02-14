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
      transitionProperty: {
        width: 'width',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [
    require('tailwindcss-debug-screens'),
    require('@tailwindcss/forms'),
  ],
}
