<template>
  <div class="min-h-screen text-gray-300 bg-center bg-no-repeat bg-cover">
    <div
      class="flex flex-wrap min-h-screen mx-auto overflow-hidden lg:w-10/12 xl:w-8/12"
    >
      <div
        class="flex flex-col items-center justify-center w-full overflow-hidden sm:w-1/2"
      >
        <div
          class="p-2 text-indigo-700 underline text-7xl md:text-8xl 2xl:text-9xl font-display"
        >
          Habitrac
        </div>
        <div
          class="text-2xl italic tracking-widest text-white sm:text-3xl md:text-4xl font-handwriting"
        >
          Track your habits elegantly
        </div>
      </div>
      <div class="relative w-full mb-32 overflow-hidden sm:mb-0 sm:w-1/2">
        <transition-group
          tag="div"
          class="flex items-center justify-center h-full px-3"
          :name="slideTransitionName"
        >
          <div
            :key="currentSlide"
            class="absolute flex flex-col items-center justify-center space-y-3 h-3/4"
          >
            <div
              class="flex flex-col items-center space-y-5 text-true-gray-200"
            >
              <div class="border border-yellow-300 rounded-lg">
                <FontAwesomeIcon
                  class="flex-none w-16 h-16 p-3 cursor-pointer sm:h-24 sm:w-24"
                  :class="{ 'animate-bounce': confetti }"
                  :icon="['fas', traits[currentSlide].icon]"
                  @click="confetti = !confetti"
                ></FontAwesomeIcon>
              </div>
              <div class="flex justify-between space-x-10 font-extrabold">
                <button
                  class="flex items-center justify-center w-8 h-8 text-lg text-red-100 transition-transform duration-300 transform focus:outline-none sm:text-2xl md:text-4xl sm:h-12 s2m:w-12 md:h-16 md:w-16 hover:scale-150"
                  @click="changeSlide(-1)"
                >
                  &#10094;
                </button>
                <button
                  class="flex items-center justify-center w-8 h-8 text-lg text-red-100 transition-transform duration-300 transform focus:outline-none sm:text-2xl md:text-4xl sm:h-12 sm:w-12 md:h-16 md:w-16 hover:scale-150"
                  @click="changeSlide(1)"
                >
                  &#10095;
                </button>
              </div>
            </div>
            <div
              class="w-full px-3 font-serif text-lg text-center transition-colors duration-1000 sm:px-0 sm:w-4/5 md:w-4/5 sm:text-xl md:text-3xl text-true-gray-200"
            >
              {{ traits[currentSlide].text }}
            </div>
          </div>
        </transition-group>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data: () => ({
    traits: [
      {
        icon: 'user-graduate',
        text:
          'Keep yourself accountable, whether you are a student or a professional.',
      },
      {
        icon: 'clock',
        text:
          'Make the best use of your present, after-all it is the only one you have.',
      },
      {
        icon: 'guitar',
        text: 'Pursue your hobbies by keeping yourself answerable.',
      },
      {
        icon: 'users',
        text:
          'Time better managed automatically means more free time on hand. Why not use it to meet some people and have fun together?',
      },
    ],
    currentSlide: 0,
    slideTransitionName: '',
    confetti: false,
  }),
  head: () => ({
    title: 'Habitrac',
  }),
  watch: {
    confetti(newValue) {
      if (newValue === true) this.startConfetti()
      else this.stopConfetti()
    },
  },
  beforeDestroy() {
    this.stopConfetti()
  },
  methods: {
    ...mapActions({
      fetchUserDetailsAction: 'user/fetchUserDetails',
    }),
    startConfetti() {
      this.$confetti.start({
        particlesPerFrame: 0.7,
        particles: [
          {
            type: 'heart',
            dropRate: 6,
          },
          {
            type: 'circle',
            size: 3,
          },
        ],
      })
    },
    stopConfetti() {
      this.$confetti.stop()
    },
    changeSlide(number) {
      if (number === 1) {
        this.slideTransitionName = 'slide-next'
      } else {
        this.slideTransitionName = 'slide-prev'
      }
      const traitLength = this.traits.length - 1
      if (number === -1 && this.currentSlide === 0) {
        this.currentSlide = traitLength
      } else if (number === 1 && this.currentSlide === traitLength) {
        this.currentSlide = 0
      } else {
        this.currentSlide += number
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.slide-next-enter-active,
.slide-next-leave-active,
.slide-prev-enter-active,
.slide-prev-leave-active {
  transition: transform 0.5s ease-in-out;
}

.slide-next-enter {
  transform: translate(100%);
}

.slide-next-leave-to {
  transform: translate(-100%);
}

/* GO TO PREVIOUS SLIDE */
.slide-prev-enter {
  transform: translate(-100%);
}

.slide-prev-leave-to {
  transform: translate(100%);
}
</style>
