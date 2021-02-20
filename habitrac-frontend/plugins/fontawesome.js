import Vue from 'vue'
import { library, config } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import {
  faUserGraduate,
  faSpinner,
  faEye,
  faEyeSlash,
  faGuitar,
  faMoon,
  faUserPlus,
  faSignInAlt,
  faLightbulb,
  faCalendar,
  faUsers,
  faTimes,
  faUser,
  faClock,
} from '@fortawesome/free-solid-svg-icons'
import { faGithub } from '@fortawesome/free-brands-svg-icons'

// This is important, we are going to let Nuxt.js worry about the CSS
config.autoAddCss = false

// You can add your icons directly in this plugin. See other examples for how you
// can add other styles or just individual icons.
library.add(
  faEyeSlash,
  faTimes,
  faUser,
  faCalendar,
  faUserGraduate,
  faEye,
  faSignInAlt,
  faClock,
  faUserPlus,
  faGuitar,
  faUsers,
  faSpinner,
  faLightbulb,
  faMoon,
  faGithub
)

// Register the component globally
Vue.component('FontAwesomeIcon', FontAwesomeIcon)
