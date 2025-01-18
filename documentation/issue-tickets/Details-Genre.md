# Retrieve details of a single genre with associated songs

## Description
This ticket requests the implementation of a route that retrieves the details of a single genre, including the songs associated with it.

## Request
- **Method:** GET
- **Path:** /genres/{genreId}

#### Response
- **Body**
  ```json
  {
    "id": {genreId},
    "description": "Genre Description",
    "songs": [
      {
        "id": 123,
        "title": "Song 1",
        "artist_id": 456,
        "album": "Album 1",
        "length": 180
      },
      {
        "id": 789,
        "title": "Song 2",
        "artist_id": 456,
        "album": "Album 2",
        "length": 240
      }
    ]
  }
  ```
