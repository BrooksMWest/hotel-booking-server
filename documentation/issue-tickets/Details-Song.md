# Retrieve details of a single song with associated genres and artist details

## Description
This ticket requests the implementation of a route that retrieves the details of a single song, including its associated genres and artist details.

## Request
- **Method:** GET
- **Path:** /songs/{songId}

## Response
- **Body**
  ```json
  {
    "id": {songId},
    "title": "Song Title",
    "artist": {
      "id": 456,
      "name": "Artist Name",
      "age": 30,
      "bio": "Artist Bio"
    },
    "album": "Album Name",
    "length": 180,
    "genres": [
      {
        "id": 789,
        "description": "Genre 1"
      },
      {
        "id": 123,
        "description": "Genre 2"
      }
    ]
  }
  ```
