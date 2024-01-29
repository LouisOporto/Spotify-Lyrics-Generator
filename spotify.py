import spotipy, time
from spotipy.oauth2 import SpotifyOAuth

with open("credentials.txt", 'r') as openfile:
    SPOTIPY_CLIENT_ID = openfile.readline().split('\'')[1]
    SPOTIPY_CLIENT_SECRET = openfile.readline().split('\'')[1]
    SPOTIPY_REDIRECT_URI = openfile.readline().split('\'')[1]

''' TO DO LIST
1. Have the crendtial information imported from a secondary file instead immortalized in the code.
2. Make the Auth case much more simpler and cleaner
3. Simultaneously, check if Spotify is actively playing if not reduce request from spotify
4. Settings to config to adjust settings
5. Use pygame to display the name and artist of the song. Display art with image
6. ADD MORE HERE (-----------)
7. Find out the best way to access data from Spotify (reduce calls)
8. Act like a playback tracker with skipping and bar tracking. (more complex)
9. Implement the lyrics part (what is currently being played)
10. Audio Spectrum accurate to base and treble
'''

def retrieve_song():
    # If playing a song will return the song data
    scope = "user-read-playback-state"  # Need a scope of access for Spotify to allow access
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI))

    result = sp.current_playback()
    if result == None:
        return 0

    # Will be replaced to just save info as var and used later for
    print("Currently playing " + result['item']['name'] + " by:")
    for artist in result['item']['artists']:
        print(f"\t{artist['name']} ")
    return result


# check_spotify_active is being removed
def check_spotify_active():
    '''This will be removed since retrieve_song already checks for state and data'''
    # Checks if spotify is currently opened and currently playing a song
    # Will return a boolean true if active and false if not
    scope = "user-read-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI))

    results = sp.get_
    return True


def retrieve_lyrics():
    # Search for lyrics online to be returned either as a string or graphical display
    pass


def init():
    # Initialize pygame to display text while the song plays
    pass


def main():
    # Area for main loop of the game where it checks for activity and recieves updates at a set interval
    print("Welcome to Spotify Lyrics")

    init()
    finished = 1 # temporary 1 og was (20)
    while finished != 0:

        data = retrieve_song()
        if data == 0:
            print("Not playing rn :)")
        time.sleep(5) # delay to prevent over pinging Spotify (better version soon to optimize pinging)
        finished -= 1


if __name__ == "__main__":
    main()
