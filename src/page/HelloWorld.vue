<template>
  <ContentBox>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="100"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Model JND in Charts
        </h1>

        <p class="subheading font-weight-regular" >
          The homepage holds the content of experiment and its result of modeling JND in charts. 
          
          <br>Just-noticeable difference (JND) is the amount something must be changed in order for a difference to be noticeable. 
          <br>We aim to analyze the perception of JND in chart elements in order to understand (and possibly aid) how people compare visual elements
with close quantities. 
        </p>
      </v-col>

      <v-col
        class="mb-5"
        cols="12"
      >
        <h2 class="headline font-weight-bold mb-3">
          Experiment
        </h2>
        <p>
         We study three popular charts: bar charts, pie charts and bubble charts, covering of three visual cues (height, size, and angle).
         You can try to do the test by yourself and measure your JNDs. 
        </p>
        <v-row justify="center">
          <a
            v-for="(next, i) in exp"
            :key="i"
            :href="next.href"
            class="subheading mx-3"
            target="_blank"
          >
            {{ next.text }}
          </a>
        </v-row>
      </v-col>


      <v-col
        class="mb-5"
        cols="12"
      >
        <h2 class="headline font-weight-bold mb-3">
          JND30 Experiment Data
        </h2>
        <p> We have performed an user study to collect <b>JND30</b>, the data from 30 participants in the JND test of three charts (bar chart, 
          bubble chart, and pie chart). We make the dataset public and free for academic purpose. Also, we release the statistics analysis of 
          JND30. (More detail to be added) </p>
        <v-row justify="center">
          <a
            v-for="(next, i) in expdata"
            :key="i"
            :href="next.href"
            class="subheading mx-3"
            target="_blank"
          >
            {{ next.text }}
          </a>
        </v-row>
      </v-col>
    </v-row>
  </ContentBox>
</template>

<script>
  import ContentBox from '@/components/ContentBox'
  export default {
    components:{
        ContentBox
    },
    name: 'HelloWorld',
    data: () => ({
      expdata: [
        {
          text: 'JND30 Dataset',
          href: 'https://github.com/vuetifyjs/vuetify-loader',
        },
        {
          text: 'Statistics of JND30 data (连到统计分析的网页）',
          href: 'https://github.com/vuetifyjs/vuetify-loader',
        },
      ],
      exp: [
        {
          text: 'JND Experiment Details (to be added)',
          href: 'https://github.com/vuetifyjs/vuetify',
        },
        {
          text: 'Online JND test (Try it by yourself) (连上在线测试）',
          href: 'https://github.com/vuetifyjs/vuetify',
        }
      ],     
    }),
  }
</script>
