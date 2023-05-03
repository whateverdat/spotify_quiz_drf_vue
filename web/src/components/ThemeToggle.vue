<script>
export default {
  data() {
    return {
      state: false,
    };
  },
  methods: {
    setTheme() {
      let body = document.querySelector('body');
      if (!this.state) {
        body.classList.remove('bg-white');
        body.classList.add('bg-slate-600');
        this.state = true;
      } else {
        body.classList.remove('bg-slate-600');
        body.classList.add('bg-white');
        this.state = false;
      }
    },
  },
};
</script>
<template>
  <div class="absolute top-1 right-1">
    <button @click="setTheme()">Theme</button>
  </div>
</template>
