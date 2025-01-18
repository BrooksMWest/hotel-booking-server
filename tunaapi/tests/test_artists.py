from rest_framework import status
from rest_framework.test import APITestCase

from tunaapi.models import Artist
from .utils import create_data, refresh_data


class TestArtists(APITestCase):

    @classmethod
    def setUpTestData(cls):
        create_data(cls)

    def setUp(self):
        refresh_data(self)

    def test_create(self):
        new_artist = {
            "name": self.faker.name(),
            "age": self.faker.pyint(min_value=18, max_value=100),
            "bio": self.faker.sentence(nb_words=3)
        }
        response = self.client.post("/artists", new_artist)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.data

        self.assertTrue("id" in data)
        self.assertTrue("name" in data)
        self.assertTrue("age" in data)
        self.assertTrue("bio" in data)

        db_artist = Artist.objects.get(pk=data["id"])
        self.assertEqual(db_artist.name, new_artist["name"])
        self.assertEqual(db_artist.age, new_artist["age"])
        self.assertEqual(db_artist.bio, new_artist["bio"])

    def test_delete(self):
        artist_id = Artist.objects.all()[0].id
        response = self.client.delete(f"/artists/{artist_id}")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse("data" in response)

        artists = Artist.objects.filter(id=artist_id)
        self.assertEqual(len(artists), 0)

    def test_update(self):
        artist_id = Artist.objects.all()[0].id
        updated_artist = {
            "name": self.faker.name(),
            "age": self.faker.pyint(min_value=18, max_value=100),
            "bio": self.faker.sentence(nb_words=3)
        }
        response = self.client.put(
            f"/artists/{artist_id}", updated_artist, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        self.assertTrue("id" in data)
        self.assertTrue("name" in data)
        self.assertTrue("age" in data)
        self.assertTrue("bio" in data)

        db_artist = Artist.objects.get(pk=artist_id)
        self.assertEqual(db_artist.name, updated_artist["name"])
        self.assertEqual(db_artist.age, updated_artist["age"])
        self.assertEqual(db_artist.bio, updated_artist["bio"])

    def test_list(self):
        response = self.client.get("/artists")
        data = response.data

        self.assertEqual(len(data), len(self.artists))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        first_artist = data[0]

        self.assertTrue("id" in first_artist)
        self.assertTrue("name" in first_artist)
        self.assertTrue("age" in first_artist)
        self.assertTrue("bio" in first_artist)

    def test_details(self):
        artist = Artist.objects.all()[0]
        response = self.client.get(f"/artists/{artist.id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data

        self.assertEqual(data["id"], artist.id)
        self.assertEqual(data["name"], artist.name)
        self.assertEqual(data["age"], artist.age)
        self.assertEqual(data["bio"], artist.bio)
        self.assertEqual(data["song_count"], len(artist.songs.all()))
        self.assertEqual(len(data["songs"]), len(artist.songs.all()))

        first_song = data["songs"][0]

        self.assertTrue("id" in first_song)
        self.assertTrue("title" in first_song)
        self.assertTrue("album" in first_song)
        self.assertTrue("length" in first_song)
