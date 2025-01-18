# Create a new artist

## Description
This ticket requests the implementation of a route that allows the creation of a new artist.

## Request
- **Method:** POST
- **Path:** /artists
- **Body**
  ```json
  {
    "name": "Artist Name",
    "age": 25,
    "bio": "Artist Bio"
  }
  ```

## Response
- **Body**
  ```json
  {
    "id": 123,
    "name": "Artist Name",
    "age": 25,
    "bio": "Artist Bio"
  }
  ```
