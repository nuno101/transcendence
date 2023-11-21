<template>
  <div class="lang-selection">
    <select v-model="selected" @change="changeLocale">
        <option
          v-for="lang in languages"
          :key="lang.title"
          :value="lang.language"
        >{{lang.title}}</option>
    </select>
  </div>
</template>

<script setup>
    import {ref, onMounted} from 'vue';
    import i18n from "../../plugins/i18n";
    import "../../colors.css";

  const selected = ref('');

  const languages = ref([
    { language: 'en', title: 'English' },
    { language: 'es', title: 'Español' },
    { language: 'fr', title: 'French' },
    { language: 'de', title: 'German' }
  ]);

  const changeLocale = (event) => {
    const selectedLocale = event.target.value;
    console.log('Selected locale:', selectedLocale);
    // Verify that 'locale' is a valid locale string (e.g., 'en', 'es', etc.)
    if (typeof selectedLocale === 'string') {
      i18n.global.locale.value = selectedLocale;
      localStorage.setItem('selected', selectedLocale);
    } else {
      console.error('Invalid selectedLocale:', selectedLocale);
    }
  };

  // to preserve the selected language across all sites
  onMounted(() => {
    const storedLang = localStorage.getItem('selected');
    if (storedLang) {
      selected.value = storedLang;
      i18n.global.locale.value = storedLang;
    } else {
      // Set default language if not stored in localStorage
      const defaultLang = 'en';
      selected.value = defaultLang;
      i18n.global.locale.value = defaultLang;
      localStorage.setItem('selected', defaultLang);
    }
    console.log('Mounted phase - selectedLang in LanguageSelection:', selected.value);
  });
</script>

<style scoped>
.lang-selection {
  position: fixed;
  top: 10px;
  right: 10px;
}
</style>

// how to handle lanugages in Vue 3
// https://lokalise.com/blog/vue-i18n/