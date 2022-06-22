import DashboardLayout from "@/pages/Layout/DashboardLayout.vue";

import Dashboard from "@/pages/Dashboard.vue";
import AcceptanceLetters from "@/pages/AcceptanceLetters.vue";
import WelcomeEmails  from "@/pages/WelcomeEmails.vue";
import NewApplicationFiller from "@/pages/NewApplicationFiller.vue";
import ComputerAccessDirections from "@/pages/ComputerAccessDirections.vue";


const routes = [
  {
    path: "/",
    component: DashboardLayout,
    redirect: "/acceptance_letters",
    children: [
      {
        path: "acceptance_letters",
        name: "Acceptance Letters",
        component: AcceptanceLetters,
      },
      {
        path: "welcome_emails",
        name: "Welcome Emails",
        component: WelcomeEmails,
      },
      {
        path: "new_application_filler",
        name: "New Application Filler",
        component: NewApplicationFiller,
      },
      {
        path: "computer_access_direction_emails",
        name: "Computer Access Direction Emails",
        component: ComputerAccessDirections,
      },
    ],
  },
];

export default routes;
