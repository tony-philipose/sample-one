<template>
<div id="app">
  <div class="row">
    <div class="col-md-2 col-sm-1 col-xs-1 col-lg-3"></div>
    <div class="col-md-8 col-sm-10 col-xs-10 col-lg-6">
      <div class="row">
        <div class="col-md-12 col-sm-12 col-xs-12 col-lg-12">
        <center>
          <img src="../assets/inews.png" class="icn" alt="icn"><br>
        </center>
        </div> 
      </div>
    </div>
    <div class="col-md-2 col-sm-1 col-xs-1 col-lg-3"></div>
  </div>  

<div class="row">
  <div class="col-md-12 col-sm-12 col-xs-12 col-lg-12">
  <div id="progress-container">
    <div id="progress" class="progress-bar-striped" :style="{width: progressWidth + '%'}">{{ progressWidth }}%</div>
  </div>
  </div>
</div>
<div class="row">
    <div class="col-md-4 col-sm-3 col-xs-2 col-lg-4"></div>
    <div class="col-md-4 col-sm-6 col-xs-8 col-lg-4">
  <center class="link">
    <router-link v-if="progressWidth == 100" class="btn_sm" to="/home" >
              Get Start
    </router-link>
  </center>  
  </div>
  <div class="col-md-4 col-sm-3 col-xs-2 col-lg-4"></div>
  </div>
</div>
</template>
<script>
  export default {
  name: 'load',
  data () {
    return {
      progressWidth: 0, // initial width = 0
    duration: 5 * 1000, // concert duration, ms
    start: (new Date()).valueOf() 
    }
  },
   computed: {
    end: function() { // when event finishes
      return this.start + this.duration;
    }
  },
  methods: {
    startEvent: function(start, end) {
      const int = setInterval(() => { // calculate width periodically
        const now = (new Date()).valueOf();
        if (now >= end) { // if finished
          this.progressWidth = 100;
          clearInterval(int); return;
        };
        return this.progressWidth = ((now - start)/(end - start)) * 100;
      }, 10)
    }
  },
  mounted() {
    let v = this.startEvent(this.start, this.end) // start event
  }
}  
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped >
#progress-container {
  width: 100%;
  border: 1px solid #fff;
  height: 20px;
}

#progress {
  height: 100%;
  width: 0%;
  background-color: #729d39;
  color:#fff;
}

.icn{
  width: 705;
  height: 150px;;
}
.btn_sm {
  margin-top:10%;
  color:#fff;
  background-color: #729d39;
      width: 111px;
    height: 40px;
  font-size: 21px;
  text-align: center;
  padding: 7px;
  border-radius: 20px;
  font-family: 'Slack-Lato','Roboto',Arial, Helvetica, sans-serif;
  box-shadow: 0 6px 6px 0 rgba(0,0,0,0.2);
  cursor: pointer;
  transition: 0.3s;
}
.link{
  margin-top: 10%;
}
</style>
