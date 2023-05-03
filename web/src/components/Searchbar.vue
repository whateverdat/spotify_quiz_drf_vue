<script>
import axios from 'axios';
export default {
  data() {
    return {
      info: null,
      query: '',
      playlistError: false,
      playlistLoading: false,
    };
  },
  methods: {
    // Consume API to load playlist info
    callPlaylist(query) {
      if (query.length === 0) {
        return;
      }
      this.playlistLoading = true;
      this.playlistError = false;
      axios
        .get(`http://127.0.0.1:8000/search-playlist/${query}`)
        .then((response) => {
          this.info = response.data;
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
          this.playlistError = true;
        })
        .finally(() => {
          this.playlistLoading = false;
        });
    },
  },
};
</script>
<template>
  <form v-if="!info">
    <input
      v-model="query"
      placeholder="Enter a playlist name"
      minlength="3"
      maxlength="200"
    />
    <button
      class="border-none hover:text-gray-700"
      type="submit"
      @click.prevent="callPlaylist(query)"
    >
      Search
    </button>
  </form>
  <button v-if="this.info" @click="this.info = null">Return to Search</button>
  <!-- Load this component when there is response -->
  <SearchResults
    v-if="playlistLoading || info || playlistError"
    :data="info"
    :playlistLoading="playlistLoading"
    :playlistError="playlistError"
  ></SearchResults>
</template>
