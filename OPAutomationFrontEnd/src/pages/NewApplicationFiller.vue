<template>
    <div class="content">
    <div class="md-layout" >
        <nav-tabs-card >
            <template slot="content">
            <md-tabs class="md-primary" md-alignment="centered" >
                <md-tab id="tab-home" md-label="Generate" md-icon="play_circle">
                <div class="md-layout-item md-size-50">
                    <div class="child">
                    <md-field>
                        <md-file v-model="placeholder" @change="handleFileUpload( $event )" placeholder="Choose file" />    
                    </md-field>
                    </div>
                    <div class="child">
                    <md-button class="md-primary"  @click="upload">Generate files</md-button>
                    <md-progress-spinner v-show="spinner_visiblity" class="md-primary" :md-diameter="30" :md-stroke="3" md-mode="indeterminate"></md-progress-spinner>
                    </div>
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
import axios from 'axios';

export default {
  components: {
    NavTabsCard,
    Stepper
  },
  data() {
    return {
      placeholder:"",
      file: '',
      spinner_visiblity: false
    };
  },
  methods: {
      handleFileUpload( event ){
        this.file = event.target.files[0];
      },
      upload(){
        this.spinner_visiblity = true
        let formData = new FormData();
        formData.append('file', this.file);
        const baseURI = 'http://localhost:5000/new_applications_filler'
        axios.post(baseURI,
        formData,
        {
          headers: {
              'Content-Type': 'multipart/form-data',

          },
          responseType: 'arraybuffer'
        },
        )
        .then((response) => {
          let blob = new Blob([response.data], { type: 'application/zip' })
          let link = document.createElement('a')
          link.href = window.URL.createObjectURL(blob)
          link.download = 'Download.zip'
          link.click()
          // console.log(response)
          this.spinner_visiblity = false
          this.file = ""
        })
      }
      
    }
};
</script>


<style lang="scss" scoped>
  .md-progress-spinner {
    margin: 13px 13px;
  }
  .child {
  display: inline-block;
  margin: 1rem;
  vertical-align: middle;
  width: auto;
}
</style>