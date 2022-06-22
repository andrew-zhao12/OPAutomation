<template>
    <div class="content">
    <div class="md-layout" >
        <nav-tabs-card >
            <template slot="content">
            <md-tabs class="md-primary" md-alignment="centered" >
                <md-tab id="tab-home" md-label="Generate" md-icon="play_circle">
                <div class="md-layout-item md-size-50 abcs">
                    <md-field>
                        <md-file v-model="placeholder" placeholder="Choose file" />    
                        <md-button class="md-primary" @click="upload">Generate files</md-button>
                    </md-field>
                </div>
                </md-tab>
                
                <md-tab id="tab-pages" md-label="Configure" md-icon="tune">
                <Stepper/>
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
  Stepper
} from "@/components";

export default {
  components: {
    NavTabsCard,
    Stepper
  },
  data() {
    return {
      placeholder:""
    };
  },
  methods: {
      upload(){
        
      }
      
    }
};
</script>


