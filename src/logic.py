import pandas as pd
import random

# Mock data for development
DEV_MODE_MOCK_EMOTION = "happy"

PLAYLISTS = {
    "happy": [
        {"track_name": "Happy", "artist_name": "Pharrell Williams", "album_name": "G I R L"},
        {"track_name": "Walking on Sunshine", "artist_name": "Katrina & The Waves", "album_name": "Walking on Sunshine"},
        {"track_name": "Don't Stop Me Now", "artist_name": "Queen", "album_name": "Jazz"},
        {"track_name": "Good as Hell", "artist_name": "Lizzo", "album_name": "Cuz I Love You"},
        {"track_name": "Dancing Queen", "artist_name": "ABBA", "album_name": "Arrival"},
    ],
    "sad": [
        {"track_name": "Someone Like You", "artist_name": "Adele", "album_name": "21"},
        {"track_name": "Hallelujah", "artist_name": "Jeff Buckley", "album_name": "Grace"},
        {"track_name": "Easy On Me", "artist_name": "Adele", "album_name": "30"},
        {"track_name": "Both Sides Now", "artist_name": "Joni Mitchell", "album_name": "Clouds"},
        {"track_name": "My Immortal", "artist_name": "Evanescence", "album_name": "Fallen"},
    ],
    "angry": [
        {"track_name": "You Oughta Know", "artist_name": "Alanis Morissette", "album_name": "Jagged Little Pill"},
        {"track_name": "One Step Closer", "artist_name": "Linkin Park", "album_name": "Hybrid Theory"},
        {"track_name": "Smells Like Teen Spirit", "artist_name": "Nirvana", "album_name": "Nevermind"},
        {"track_name": "Misery Business", "artist_name": "Paramore", "album_name": "Riot!"},
        {"track_name": "In the End", "artist_name": "Linkin Park", "album_name": "Hybrid Theory"},
    ],
    "neutral": [
        {"track_name": "Sweet", "artist_name": "Cigarettes After Sex", "album_name": "Cigarettes After Sex"},
        {"track_name": "Apocalypse", "artist_name": "Cigarettes After Sex", "album_name": "Cigarettes After Sex"},
        {"track_name": "He Went to Paris", "artist_name": "Jimmy Buffett", "album_name": "A White Sport Coat and a Pink Crustacean"},
        {"track_name": "Knockin' on Heaven's Door", "artist_name": "Bob Dylan", "album_name": "Pat Garrett & Billy the Kid"},
        {"track_name": "Fast Car", "artist_name": "Tracy Chapman", "album_name": "Tracy Chapman"},
    ],
    "surprise": [
        {"track_name": "It's Oh So Quiet", "artist_name": "Björk", "album_name": "Post"},
        {"track_name": "Surprise", "artist_name": "Gnarls Barkley", "album_name": "The Odd Couple"},
        {"track_name": "Bohemian Rhapsody", "artist_name": "Queen", "album_name": "A Night at the Opera"},
        {"track_name": "A Day in the Life", "artist_name": "The Beatles", "album_name": "Sgt. Pepper's Lonely Hearts Club Band"},
        {"track_name": "Stay", "artist_name": "Justin Bieber", "album_name": "Justice"},
    ],
    "fear": [
        {"track_name": "Afraid of Everyone", "artist_name": "The National", "album_name": "High Violet"},
        {"track_name": "The Fear", "artist_name": "The Shins", "album_name": "Heartworms"},
        {"track_name": "Getting Older", "artist_name": "Billie Eilish", "album_name": "Happier Than Ever"},
        {"track_name": "bury a friend", "artist_name": "Billie Eilish", "album_name": "WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?"},
        {"track_name": "Thriller", "artist_name": "Michael Jackson", "album_name": "Thriller"},
    ],
    "disgust": [
        {"track_name": "Puke", "artist_name": "Eminem", "album_name": "Encore"},
        {"track_name": "No Scrubs", "artist_name": "TLC", "album_name": "FanMail"},
        {"track_name": "People = Shit", "artist_name": "Slipknot", "album_name": "Iowa"},
        {"track_name": "I'm So Sick", "artist_name": "Flyleaf", "album_name": "Flyleaf"},
        {"track_name": "Down with the Sickness", "artist_name": "Disturbed", "album_name": "The Sickness"},
    ]
}

DEV_MODE_MOCK_PLAYLIST = pd.DataFrame(PLAYLISTS["happy"])


def analyze_emotion(image, dev_mode=True):
    """
    Analyzes the emotion from an image.
    In dev mode, returns a mock emotion.
    Otherwise, would use a library like DeepFace.
    """
    if dev_mode:
        return DEV_MODE_MOCK_EMOTION
    else:
        try:
            from deepface import DeepFace
            # Note: DeepFace.analyze can be slow.
            # The 'detector_backend' can be changed to 'opencv', 'ssd', 'dlib', or 'retinaface'
            analysis = DeepFace.analyze(img_path=image, actions=['emotion'], detector_backend='opencv')
            if isinstance(analysis, list):
                return analysis[0]['dominant_emotion']
            return analysis['dominant_emotion']
        except Exception as e:
            # If face detection fails, return a default emotion
            print(f"Error analyzing emotion: {e}")
            return "neutral"

def get_playlist(emotion):
    """
    Generates a playlist based on the detected emotion from a pre-defined list.
    """
    emotion = emotion.lower()
    default_playlist = PLAYLISTS["neutral"]
    
    playlist_data = PLAYLISTS.get(emotion, default_playlist)
    
    # Return a random sample of up to 5 songs
    sample_size = min(len(playlist_data), 5)
    playlist_sample = random.sample(playlist_data, sample_size)
    
    return pd.DataFrame(playlist_sample)
