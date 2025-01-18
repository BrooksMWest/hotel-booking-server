# Retrieve a list of all artists

## Description
This ticket requests the implementation of a route that retrieves a list of all artists.

## Request
- **Method:** GET
- **Path:** /artists

## Response
- **Body**
  ```json
  [
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
  ```
