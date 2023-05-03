<script>
import axios from 'axios';
export default {
  data() {
    return {
      // Loaded when user requests to see available tracks
      tracks: null,
      tracksError: false,
      tracksLoading: false,
      playlistID: null,
      // Loaded when user requests for a session
      session: null,
      sessionLoading: false,
      sessionError: false,
    };
  },
  props: ['data', 'playlistLoading', 'playlistError'],
  methods: {
    // Consumes API to get tracks, using preloaded playlist ID
    callTracks(id) {
      this.tracksLoading = true;
      axios
        .get(`http://127.0.0.1:8000/get-playlist-tracks/${id}`)
        .then((response) => {
          this.tracks = response.data.tracks;
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
          this.tracksError = true;
        })
        .finally(() => {
          this.tracksLoading = false;
        });
    },
    // Reset tracks variable
    resetTracks() {
      this.tracks = null;
    },
    // Consumes API to create session
    createSession(id) {
      this.sessionLoading = true;
      axios
        .get(`http://127.0.0.1:8000/get-playlist-tracks/${id}`)
        .then((response) => {
          this.session = response.data;
          console.log(response);
        })
        .catch((err) => {
          console.log(err);
          this.sessionError = true;
        })
        .finally(() => {
          this.sessionLoading = false;
        });
    },
  },
};
</script>
<template>
  <!-- If there is a session, load only the session component -->
  <div v-if="session || sessionLoading || sessionError">
    <form>
      <button
        type="submit"
        @click.prevent="
          session = null;
          sessionLoading = false;
          sessionError = false;
        "
      >
        Return to Playlist
      </button>
    </form>
    <!-- Session Error -->
    <section v-if="sessionError">
      <h3 class="text-black">ERROR</h3>
    </section>
    <section v-else>
      <!-- Session is loading, API call is on progress -->
      <div v-if="sessionLoading">
        <h3 class="text-black">Loading...</h3>
      </div>
      <!-- Session component -->
      <Session v-if="session" :session="session"></Session>
    </section>
  </div>
  <!-- No session -->
  <div v-else>
    <!-- Playlist Error -->
    <section v-if="playlistError">
      <h3 class="text-black">ERROR</h3>
    </section>
    <!-- Playlist Loading -->
    <section v-else class="text-black">
      <div v-if="playlistLoading">
        <h3 class="text-black">Loading...</h3>
      </div>
      <!-- Playlist is loaded -->
      <div v-else>
        <h1>{{ data.name }}</h1>
        <h2>{{ data.description }}</h2>
        <img class="w-36 mx-auto" :src="data.image" :alt="data.name" />
        <h3>{{ data.songs }} songs.</h3>
        <form>
          <!-- To call API for previewing playlist tracks -->
          <button
            @click.prevent="
              callTracks(data.spotifyID);
              playlistID = data.spotifyID;
            "
            type="submit"
          >
            Browse Tracks
          </button>
        </form>
        <!-- To call API to create session -->
        <form>
          <button @click.prevent="createSession(data.spotifyID)" type="submit">
            Start session
          </button>
        </form>
      </div>
    </section>
    <!-- Playlist Preview -->
    <ExpandedPlaylist
      v-if="
        (tracks || tracksLoading || tracksError) &&
        playlistID == data.spotifyID &&
        !playlistLoading
      "
      :tracks="tracks"
      :tracksError="tracksError"
      :tracksLoading="tracksLoading"
    ></ExpandedPlaylist>
  </div>
</template>
