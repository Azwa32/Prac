"""
Create a Playlist class that represents a collection of Track objects. The Playlist class should have the following methods:

__init__: Initializes an empty playlist.
add_track: Adds a Track object to the playlist.
remove_track: Removes a Track object from the playlist.
display: Displays the name, artist, duration, and rating of each Track object in the playlist.
Here's an example of what the completed code might look like:
"""

class Track:
    def __init__(self, name, artist, duration, rating):
        self.name = name
        self.artist = artist
        self.duration = duration
        self.rating = rating

    def display(self):
        print(f"{self.name} by {self.artist} {self.duration} {self.rating}")

class Playlist:
    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)

    def remove_track(self, track):
        self.tracks.remove(track)

    def display(self):
        for track in self.tracks:
            track.display()

# TODO create a playlist object
playlist_1 = Playlist()

# TODO add some track objects to it
track_1 = Track("Snoops Upside Ya Head", "Snoop Dog", "03:30", "MA")
track_2 = Track("Gangam Style", "PSY", "3:30", "PG")
track_3 = Track("Low", "Flow Rida", "3:30", "M15+")

playlist_1.add_track(track_1)
playlist_1.add_track(track_2)
playlist_1.add_track(track_3)

# TODO remove one of the tracks
playlist_1.remove_track(track_1)

# TODO then call the display method to make sure the remaining tracks are displayed correctly
playlist_1.display()
