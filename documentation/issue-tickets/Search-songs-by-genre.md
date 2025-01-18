# Search songs by genre

## Description
This ticket requests the implementation of a route that allows searching songs by genre.

## Request
- **Method:** GET
- **Path:** /songs?genre={genreId}

## Response
- **Body**
  ```json
  {
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
- **Status Code:** 200 OK
