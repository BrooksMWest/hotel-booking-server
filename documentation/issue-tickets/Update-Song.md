# Update an existing song

## Description
This ticket requests the implementation of a route that allows updating an existing song.

## Request
- **Method:** PUT
- **Path:** /songs/{songId}
- **Body**
  ```json
  {
    "title": "Updated Song Title",
    "artist_id": 123,
    "album": "Updated Album Name",
    "length": 240
  }
  ```

## Response
- **Body**
  ```json
  {
    "id": {songId},
    "title": "Updated Song Title",
    "artist_id": 123,
    "album": "Updated Album Name",
    "length": 240
  }
  ```
- **Status Code:** 200 OK
