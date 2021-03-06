<template>
  <div class="flex items-center justify-center min-h-screen">
    <div class="w-full mx-3 sm:w-4/5 md:w-1/3">
      <CodeWindow>
        <template #body>
          <div
            v-for="(link, index) in links"
            :key="index"
            class="hover:underline"
          >
            <NuxtLink :to="{ name: link.path }">{{ link.label }}</NuxtLink>
          </div>
        </template>
      </CodeWindow>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    links: [
      { label: 'My Habits', path: 'habits' },
      { label: 'My Profile', path: 'profile' },
      { label: 'Vault', path: 'vault' },
    ],
  }),
  head: () => ({
    title: 'Dashboard',
  }),
}
</script>
