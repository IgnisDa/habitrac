<template>
  <div class="flex items-center justify-center min-h-screen">
    <div class="w-full mx-3 sm:w-4/5 md:w-1/3">
      <CodeWindow>
        <template #body>
          <div class="hover:underline">
            <NuxtLink :to="{ name: 'habits' }">My Habits</NuxtLink>
          </div>
          <div class="hover:underline">
            <NuxtLink :to="{ name: 'profile' }">My Profile</NuxtLink>
          </div>
        </template>
      </CodeWindow>
    </div>
  </div>
</template>

<script>
export default {
  head: () => ({
    title: 'Dashboard',
  }),
}
</script>
