<template>
  <div class="fixed top-0 right-0 m-3">
    <div class="flex justify-around w-full mx-auto lg:w-10/12 xl:w-8/12">
      <a href="//github.com/IgnisDa/habitrac" target="blank">
        <FontAwesomeIcon
          class="w-10 h-10 transition-colors duration-1000 fill-current sm:h-10 sm:w-10 text-true-gray-200 hover:text-true-gray-100"
          :icon="['fab', 'github']"
        ></FontAwesomeIcon>
      </a>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.color-mode-enter-active,
.color-mode-leave-active {
  transition-duration: 0.7s;
  transition-property: opacity scale;
  transition-timing-function: ease-in-out;
}

.color-mode-enter,
.color-mode-leave-to {
  @apply opacity-0 scale-75 transform;
}
</style>
