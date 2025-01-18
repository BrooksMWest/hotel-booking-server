# Create a new genre

## Description
This ticket requests the implementation of a route that allows the creation of a new genre.

## Request
- **Method:** POST
- **Path:** /genres
- **Body**
  ```json
  {
    "description": "Genre Description"
  }
  ```

## Response
- **Body**
  ```json
  {
    "id": 123,
    "description": "Genre Description"
  }
  ```
