# Search artists by genre

## Description
This ticket requests the implementation of a route that allows searching artists by genre.

## Request
- **Method:** GET
- **Path:** /artists?genre={genreId}

## Response
- **Body**
  ```json
  {
    "artists": [
      {
        "id": 123,
        "name": "Artist 1",
        "age": 25,
        "bio": "Bio 1"
      },
      {
        "id": 456,
        "name": "Artist 2",
        "age": 30,
        "bio": "Bio 2"
      }
    ]
  }
  ```
- **Status Code:** 200 OK