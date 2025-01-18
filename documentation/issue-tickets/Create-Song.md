# Create a new song

## Description
This ticket requests the implementation of a route that allows the creation of a new song.

## Request
- **Method:** POST
- **Path:** /songs
- **Body**
  ```json
  {
    "title": "My Song",
    "artist_id": 123,
    "album": "My Album",
    "length": 180
  }
  ```

## Response
- **Body**
  ```json
  {
    "id": 456,
    "title": "My Song",
    "artist_id": 123,
    "album": "My Album",
    "length": 180
  }
  ```
