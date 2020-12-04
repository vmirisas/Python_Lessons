from random import randrange, seed
from datetime import datetime


class Video:
    def __init__(self, artist, title, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"Artist: {self.artist}, Title: {self.title}, Duration: {self.duration}"


class Playlist:
    def __init__(self, title, description, duration, videos):
        self.title = title
        self.description = description
        self.duration = duration
        self.videos = videos

    def add_video(self, video):
        self.videos += [video]

    def __str__(self):
        st = f"{self.title}, {self.description}, Duration: {self.duration}"
        st += "\n" + "=" * 100
        for video in self.videos:
            st += f"\n{video}"
        st += "\n" + "-" * 100
        st += "\n"
        return st

    def recommendation(self):
        recommended = self.videos[randrange(len(self.videos))]
        return f"We recommend you this video: ({recommended}) \n"


class ClassicalPlaylist(Playlist):
    def __init__(self, title, description, duration, videos, period):
        super().__init__(title, description, duration, videos)
        self.period = period

    def recommendation(self):
        recommended = self.videos[0]
        return recommended


seed(datetime.now())

playlist = Playlist("Amon Amarth Playlist", "Testosterone Heightening Music", "50:06",
                    [Video("Amon Amarth", "The Way of Vikings", "5.15"), Video("Amon Amarth", "Raven's Flight", "5.43"),
                     Video("Amon Amarth", "First Kill", "4.55")])



playlist_classic = ClassicalPlaylist("Beethoven No.9", "", "88.13",
                                     [Video("Beethoven", "Track 01", "03.22"), Video("Beethoven", "Track 02", "04.17")],
                                     "baroque")

print(playlist)
playlist.add_video(Video("Amon Amarth", "Guardians Of Asgaard", "4.33"))
print(playlist)
print(playlist.recommendation())

print(playlist_classic)
print(playlist_classic.recommendation())
