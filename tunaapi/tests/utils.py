import random

from faker import Faker

from tunaapi.models import Artist, Song, Genre, SongGenre


def create_data(cls):
    cls.faker = Faker()
    cls.artists = []
    cls.songs = []
    cls.genres = []
    cls.song_genres = []

    for _ in range(0, 10):
        artist = Artist.objects.create(
            name=cls.faker.name(),
            age=cls.faker.pyint(
                min_value=18,
                max_value=100
            ),
            bio=cls.faker.sentence()
        )
        cls.artists.append(artist)

        genre = Genre.objects.create(
            description=cls.faker.sentence()
        )
        cls.genres.append(genre)

        for _ in range(0, random.randint(1, 3)):
            song = Song.objects.create(
                title=cls.faker.sentence(nb_words=5),
                artist=artist,
                album=cls.faker.sentence(nb_words=2),
                length=cls.faker.pyint(
                    min_value=15,
                    max_value=180
                )
            )
            cls.songs.append(song)

            song_genre = SongGenre.objects.create(
                song=song,
                genre=genre
            )
            cls.song_genres.append(song_genre)


def refresh_data(self):
    for artist in self.artists:
        artist.refresh_from_db()
    for song in self.songs:
        song.refresh_from_db()
    for genre in self.genres:
        genre.refresh_from_db()
    for song_genre in self.song_genres:
        song_genre.refresh_from_db()
