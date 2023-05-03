<script>
export default {
  data() {
    return {
      nowPlaying: false,
      sessionTracks: [...this.session['tracks']],
      incorrects: Array,
      correct: null,
      questionArray: Array,
      url: null,
      loadingTrack: false,
      answerFeedback: null,
      correctGuesses: 0,
      wrongGuesses: 0,
      titleScreen: false,
    };
  },
  props: ['session'],
  methods: {
    selectRandom() {
      // Initialize a pool to select from, and variables to store correct and incorrect tracks
      let array = [...this.sessionTracks];
      let incorrects = [];
      let correct = [];
      // If there are equal or less than 3 songs left, they cannot be used to create incorrects array
      if (array.length <= 3) {
        // So, create a new pool to select from
        let all_tracks = [...this.session['tracks']];
        while (incorrects.length < 3) {
          let rnd_idx = Math.floor(Math.random() * all_tracks.length);
          if (!array.includes(all_tracks[rnd_idx])) {
            incorrects.push(all_tracks[rnd_idx]);
            all_tracks.splice(rnd_idx, 1);
          }
        }
        // If there are more than 3 songs, it is all good and incorrects array can be fromed from the same pool
      } else {
        for (let i = 0; i < 3; i++) {
          let rnd_idx = Math.floor(Math.random() * array.length);
          incorrects.push(array[rnd_idx]);
          array.splice(rnd_idx, 1);
        }
      }
      // Select a correct song
      let rnd_idx = Math.floor(Math.random() * array.length);
      correct = array[rnd_idx];
      let correct_idx = this.sessionTracks.indexOf(correct);
      // Remove the correct song from pool, therefore it will not appear again, not as a correct or incorrect option
      this.sessionTracks.splice(correct_idx, 1);
      this.incorrects = incorrects;
      this.correct = correct;
    },
    createQuestionArray() {
      // There are no tracks left unanswered, exit
      if (this.sessionTracks.length == 0) {
        this.nowPlaying = false;
        this.loadingTrack = false;
        this.url = null;
        this.titleScreen = true;
        return;
      }
      this.loadingTrack = true;
      this.selectRandom();
      console.log(this.correct['name']);
      for (let i = 0; i < this.incorrects.length; i++) {
        console.log(this.incorrects[i]['name']);
      }
      console.log(this.session['tracks'].length);
      console.log(this.sessionTracks.length);
      // Combine correct and incorrect tracks in an array then shuffle it
      this.questionArray = this.incorrects.concat(this.correct);
      this.shuffle(this.questionArray);
      this.playSelected();
    },
    playSelected() {
      this.url = this.correct.preview_url;
      // If the selected song does not have a preview_url, repeat
      if (!this.url) {
        this.createQuestionArray();
      } else {
        this.nowPlaying = true;
        this.loadingTrack = false;
      }
    },
    async flashAlert(text) {
      this.answerFeedback = text;
      this.nowPlaying = false;
      await new Promise((resolve) => setTimeout(resolve, 3000));
      this.createQuestionArray();
    },
    //https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array
    shuffle(array) {
      let currentIndex = array.length,
        randomIndex;
      // While there remain elements to shuffle.
      while (currentIndex != 0) {
        // Pick a remaining element.
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;
        // And swap it with the current element.
        [array[currentIndex], array[randomIndex]] = [
          array[randomIndex],
          array[currentIndex],
        ];
      }
      return array;
    },
    syncTimer() {
      try {
        return this.$refs.player.timer;
      } catch (typeError) {
        return null;
      }
    },
  },
};
</script>
<template>
  <Player
    ref="player"
    v-if="nowPlaying"
    :url="url"
    :session-player="true"
    @timerReachedZero="
      flashAlert(`Out of time, the answer was ${correct.name}`);
      this.wrongGuesses++;
    "
    @trackFailure="flashAlert('Error, track could not be played.')"
  ></Player>
  <section v-if="nowPlaying">
    <ul>
      <li
        v-for="question in questionArray"
        class="text-black cursor-pointer m-5 hover:text-gray-400"
        @click="
          if (question.name === correct.name) {
            flashAlert('Correct!');
            this.correctGuesses++;
          } else {
            flashAlert(`Incorrect, the answer was ${correct.name}`);
            this.wrongGuesses++;
          }
        "
      >
        {{ question.name }}
      </li>
    </ul>
  </section>
  <div v-if="!nowPlaying && !loadingTrack && !titleScreen">
    <answerFeedback
      v-if="answerFeedback"
      :feedback="answerFeedback"
    ></answerFeedback>
    <div v-else>
      <button class="bg-lime-500 text-white" @click="createQuestionArray()">
        BEGIN!
      </button>
      <h3 class="text-black">List of Available Tracks</h3>
      <ul class="text-black">
        <li v-for="track in sessionTracks">
          <h5 class="text-gray-400" v-if="track.preview_url">
            {{ track.name }}
          </h5>
        </li>
      </ul>
    </div>
    <div v-if="loadingTrack">
      <h3 class="text-black">Loading Track...</h3>
    </div>
  </div>
  <button
    class="bg-red-700 text-white"
    v-if="nowPlaying"
    @click="
      this.titleScreen = true;
      this.nowPlaying = false;
    "
  >
    End Session
  </button>
  <TitleScreen
    v-if="titleScreen"
    :wrong="wrongGuesses"
    :correct="correctGuesses"
  ></TitleScreen>
</template>
