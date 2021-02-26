<template>
  <div>
    <FontAwesomeIcon
      :icon="['fas', 'check']"
      :class="classes"
    ></FontAwesomeIcon>
  </div>
</template>

<script>
export default {
  props: {
    classes: {
      type: String,
      default: 'h-8 w-8',
    },
  },
}
</script>
