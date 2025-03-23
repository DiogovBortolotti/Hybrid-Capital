<template>
  <div id="home">
    <HeaderComponent />
    <MainContent />
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from "../components/Header.vue";
import MainContent from "../components/MainContent.vue";
import FooterComponent from "../components/Footer.vue";

export default {
  name: "Home",
  components: {
    HeaderComponent,
    MainContent,
    FooterComponent,
  },
};
</script>

<style scoped>
@import '../assets/styles/global.css';
</style>