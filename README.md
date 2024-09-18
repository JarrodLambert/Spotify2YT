# Instructions

1. **Set Up Spotify API Credentials**

   To access your Spotify playlists, you'll need to create a Spotify app to obtain the necessary credentials.

   a. **Create a Spotify App**

   - Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in with your Spotify account.
   - Click on **"Create an App"**.
   - Fill in the required details and accept the terms.
   - Once the app is created, you'll see your **Client ID** and **Client Secret**.

   b. **Set the Redirect URI**

   - In your app's settings, click on **"Edit Settings"**.
   - Under **"Redirect URIs"**, add a URI (e.g., `http://localhost:8888/callback`).
   - Save the changes.

   c. **Update the Script with Your Credentials**

   Replace the placeholders in the script with your actual credentials:

   ```python
   SPOTIFY_CLIENT_ID = 'YOUR_SPOTIFY_CLIENT_ID'
   SPOTIFY_CLIENT_SECRET = 'YOUR_SPOTIFY_CLIENT_SECRET'
   SPOTIFY_REDIRECT_URI = 'YOUR_SPOTIFY_REDIRECT_URI'  # e.g., 'http://localhost:8888/callback'
   ```

2. **Obtain Your Spotify Playlist ID**

   - Open Spotify and navigate to the playlist you want to convert.
   - Click on the three dots (**...**) next to the playlist name.
   - Select **"Share" > "Copy Link to Playlist"**.
   - The link will look like `https://open.spotify.com/playlist/PLAYLIST_ID`.
   - Extract the `PLAYLIST_ID` from the URL and replace it in the script:

     ```python
     SPOTIFY_PLAYLIST_ID = 'YOUR_SPOTIFY_PLAYLIST_ID'
     ```

3. **Customize Playlist Details**

   In the script, set your desired YouTube Music playlist name and privacy status:

   ```python
   playlist_name = 'Your Playlist Name'  # Replace with your desired name
   privacy_status = 'PRIVATE'  # Options: 'PRIVATE', 'PUBLIC', 'UNLISTED'
   ```

4. **Install Required Libraries**

   Make sure you have both `spotipy` and `ytmusicapi` installed:

   ```bash
   pip install spotipy ytmusicapi
   ```

5. **Run the Script**

   Now you're ready to run the script:

   ```bash
   python your_script_name.py
   ```

---

## How the Script Works

- **Spotify Authentication:**

  - Uses `spotipy.SpotifyOAuth` to authenticate with Spotify.
  - Requires `client_id`, `client_secret`, and `redirect_uri`.

- **Retrieve Spotify Playlist Tracks:**

  - The function `get_spotify_playlist_tracks` fetches all tracks from the specified Spotify playlist.
  - Handles pagination to retrieve playlists with more than 100 tracks.

- **Initialize YouTube Music API:**

  - Loads authenticated headers from `headers_auth.json`.
  - Creates an instance of `YTMusic` for API calls.

- **Create YouTube Music Playlist:**

  - Creates a new playlist on YouTube Music with the specified name and privacy status.

- **Search and Add Tracks:**

  - Iterates over each track from the Spotify playlist.
  - Searches YouTube Music for the track using the song name and artist(s).
  - Adds the best matching track to the YouTube Music playlist.
  - Includes a `time.sleep(1)` call to respect rate limits.

- **Error Handling:**

  - If a track isn't found on YouTube Music, it prints a message and continues.

---

## Notes

- **Rate Limits:** The script includes a delay (`time.sleep(1)`) between API calls to avoid hitting rate limits.
- **Accuracy:** Search results may not always match perfectly due to differences in song titles or availability on YouTube Music.
- **Privacy:** Keep your authentication files (`headers_auth.json`, `headers_raw.txt`) secure, as they contain sensitive information.

---

## Conclusion

This script automates the process of transferring a Spotify playlist to YouTube Music. By following the setup instructions carefully, you can customize and run the script to migrate your playlists seamlessly.

If you have any questions or need further assistance, feel free to ask!