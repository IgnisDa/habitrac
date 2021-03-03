const colors = require('tailwindcss/colors')

module.exports = {
  purge: [],
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    debugScreens: {
      position: ['left', 'bottom'],
    },
    extend: {
      fontFamily: {
        display: ['Josefin Sans', 'sans-serif'],
        handwriting: ['Sacramento', 'cursive'],
      },
      colors: {
        lime: colors.lime,
        'true-gray': colors.trueGray,
      },
      transitionProperty: {
        width: 'width',
      },
    },
  },
  variants: {
    extend: {
      space: ['hover'],
      animation: ['hover'],
    },
  },
  plugins: [require('tailwindcss-debug-screens')],
}
