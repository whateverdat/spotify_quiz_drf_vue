<script>
import Player from './Player.vue';

export default {
  data() {
    return {
      previewURL: null,
      nowPlaying: null,
      previewLoading: false,
      previewError: false,
    };
  },
  props: ['tracks', 'tracksError', 'tracksLoading'],
  methods: {
    getPreview(url) {
      this.previewLoading = true;
      this.previewURL = url;
      console.log(this.previewURL);
      this.previewLoading = false;
    },
  },
  components: { Player },
};
</script>
<template>
  <Player v-if="previewURL" :url="previewURL"></Player>
  <section v-if="tracksError">
    <h3 class="text-black">ERROR</h3>
  </section>
  <section v-else>
    <div v-if="tracksLoading">
      <h3 class="text-black">Loading...</h3>
    </div>
    <div v-else>
      <ul>
        <li v-for="track in tracks" class="text-black mt-5">
          <div v-if="track.preview_url">
            <h3>{{ track.name }}</h3>
            <h4>{{ track.album }}</h4>
            <img class="w-32 mx-auto" :src="track.image" :alt="track.name" />
            <form>
              <button v-if="previewLoading" type="submit" disabled>
                Loading
              </button>
              <button
                v-else-if="!previewURL || nowPlaying != track.spotifyID"
                type="submit"
                @click.prevent="
                  getPreview(track.preview_url);
                  nowPlaying = track.spotifyID;
                "
              >
                Play
              </button>
              <button
                v-else-if="previewURL && nowPlaying == track.spotifyID"
                @click.prevent="
                  previewURL = null;
                  nowPLaying = null;
                "
                type="submit"
              >
                Stop
              </button>
            </form>
          </div>
        </li>
      </ul>
    </div>
  </section>
</template>
