# Retrieve a list of all songs

## Description
This ticket requests the implementation of a route that retrieves a list of all songs.

## Request
- **Method:** GET
- **Path:** /songs

## Response
- **Body**
  ```json
  [
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
  ```
