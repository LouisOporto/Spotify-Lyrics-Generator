import spotipy
from spotipy.oauth2 import SpotifyOAuth

import spotipy.util as util
import sys

import time

''' alternative
export SPOTIPY_CLIENT_ID='c6ce5af1c46b4145bd77d022b9f5397f'
export SPOTIPY_CLIENT_SECRET='176e9e416772492e94bb6d9fa908e2c1'
export SPOTIPY_REDIRECT_URI='http://localhost:3000'
'''
SPOTIPY_CLIENT_ID='c6ce5af1c46b4145bd77d022b9f5397f'
SPOTIPY_CLIENT_SECRET='176e9e416772492e94bb6d9fa908e2c1'
SPOTIPY_REDIRECT_URI='http://localhost:3000'

''' TO DO
1. Make the Auth case much more simpler and cleaner
2. Use pygame to display the name and artist of the song. Display art with image
3. Simultaneously, check if Spotify is actively playing if not reduce request from spotify
4. Act like a playback tracker with skipping and bar tracking. (more complex)
5. Implement the lyrics part (what is currently being played)
'''
def retrieve_song():
    # If playing a song will return the song data
    scope = "user-read-currently-playing"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI))
    results = sp.current_user_playing_track()
    track = results['item']
    print("Currently playing " + track['name'] + " by " + track['artists'][0]['name'])
    return track

def check_spotify_active():
    # Checks if spotify is currently opened and currently playing a song
    pass


def retrieve_lyrics():
    # Search for lyrics online to be returned either as a string or graphical display
    pass

def init():
    # Initialize pygame to display text while the song plays
    pass

def main():

    # Area for main loop of the game where it checks for activity and recieves updates at a set interval
    print("Welcome to Spotify Lyrics")
    interval = int(input("At what interval do you want to update the song?(5 - 30 sec):"))

    init()
    finished = 1 # temporary 1 og was (20)
    while finished != 0:
        track = retrieve_song()
        time.sleep(interval)
        finished -= 1


if __name__ == "__main__":
    main()

'''
{'album': {'album_type': 'album',
           'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/246dkjvS1zLTtiykXe5h60'},
                         'href': 'https://api.spotify.com/v1/artists/246dkjvS1zLTtiykXe5h60',
                         'id': '246dkjvS1zLTtiykXe5h60',
                         'name': 'Post Malone',
                         'type': 'artist',
                         'uri': 'spotify:artist:246dkjvS1zLTtiykXe5h60'}],
           'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'],
           'external_urls': {'spotify': 'https://open.spotify.com/album/4g1ZRSobMefqF6nelkgibi'},
           'href': 'https://api.spotify.com/v1/albums/4g1ZRSobMefqF6nelkgibi',
           'id': '4g1ZRSobMefqF6nelkgibi',
           'images': [{'height': 640,
                       'url': 'https://i.scdn.co/image/ab67616d0000b2739478c87599550dd73bfa7e02',
                       'width': 640},
                      {'height': 300,
                       'url': 'https://i.scdn.co/image/ab67616d00001e029478c87599550dd73bfa7e02',
                       'width': 300},
                      {'height': 64,
                       'url': 'https://i.scdn.co/image/ab67616d000048519478c87599550dd73bfa7e02',
                       'width': 64}],
           'name': "Hollywood's Bleeding",
           'release_date': '2019-09-06',
           'release_date_precision': 'day',
           'total_tracks': 17,
           'type': 'album',
           'uri': 'spotify:album:4g1ZRSobMefqF6nelkgibi'},
 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/246dkjvS1zLTtiykXe5h60'},
              'href': 'https://api.spotify.com/v1/artists/246dkjvS1zLTtiykXe5h60',
              'id': '246dkjvS1zLTtiykXe5h60',
              'name': 'Post Malone',
              'type': 'artist',
              'uri': 'spotify:artist:246dkjvS1zLTtiykXe5h60'}],
 'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'],
 'disc_number': 1,
 'duration_ms': 215280,
 'explicit': False,
 'external_ids': {'isrc': 'USUM71915699'},
 'external_urls': {'spotify': 'https://open.spotify.com/track/21jGcNKet2qwijlDFuPiPb'},
 'href': 'https://api.spotify.com/v1/tracks/21jGcNKet2qwijlDFuPiPb',
 'id': '21jGcNKet2qwijlDFuPiPb',
 'is_local': False,
 'name': 'Circles',
 'popularity': 88,
 'preview_url': 'https://p.scdn.co/mp3-preview/193a0924b0f73d211131bf2fb0bddb7202176202?cid=c6ce5af1c46b4145bd77d022b9f5397f',
 'track_number': 6,
 'type': 'track',
 'uri': 'spotify:track:21jGcNKet2qwijlDFuPiPb'}
'''
