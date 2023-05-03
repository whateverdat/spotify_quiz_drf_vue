<script>
export default {
  data() {
    return {
      playing: true,
      timer: 25,
      timerClass: 'text-lime-500',
      failCounter: 0,
    };
  },
  props: {
    url: {
      required: true,
    },
    sessionPlayer: {
      default: false,
    },
  },
  methods: {
    checkPlaying(audio) {
      if (!audio.paused) {
        console.log('playing');
        this.playing = true;
        this.startCountDown();
        clearInterval(this.interval);
        return;
      }
      console.log('stopped');
      this.playing = false;
      this.failCounter++;
      if (this.failCounter === 5) {
        this.$emit('trackFailure', this.playing);
      }
      return;
    },
    countDown() {
      if (this.timer > 0) {
        this.timer -= 1;
        if (this.timer === 10) {
          this.timerClass = 'text-yellow-400';
        } else if (this.timer === 3) {
          this.timerClass = 'text-red-700';
        }
      } else {
        this.$emit('timerReachedZero', this.timer);
      }
    },
    startCountDown() {
      this.timerInt = setInterval(() => this.countDown(), 1000);
    },
  },
  created() {
    this.interval = setInterval(
      () => this.checkPlaying(this.$refs.audio),
      1000
    );
  },
  beforeUnmount() {
    clearInterval(this.interval);
    clearInterval(this.timerInt);
  },
};
</script>
<template>
  <div>
    <audio ref="audio" :src="url" autoplay></audio>
    <h1 v-if="sessionPlayer === true" :class="`transition-all ${timerClass}`">
      {{ timer }}
    </h1>
  </div>
</template>
