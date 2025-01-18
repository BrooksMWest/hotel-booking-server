# Retrieve popular genres based on the number of associated songs

## Description
This ticket requests the implementation of a route that retrieves a list of popular genres based on the number of songs associated with each genre.

## Request
- **Method:** GET
- **Path:** /genres/popular

## Response
- **Body**
  ```json
  {
    "genres": [
      {
        "id": 123,
        "description": "Genre 1",
        "song_count": 10
      },
      {
        "id": 456,
        "description": "Genre 2",
        "song_count": 5
      }
    ]
  }
  ```
- **Status Code:** 200 OK