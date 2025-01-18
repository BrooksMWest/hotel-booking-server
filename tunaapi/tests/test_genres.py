from rest_framework import status
from rest_framework.test import APITestCase

from tunaapi.models import Genre, SongGenre

from .utils import create_data, refresh_data


class TestGenres(APITestCase):

    @classmethod
    def setUpTestData(cls):
        create_data(cls)

    def setUp(self):
        refresh_data(self)

    def test_create(self):
        new_genre= {
            "description": self.faker.sentence(nb_words=3)
        }
        response = self.client.post("/genres", new_genre)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.data

        self.assertTrue("id" in data)
        self.assertTrue("description" in data)

        db_genre = Genre.objects.get(pk=data["id"])
        self.assertEqual(db_genre.description, new_genre["description"])

    def test_delete(self):
        genre_id = Genre.objects.all()[0].id
        response = self.client.delete(f"/genres/{genre_id}")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse("data" in response)

        genre = Genre.objects.filter(id=genre_id)
        self.assertEqual(len(genre), 0)

    def test_update(self):
        genre_id = Genre.objects.all()[0].id
        updated_genre = {
            "description": self.faker.sentence(nb_words=3)
        }
        response = self.client.put(
            f"/genres/{genre_id}", updated_genre, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        self.assertTrue("id" in data)
        self.assertTrue("description" in data)

        db_genre = Genre.objects.get(pk=genre_id)
        self.assertEqual(db_genre.description, updated_genre["description"])

    def test_list(self):
        response = self.client.get("/genres")
        data = response.data

        self.assertEqual(len(data), len(self.genres))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        first_genre = data[0]
        self.assertTrue("id" in first_genre)
        self.assertTrue("description" in first_genre)

    def test_details(self):
        genre = Genre.objects.all()[0]
        response = self.client.get(f"/genres/{genre.id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data

        self.assertEqual(data["id"], genre.id)
        self.assertEqual(data["description"], genre.description)
        song_genres = SongGenre.objects.filter(genre=genre)
        self.assertEqual(len(data["songs"]), len(song_genres))

        first_song = data["songs"][0]

        self.assertTrue("id" in first_song)
        self.assertTrue("title" in first_song)
        self.assertTrue("artist_id" in first_song)
        self.assertTrue("album" in first_song)
        self.assertTrue("length" in first_song)
