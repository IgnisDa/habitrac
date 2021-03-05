<template>
  <div>Index</div>
</template>

<script>
import { getCookie } from '~/utils.js'

export default {
  mounted() {
    if (!getCookie('vault-token')) {
      this.$router.push({ name: 'vault-prompt' })
      this.$addAlert({
        severity: 'danger',
        messageBody:
          'The vault token has expired, please login into the vault again.',
        messageHeading: 'Expired',
        active: true,
      })
    }
  },
}
</script>
