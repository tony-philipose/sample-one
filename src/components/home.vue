<template>
  <div>
    <div class="row">
      <div class="col-md-12 col-sm-12 col-xs-12 col-lg-12">
        <div class="bar">
          <input type="text" v-on:keyup="search()"  class="search" placeholder="Search here">
        </div>
      </div>
    </div>
    <div class="row tab" >
      <div class="col-md-4 col-sm-4 col-xs-4 col-lg-4">
        <div class="btn_sm" v-on:click="tech()" >
        Technology
        </div>
      </div>
      <div class="col-md-4 col-sm-4 col-xs-4 col-lg-4">
        <div class="btn_sm" v-on:click="spotrs()" >
        Sports
        </div>
      </div>
      <div class="col-md-4 col-sm-4 col-xs-4 col-lg-4">
        <div class="btn_sm" v-on:click="science()" >
        Science
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12 col-sm-12 col-xs-12 col-lg-12">
        <div v-for="joke in fst" :key="joke.id">
          <div class="card">
            <h4>{{ joke.title }}</h4>
            <p>{{ joke.description }}</p>
            <img :src="joke.urlToImage" width="60%" height="17%">
            <br>
            <a v-bind:href="joke.url">Read more</a>
            <br>
          </div>
        </div>
        
        <div v-if="n < m" class="btn_sm" v-on:click="dataProcess()" >
          Load more
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      jokes: [],
      fst: [],
      count: 0,
      m: 0,
      n: 0,
      tec: 'yes',
      spo: 'no',
      gen: 'no'
    }
  },
  mounted () {
    this.fetchNews()
  },
  methods: {
    fetchNews: async function () {
      try {
        if (this.tec === 'yes') {
          await axios.get('http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=5add2cd10259480fa9b7ea528e4b034c').then(response => {
            this.jokes = response.data.articles
            this.m = this.jokes.length
            this.dataProcess()
            console.log(this.jokes.length)
          })
        } else if (this.spo === 'yes') {
          await axios.get('https://newsapi.org/v2/top-headlines?sources=espn&apiKey=5add2cd10259480fa9b7ea528e4b034c').then(response => {
            this.jokes = response.data.articles
            this.m = this.jokes.length
            this.dataProcess()
            console.log(this.jokes.length)
          })
        } else if (this.gen === 'yes') {
          await axios.get('https://newsapi.org/v2/top-headlines?sources=new-scientist&apiKey=5add2cd10259480fa9b7ea528e4b034c').then(response => {
            this.jokes = response.data.articles
            this.m = this.jokes.length
            this.dataProcess()
            console.log(this.jokes.length)
          })
        }
      } catch (err) {
        console.log(err)
      }
    },
    dataProcess: function () {
      for (let key = this.count; key < this.jokes.length; key++) {
        this.count = this.count + 1
        if (this.count % 3 === 0) {
          this.fst.push(this.jokes[key])
          this.n = this.fst.length
          console.log(this.fst.length)
          break
        } else {
          console.log(this.count)
          this.fst.push(this.jokes[key])
          this.n = this.fst.length
          console.log(this.fst.length)
        }
      }
    },
    tech: function () {
      this.tec = 'yes'
      this.spo = 'no'
      this.gen = 'no'
      this.fst = []
      this.fetchNews()
    },
    spotrs: function () {
      this.tec = 'no'
      this.spo = 'yes'
      this.gen = 'no'
      this.fst = []
      this.fetchNews()
    },
    science: function () {
      this.tec = 'no'
      this.spo = 'no'
      this.gen = 'yes'
      this.fst = []
      this.fetchNews()
    }
  }
}
</script>
<style scoped>
  .card {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
     width: 70%;
    margin-left: 15%;
    margin-top: 5%;
    background-color: #fff;
}

.bar {
   background-color: #729d39;
   margin-top:0%;
}

.newsbg{
    background-color: #fbfad3;
}
.btn_sm {
  margin-top:3%;
  color:#fff;
  background-color: #729d39;
  width: 140px;
  height: 40px;
  font-size: 1.2em;
  text-align: center;
  padding-top: 8px;
  border-radius: 0.375rem;
  font-family: 'Slack-Lato','Roboto',Arial, Helvetica, sans-serif;
  -webkit-box-shadow: -3px 13px 31px -4px rgba(39,39,39,0.52);
  -moz-box-shadow: -3px 13px 31px -4px rgba(39,39,39,0.52);
  box-shadow: -3px 13px 31px -4px rgba(39,39,39,0.52);
  cursor: pointer;
  transition: 0.3s;
  margin-left: 43%;
  margin-bottom: 5%;
}

.search {
  width:65%;
  height:20px;
  padding: 15px;
  font-size:17px;
}
h4{
    color: #36622b;
    padding-top: 15px;
    font-weight: 800;
}
.more{
    color: #36622b;
}
</style>