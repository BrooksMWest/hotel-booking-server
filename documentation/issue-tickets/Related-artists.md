# Retrieve related artists with similar genres

## Description
This ticket requests the implementation of a route that retrieves a list of related artists based on similar genres.

## Request
- **Method:** GET
- **Path:** /artists/{artistId}/related

## Response
- **Body**
  ```json
  {
    "artists": [
      {
        "id": 123,
        "name": "Related Artist 1"
      },
      {
        "id": 456,
        "name": "Related Artist 2"
      }
    ]
  }
  ```
- **Status Code:** 200 OK