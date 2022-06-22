<template>
  <div class="wrapper" :class="{ 'nav-open': $sidebar.showSidebar }">
    <!-- <notifications></notifications> -->

    <side-bar
      :sidebar-item-color="sidebarBackground"
      :sidebar-background-image="sidebarBackgroundImage"
    >
      <mobile-menu slot="content"></mobile-menu>
      
      <sidebar-link to="/acceptance_letters">
        <md-icon>dashboard</md-icon>
        <p>Acceptance Letters</p>
      </sidebar-link>

      <sidebar-link to="/welcome_emails">
        <md-icon>mail</md-icon>
        <p>Welcome Emails</p>
      </sidebar-link>
      
      <sidebar-link to="/new_application_filler">
        <md-icon>content_paste</md-icon>
        <p>New Application Filler</p>
      </sidebar-link>
      
      <sidebar-link to="/computer_access_direction_emails">
        <md-icon>devices</md-icon>
        <p>computer Access directions</p>
      </sidebar-link>
    </side-bar>

    <div class="main-panel">
      <top-navbar></top-navbar>

      <dashboard-content> </dashboard-content>

      <content-footer v-if="!$route.meta.hideFooter"></content-footer>
    </div>
  </div>
</template>

<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "@/pages/Layout/MobileMenu.vue";

export default {
  components: {
    TopNavbar,
    DashboardContent,
    MobileMenu,
    ContentFooter
    // FixedPlugin,
  },
  data() {
    return {
      sidebarBackground: "green",
      sidebarBackgroundImage: require("@/assets/img/sidebar-2.jpg"),
    };
  },
};
</script>
