<template>
  <div class="flex items-center justify-center min-h-screen">
    <div>This is my profile page</div>
  </div>
</template>

<script>
export default {
  middleware: ['isAuthenticated'],
}
</script>
