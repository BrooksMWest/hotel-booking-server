# Update an existing genre

## Description
This ticket requests the implementation of a route that allows updating an existing genre.

## Request
- **Method:** PUT
- **Path:** /genres/{genreId}
- **Body**
  ```json
  {
    "description": "Updated Genre Description"
  }
  ```

## Response
- **Body**
  ```json
  {
    "id": {genreId},
    "description": "Updated Genre Description"
  }
  ```
- **Status Code:** 200 OK
