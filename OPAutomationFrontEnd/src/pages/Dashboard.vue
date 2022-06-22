<template>

  <div class="content">
    <div class="md-layout">
        <nav-tabs-card>
          <template slot="content">
            <md-tabs class="md-success" md-alignment="left">
              <md-tab id="tab-home" md-label="Generate" md-icon="play_circle">
                <!-- <nav-tabs-table></nav-tabs-table> -->
              </md-tab>

              <md-tab id="tab-pages" md-label="Configure" md-icon="tune">
                <!-- <nav-tabs-table></nav-tabs-table> -->
              </md-tab>

            </md-tabs>
          </template>
        </nav-tabs-card>
    </div>
  </div>
</template>

<script>
import {
  NavTabsCard,
} from "@/components";

export default {
  components: {
    NavTabsCard,
  },
  data() {
    return {
    };
  },
};
</script>
