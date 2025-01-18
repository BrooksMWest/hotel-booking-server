from rest_framework import status
from rest_framework.test import APITestCase

from tunaapi.models import Song
from .utils import create_data, refresh_data


class TestSongs(APITestCase):

    @classmethod
    def setUpTestData(cls):
        create_data(cls)

    def setUp(self):
        refresh_data(self)

    def test_create(self):
        artist = self.artists[0]
        new_song = {
            "title": self.faker.sentence(nb_words=3),
            "artist_id": artist.id,
            "album": self.faker.sentence(nb_words=3),
            "length": self.faker.pyint(min_value=30, max_value=180)
        }
        response = self.client.post("/songs", new_song)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.data

        self.assertTrue("id" in data)
        self.assertTrue("title" in data)
        self.assertTrue("artist_id" in data)
        self.assertTrue("album" in data)
        self.assertTrue("length" in data)

        db_song = Song.objects.get(pk=data["id"])
        self.assertEqual(db_song.title, new_song["title"])
        self.assertEqual(db_song.artist.id, new_song["artist_id"])
        self.assertEqual(db_song.album, new_song["album"])
        self.assertEqual(db_song.length, new_song["length"])

    def test_delete(self):
        song_id = Song.objects.all()[0].id
        response = self.client.delete(f"/songs/{song_id}")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse("data" in response)

        song = Song.objects.filter(id=song_id)
        self.assertEqual(len(song), 0)

    def test_update(self):
        artist = self.artists[0]
        song_id = Song.objects.all()[0].id
        updated_song = {
            "title": self.faker.sentence(nb_words=3),
            "artist_id": artist.id,
            "album": self.faker.sentence(nb_words=3),
            "length": self.faker.pyint(min_value=30, max_value=180)
        }
        response = self.client.put(
            f"/songs/{song_id}", updated_song, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data

        self.assertTrue("id" in data)
        self.assertTrue("title" in data)
        self.assertTrue("artist_id" in data)
        self.assertTrue("album" in data)
        self.assertTrue("length" in data)

        db_song = Song.objects.get(pk=song_id)
        self.assertEqual(db_song.title, updated_song["title"])
        self.assertEqual(db_song.artist.id, updated_song["artist_id"])
        self.assertEqual(db_song.album, updated_song["album"])
        self.assertEqual(db_song.length, updated_song["length"])

    def test_list(self):
        response = self.client.get("/songs")
        data = response.data

        self.assertEqual(len(data), len(self.songs))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        single_song = data[0]
        self.assertTrue("id" in single_song)
        self.assertTrue("title" in single_song)
        self.assertTrue("artist_id" in single_song)
        self.assertTrue("album" in single_song)
        self.assertTrue("length" in single_song)

    def test_details(self):
        song = Song.objects.all()[0]
        response = self.client.get(f"/songs/{song.id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data

        self.assertEqual(data["id"], song.id)
        self.assertEqual(data["title"], song.title)
        self.assertEqual(data["album"], song.album)
        self.assertEqual(data["length"], song.length)

        artist = data["artist"]

        self.assertEqual(artist["id"], song.artist.id)
        self.assertEqual(artist["name"], song.artist.name)
        self.assertEqual(artist["age"], song.artist.age)
        self.assertEqual(artist["bio"], song.artist.bio)

        first_genre = data["genres"][0]

        self.assertTrue("id" in first_genre)
        self.assertTrue("description" in first_genre)

    # # def test_stretch_filter_by_genre(self):
    # #     response = self.client.get("")
