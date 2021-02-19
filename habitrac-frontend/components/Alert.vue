<template>
  <div id="alert--template">
    <div v-for="alert in activeAlertsGetter" :key="alert.id">
      <div
        v-show="alert.active"
        :class="{
          'bg-green-500': alert.severity === 'success',
          'bg-blue-400': alert.severity === 'info',
          'bg-red-500': alert.severity === 'danger',
          hidden: !alert.active,
        }"
      >
        <div class="alert__heading">{{ alert.messageHeading }}</div>
        <div class="alert__body">
          {{ alert.messageBody }}
        </div>
        <div class="cursor-pointer" @click="closeAlert(alert.id)">
          <FontAwesomeIcon
            class="w-8 h-8"
            :icon="['fas', 'times-circle']"
          ></FontAwesomeIcon>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  data: () => ({
    closed: false,
  }),
  computed: {
    ...mapState({
      alerts: (state) => state.alerts.alerts,
    }),
    ...mapGetters({
      activeAlertsGetter: 'alerts/activeAlerts',
    }),
  },
  methods: {
    ...mapActions({
      disableAlertAction: 'alerts/disableAlert',
    }),
    closeAlert(id) {
      this.disableAlertAction(id)
    },
  },
}
</script>
