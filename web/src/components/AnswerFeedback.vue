<script>
export default {
  data() {
    return { class: this.determineClass(this.feedback) };
  },
  props: ['feedback'],
  methods: {
    determineClass(text) {
      if (
        text.includes('Incorrect, the answer was') ||
        text.includes('Out of time, the answer was')
      ) {
        return 'text-red-700';
      } else if (text.includes('Error, track could not be played.')) {
        return 'text-yellow-400';
      } else {
        return 'text-lime-500';
      }
    },
  },
};
</script>
<template>
  <div>
    <h3 :class="class">{{ feedback }}</h3>
  </div>
</template>
