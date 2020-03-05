<template>
  <v-app id="app">

    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-toolbar-title>JND </v-toolbar-title>
    </v-app-bar>

    <v-content>
      <slot></slot>
    </v-content>

    <v-footer
      color="indigo"
      app
    >
      <span class="white--text">&copy; 2020</span>
    </v-footer>

  </v-app>
</template>

<script>
  export default {
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
    }),
  }
</script>