<template>
<div>

    <v-container class="my-10">
      <v-layout row justify-center>
        <v-flex lg8 md8 sm8>

        <h2>
            Homepage for JND Modeling in Three Chart
        </h2>

          <v-divider></v-divider>

        <v-list>
             <v-list-item-group v-model="model">

            <v-list-item> Bar Chart (part 1)  <a href="http://47.103.22.185:7009/barinfo">  >> </a> </v-list-item>

            <v-list-item> Bar Chart (part 2) <a href="http://47.103.22.185:7011/barinfo">>></a> </v-list-item>
            
            <v-list-item> Pie Chart (part 1) <a href="http://47.103.22.185:7009/pieinfo">>></a> </v-list-item>
            
            <v-list-item> Pie Chart (part 2) <a href="http://47.103.22.185:7011/pieinfo">>></a> </v-list-item>

            <v-list-item> Bubble Chart (part 1) <a href="http://47.103.22.185:7009/bubbleinfo">>></a> </v-list-item>
            
            <v-list-item> Bubble Chart (part 2) <a href="http://47.103.22.185:7011/bubbleinfo">>></a> </v-list-item>

            </v-list-item-group>

        </v-list>

        </v-flex>
      </v-layout>
    </v-container>
  </div>
  
</template>

<script>


export default {
    name: 'App',
    data: () => ({
     }),
}
</script>