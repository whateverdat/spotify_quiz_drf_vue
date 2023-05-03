<script>
import Searchbar from './components/Searchbar.vue';
export default {
  data() {
    return {
      start: false,
    };
  },
};
</script>
<template>
  <ThemeToggle></ThemeToggle>
  <div class="flex flex-col items-center" v-if="!start">
    <h2
      class="text-black text-justify bg-slate-700 bg-opacity-5 p-5 rounded-3xl mb-2 w-1/2 font-thin text-lg"
    >
      This is a single-player song quiz-app using spotify API. Enter a playlist
      name, then you can view and play 30-second previews of the songs of that
      playlist, or initiate a 'session'. In a session, available songs from the
      selected playlist will play in random order, and you will be prompted to
      guess the name of the song that is playing. Click 'Start' to proceed.
    </h2>
    <button
      class="bg-black text-white w-32 hover:opacity-90"
      @click="this.start = true"
    >
      Start
    </button>
  </div>
  <Searchbar v-else />
</template>
